

# Import necessary libraries for building the chatbot app
import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Load API key from .env file and set it for OpenAI
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Configure the Streamlit app
st.set_page_config(page_title="Chatbot with Memory", layout="centered")
st.title("🧠 Chatbot with In-Chat Memory")

# Initialize session state for chat messages and memory if not already present
if "messages" not in st.session_state:
  st.session_state.messages = [
    {"role": "system", "content": "You are a helpful assistant that remembers facts given during the conversation."}
  ]
if "memory" not in st.session_state:
  st.session_state.memory = {}

# Display the chatbot's memory in an expandable section
with st.expander("📌 Memory (what the bot remembers)", expanded=False):
  if st.session_state.memory:
    for k, v in st.session_state.memory.items():
      st.markdown(f"**{k.capitalize()}**: {v}")
  else:
    st.info("No memory yet.")

# User input for chat
user_input = st.text_input("💬 You:", key="input")
if user_input:
  # Add user message to the conversation history
  st.session_state.messages.append({"role": "user", "content": user_input})

  # Inject memory facts into the prompt for the assistant
  memory_prompt = "\n".join([f"{k}: {v}" for k, v in st.session_state.memory.items()])
  memory_injection = {"role": "system", "content": f"Here are the facts you remember:\n{memory_prompt}"}
  full_messages = [st.session_state.messages[0], memory_injection] + st.session_state.messages[1:]

  # Get assistant's reply from OpenAI API
  with st.spinner("Thinking..."):
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=full_messages
    )

  reply = response.choices[0].message.content
  st.session_state.messages.append({"role": "assistant", "content": reply})

  # Extract and store facts from user input for memory
  if "my name is" in user_input.lower():
    name = user_input.split("my name is")[-1].strip().split()[0]
    st.session_state.memory["name"] = name
  if "i'm interested in" in user_input.lower():
    interest = user_input.split("i'm interested in")[-1].strip().split(".")[0]
    st.session_state.memory["interest"] = interest

# Display the conversation history
st.markdown("### 💬 Conversation")
for msg in st.session_state.messages[1:]:
  if msg["role"] == "user":
    st.markdown(f"**🧑 You:** {msg['content']}")
  else:
    st.markdown(f"**🤖 Bot:** {msg['content']}")

# Allow user to download the chat history as a text file
if len(st.session_state.messages) > 1:
  full_chat = "\n".join(
    [f"{msg['role'].capitalize()}: {msg['content']}" for msg in st.session_state.messages[1:]]
  )
  st.download_button("⬇️ Download Chat", full_chat, file_name="chat_history.txt")
# Allow user to clear the chat and memory
if st.button("🗑️ Clear Chat and Memory"):
  st.session_state.messages = [st.session_state.messages[0]]  # Keep the system message
  st.session_state.memory = {}
  st.success("Chat and memory cleared!")