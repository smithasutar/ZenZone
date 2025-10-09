🧘‍♀️ ZenZone an AI Therapy Companion

ZenZone is a simple web-based chat application that provides supportive, AI-powered conversations for mental wellness.
It is not a replacement for professional care, but a space for calm, mindful interaction and emotional reflection.

🚀 Features

💬 Real-time Chat —> Talk with your AI therapy companion in a responsive chat interface.

🎨 Modern UI —> Elegant gradients, soft animations, and clean layout.

🗨️ Chat Bubbles —> Messages styled with speech tails and avatars for clarity.

🤖 Bot Avatar (Z) —> Clearly distinguishes AI messages from user input.

📱 Responsive Design —> Works seamlessly across desktop and mobile.

⚠️ Mental Health Disclaimer Banner —> Prominent reminder that ZenZone is for wellness, not medical advice.

🛠️ Setup & Usage
1. Clone the Repository

2. Open Locally

You can simply open the index.html file in your web browser to start using the app.

3. (Optional) Connect to Backend API

If your chat is configured to use a FastAPI backend (e.g., http://127.0.0.1:8000/chat):

Run your FastAPI server:

uvicorn main:app --reload


Ensure the backend returns JSON responses like:

{
  "reply": "Hello! How are you feeling today?"
}

⚠️ Disclaimer

ZenZone is not a substitute for professional mental health care.
If you are experiencing a mental health crisis or need immediate help, please contact emergency services or a licensed mental health professional.
