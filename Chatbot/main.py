# Import necessary libraries for building the chatbot app
import streamlit as st
import openai
import os
import re
import json
from datetime import datetime
from dotenv import load_dotenv

# Load API key from .env file and set it for OpenAI
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Configure the Streamlit app
st.set_page_config(page_title="Enhanced Chatbot with Memory", layout="centered", page_icon="🧠")
st.title("🧠 Enhanced Chatbot with Memory")

# Initialize session state for chat messages and memory if not already present
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful assistant that remembers facts given during the conversation. When you learn new information about the user, acknowledge it and use it in future responses."}
    ]

if "memory" not in st.session_state:
    st.session_state.memory = {}

if "conversation_started" not in st.session_state:
    st.session_state.conversation_started = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Enhanced memory extraction function
def extract_facts_from_text(text):
    """Extract various types of facts from user input"""
    facts = {}
    text_lower = text.lower()
    
    # Name extraction (multiple patterns)
    name_patterns = [
        r"my name is (\w+)",
        r"i'm (\w+)",
        r"i am (\w+)",
        r"call me (\w+)"
    ]
    
    for pattern in name_patterns:
        match = re.search(pattern, text_lower)
        if match:
            facts["name"] = match.group(1).capitalize()
            break
    
    # Interest extraction
    interest_patterns = [
        r"i'm interested in (.+?)(?:\.|$)",
        r"i like (.+?)(?:\.|$)",
        r"i love (.+?)(?:\.|$)",
        r"my hobby is (.+?)(?:\.|$)",
        r"i enjoy (.+?)(?:\.|$)"
    ]
    
    for pattern in interest_patterns:
        match = re.search(pattern, text_lower)
        if match:
            interest = match.group(1).strip()
            if "interests" not in facts:
                facts["interests"] = []
            if interest not in facts["interests"]:
                facts["interests"] = facts.get("interests", []) + [interest]
            break
    
    # Age extraction
    age_match = re.search(r"i am (\d+) years old|i'm (\d+)", text_lower)
    if age_match:
        age = age_match.group(1) or age_match.group(2)
        facts["age"] = age
    
    # Location extraction
    location_patterns = [
        r"i live in (.+?)(?:\.|$)",
        r"i'm from (.+?)(?:\.|$)",
        r"i am from (.+?)(?:\.|$)"
    ]
    
    for pattern in location_patterns:
        match = re.search(pattern, text_lower)
        if match:
            facts["location"] = match.group(1).strip().title()
            break
    
    # Job/Profession extraction
    job_patterns = [
        r"i work as (.+?)(?:\.|$)",
        r"i'm a (.+?)(?:\.|$)",
        r"i am a (.+?)(?:\.|$)",
        r"my job is (.+?)(?:\.|$)"
    ]
    
    for pattern in job_patterns:
        match = re.search(pattern, text_lower)
        if match:
            facts["profession"] = match.group(1).strip()
            break
    
    return facts

# Display the chatbot's memory in an enhanced expandable section
with st.expander("📌 Memory Bank (what I remember about you)", expanded=False):
    if st.session_state.memory:
        col1, col2 = st.columns(2)
        
        with col1:
            for i, (k, v) in enumerate(st.session_state.memory.items()):
                if i % 2 == 0:  # Even indices go to first column
                    if isinstance(v, list):
                        st.markdown(f"**{k.capitalize()}**: {', '.join(v)}")
                    else:
                        st.markdown(f"**{k.capitalize()}**: {v}")
        
        with col2:
            for i, (k, v) in enumerate(st.session_state.memory.items()):
                if i % 2 == 1:  # Odd indices go to second column
                    if isinstance(v, list):
                        st.markdown(f"**{k.capitalize()}**: {', '.join(v)}")
                    else:
                        st.markdown(f"**{k.capitalize()}**: {v}")
        
        # Memory management buttons
        col1, col2 = st.columns(2)
        with col1:
            if st.button("📥 Export Memory", key="export_memory"):
                memory_json = json.dumps(st.session_state.memory, indent=2)
                st.download_button(
                    "⬇️ Download Memory",
                    memory_json,
                    file_name=f"chatbot_memory_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                    mime="application/json"
                )
        
        with col2:
            if st.button("🗑️ Clear Memory Only", key="clear_memory"):
                st.session_state.memory = {}
                st.success("Memory cleared!")
                st.rerun()
    else:
        st.info("💭 I haven't learned anything about you yet. Tell me about yourself!")

