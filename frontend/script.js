const inputMessage = document.getElementById("inputMessage");
const sendBtn = document.getElementById("sendBtn");
const chatbox = document.getElementById("chatbox");


function appendMessage(text, sender) {
    const msgDiv = document.createElement("div");
    msgDiv.classList.add("message", sender);

    if (sender === "bot") {
        const avatar = document.createElement("div");
        avatar.classList.add("message-avatar", "bot-avatar");
        avatar.textContent = "Z";
        msgDiv.appendChild(avatar);
    }

    const bubble = document.createElement("div");
    bubble.classList.add("message-content");
    bubble.textContent = text;

    msgDiv.appendChild(bubble);
    chatbox.appendChild(msgDiv);
    chatbox.scrollTop = chatbox.scrollHeight;
}



async function sendMessage(){
    const message=inputMessage.value.trim();

    if(!message) return ; 
    appendMessage(message,"user");
    inputMessage.value = '';
    sendBtn.disabled=true;


    try {
        const response = await fetch('https://zenzone-pq9t.onrender.com', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message }),
        });

        if (!response.ok) throw new Error("Network response was not ok");

        const data = await response.json();
        // data.reply
        appendMessage(data.reply,"bot")

    } catch (error) {
        appendMessage('Error: Could not reach the server.','bot');
    } finally{
        sendBtn.disabled=false;
        inputMessage.focus();
    }
    

}

// event
sendBtn.addEventListener("click",sendMessage)
inputMessage.addEventListener("keypress",function (e){
    if (e.key === "Enter") sendMessage();
})