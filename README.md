**ZenZone – AI Therapy Companion**

ZenZone is a simple chat web application that provides supportive conversations through an AI therapy companion (through FastAPI).
It is designed for general mental wellness support, not as a replacement for professional care.

🚀 Features

💬 Real-time chat between user and AI bot

🎨 Modern UI with gradient backgrounds and smooth animations

🗨️ Speech bubble messages with tails pointing to avatars

🤖 Bot avatar (Z) for easy distinction

📱 Responsive design for desktop and mobile

⚠️ Warning banner for mental health disclaimer


🛠️ Setup & Usage
1. Clone the Repository
git clone https://github.com/yourusername/zenzone.git
cd zenzone

2. Open Locally

- Simply open index.html in your browser.

3. Backend (Optional)

- If you’re connecting to an API (like FastAPI at http://127.0.0.1:8000/chat in your code):

- Start your backend server: uvicorn main:app --reload

Make sure it returns JSON responses like:

{ "reply": "Hello! How are you feeling today?" }

⚠️ Disclaimer

ZenZone is not a substitute for professional mental health care.
If you are in crisis, please call emergency services or reach out to a licensed professional.