# Sidebar with conversation stats
with st.sidebar:
    st.header("📊 Conversation Stats")
    st.metric("Messages Exchanged", len(st.session_state.messages) - 1)
    st.metric("Facts Remembered", len(st.session_state.memory))
    st.text(f"Started: {st.session_state.conversation_started}")
    
    st.header("⚙️ Settings")
    temperature = st.slider("Response Creativity", 0.0, 1.0, 0.7, 0.1)
    max_tokens = st.slider("Max Response Length", 50, 500, 150)

# Main chat interface
st.markdown("### 💬 Chat with me!")

# User input for chat
user_input = st.text_input("💬 You:", key="input", placeholder="Tell me about yourself or ask me anything...")

if user_input:
    # Add user message to the conversation history
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Extract and store facts from user input for memory
    new_facts = extract_facts_from_text(user_input)
    
    # Update memory with new facts
    for key, value in new_facts.items():
        if key == "interests" and key in st.session_state.memory:
            # Merge interests lists
            existing_interests = st.session_state.memory[key] if isinstance(st.session_state.memory[key], list) else [st.session_state.memory[key]]
            combined_interests = list(set(existing_interests + value))
            st.session_state.memory[key] = combined_interests
        else:
            st.session_state.memory[key] = value
    
    # Create enhanced memory context for the AI
    memory_context = ""
    if st.session_state.memory:
        memory_items = []
        for k, v in st.session_state.memory.items():
            if isinstance(v, list):
                memory_items.append(f"{k}: {', '.join(v)}")
            else:
                memory_items.append(f"{k}: {v}")
        memory_context = "What you know about the user:\n" + "\n".join(memory_items)
    
    memory_injection = {"role": "system", "content": memory_context} if memory_context else None
    
    # Prepare messages for API call
    api_messages = [st.session_state.messages[0]]
    if memory_injection:
        api_messages.append(memory_injection)
    api_messages.extend(st.session_state.messages[1:])
    
    # Get assistant's reply from OpenAI API with error handling
    try:
        with st.spinner("🤔 Thinking..."):
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=api_messages,
                temperature=temperature,
                max_tokens=max_tokens
            )
        
        reply = response.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": reply})
        
        # Show success message if new facts were learned
        if new_facts:
            fact_summary = ", ".join([f"{k}: {v if not isinstance(v, list) else ', '.join(v)}" for k, v in new_facts.items()])
            st.success(f"📝 Learned: {fact_summary}")
        
        st.rerun()
        
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")
        st.info("Please check your OpenAI API key and try again.")

# Display the conversation history with better formatting
st.markdown("---")
st.markdown("### 💭 Our Conversation")

for i, msg in enumerate(st.session_state.messages[1:], 1):
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.markdown(msg["content"])
    else:
        with st.chat_message("assistant"):
            st.markdown(msg["content"])

# Enhanced export options
if len(st.session_state.messages) > 1:
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # Download chat as text
        full_chat = f"Chatbot Conversation - {st.session_state.conversation_started}\n"
        full_chat += "=" * 50 + "\n\n"
        for msg in st.session_state.messages[1:]:
            role = "You" if msg["role"] == "user" else "Bot"
            full_chat += f"{role}: {msg['content']}\n\n"
        
        st.download_button(
            "⬇️ Download Chat",
            full_chat,
            file_name=f"chat_history_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        )
    
    with col2:
        # Download as JSON
        chat_data = {
            "conversation_started": st.session_state.conversation_started,
            "messages": st.session_state.messages[1:],
            "memory": st.session_state.memory
        }
        
        st.download_button(
            "📊 Download JSON",
            json.dumps(chat_data, indent=2),
            file_name=f"chat_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
            mime="application/json"
        )
    
    with col3:
        # Clear everything
        if st.button("🗑️ Clear All", type="secondary"):
            st.session_state.messages = [st.session_state.messages[0]]
            st.session_state.memory = {}
            st.session_state.conversation_started = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            st.success("Everything cleared!")
            st.rerun()

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: gray; font-size: 0.8em;'>
    🧠 Enhanced Chatbot with Memory | Built with Streamlit & OpenAI
    </div>
    """,
    unsafe_allow_html=True
)
