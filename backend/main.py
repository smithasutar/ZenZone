import os
import logging
import uuid
from typing import List, Dict
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv

# Load env locally (optional on Render)
load_dotenv()

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Groq client
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# FastAPI app
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)

# In-memory chat history
chat_sessions: Dict[str, List[Dict[str, str]]] = {}

# Request models
class ChatRequest(BaseModel):
    message: str
    session_id: str = None
    temperature: float = 0.7
    max_tokens: int = 256

class ClearRequest(BaseModel):
    session_id: str

# Bot response
def get_bot_response(user_message: str, session_id: str, temperature: float, max_tokens: int) -> str:
    if session_id not in chat_sessions:
        chat_sessions[session_id] = [{"role": "system", "content": "You are ZenZone, a supportive AI therapy companion."}]
    chat_sessions[session_id].append({"role": "user", "content": user_message})

    try:
        chat_completion = client.chat.completions.create(
            messages=chat_sessions[session_id],
            model="llama-3.3-70b-versatile",
            stream=False,
            temperature=temperature,
            max_tokens=max_tokens,
        )
        reply = chat_completion.choices[0].message.content
        chat_sessions[session_id].append({"role": "assistant", "content": reply})
        return reply
    except Exception as e:
        logger.error(f"Error in Groq API: {e}")
        raise HTTPException(status_code=500, detail="AI service unavailable.")

# Endpoints
@app.post("/chat")
async def chat(request: ChatRequest):
    session_id = request.session_id or str(uuid.uuid4())
    reply = get_bot_response(request.message, session_id, request.temperature, request.max_tokens)
    return {"reply": reply, "session_id": session_id}

@app.post("/clear")
async def clear_history(request: ClearRequest):
    if request.session_id in chat_sessions:
        del chat_sessions[request.session_id]
        return {"status": "cleared"}
    return {"status": "not_found"}

@app.get("/health")
async def health_check():
    return {"status": "ok", "active_sessions": len(chat_sessions)}

# Start server
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
