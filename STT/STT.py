import streamlit as st
import openai
import os
from dotenv import load_dotenv
import tempfile
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client with the new API
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Configure the Streamlit app
st.set_page_config(
    page_title="🗣️ Audio Transcribe & Translate", 
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #1f77b4;
        margin-bottom: 2rem;
    }
    .success-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        margin: 1rem 0;
    }
    .info-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #e7f3ff;
        border: 1px solid #b8daff;
        margin: 1rem 0;
    }
    .stDownloadButton button {
        background-color: #28a745;
        color: white;
        border: none;
        border-radius: 0.5rem;
        padding: 0.5rem 1rem;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Main title and description
st.markdown('<h1 class="main-header">🗣️🎯 Audio Transcription & Translation</h1>', unsafe_allow_html=True)
st.markdown("""
<div class="info-box">
Upload an audio file to get its transcription in English and translate it into your preferred language using OpenAI's Whisper and GPT models.
</div>
""", unsafe_allow_html=True)

# Sidebar for settings and information
with st.sidebar:
    st.header("⚙️ Settings")
    
    # Language selection with more options
    language = st.selectbox(
        "🌍 Translate to:",
        [
            "None (Keep English)",
            "Arabic", "French", "Spanish", "German", "Chinese (Simplified)",
            "Chinese (Traditional)", "Japanese", "Korean", "Portuguese", "Italian",
            "Russian", "Dutch", "Hindi", "Turkish", "Polish", "Swedish"
        ]
    )
    
    # Advanced options
    st.header("🔧 Advanced Options")
    
    # Transcription model selection
    transcription_model = st.selectbox(
        "Transcription Model:",
        ["whisper-1"],
        help="Currently only Whisper-1 is available"
    )
    
    # Translation model selection
    translation_model = st.selectbox(
        "Translation Model:",
        ["gpt-4o-mini", "gpt-3.5-turbo", "gpt-4"],
        index=0,
        help="Choose the model for translation. GPT-4o-mini is faster and more cost-effective."
    )
    
    # Auto-download options
    auto_download = st.checkbox("Auto-download files", value=False)
    
    st.header("📊 Session Info")
    if 'transcription_count' not in st.session_state:
        st.session_state.transcription_count = 0
    if 'translation_count' not in st.session_state:
        st.session_state.translation_count = 0
    
    st.metric("Transcriptions", st.session_state.transcription_count)
    st.metric("Translations", st.session_state.translation_count)

# Check if API key is available
if not os.getenv("OPENAI_API_KEY"):
    st.error("⚠️ OpenAI API key not found! Please add your API key to the .env file.")
    st.info("Create a .env file with: `OPENAI_API_KEY=your_api_key_here`")
    st.stop()

# File uploader for audio files
st.subheader("📤 Upload Your Audio File")
audio_file = st.file_uploader(
    "Choose an audio file", 
    type=["mp3", "wav", "m4a", "flac", "ogg", "webm"],
    help="Supported formats: MP3, WAV, M4A, FLAC, OGG, WebM"
)

# Display supported file info
with st.expander("ℹ️ Supported File Information"):
    st.markdown("""
    **Supported Formats:** MP3, WAV, M4A, FLAC, OGG, WebM
    
    **File Size Limit:** 25 MB (OpenAI Whisper limit)
    
    **Best Practices:**
    - Clear audio quality improves transcription accuracy
    - Reduce background noise when possible
    - Speak clearly and at moderate pace
    - Single speaker audio works best
    """)

if audio_file:
    # Check file size (25MB limit for Whisper)
    file_size = len(audio_file.getvalue())
    if file_size > 25 * 1024 * 1024:  # 25MB in bytes
        st.error("⚠️ File size exceeds 25MB limit. Please upload a smaller file.")
        st.stop()
    
    # Display file information
    col1, col2 = st.columns(2)
    with col1:
        st.info(f"**File:** {audio_file.name}")
    with col2:
        st.info(f"**Size:** {file_size / (1024*1024):.2f} MB")
    
    # Display audio player
    st.subheader("🎵 Audio Preview")
    st.audio(audio_file, format=f"audio/{audio_file.type.split('/')[-1]}")
    
    # Transcription section
    if st.button("🎤 Start Transcription", type="primary"):
        try:
            # Create a temporary file to save the uploaded audio
            with tempfile.NamedTemporaryFile(delete=False, suffix=f".{audio_file.name.split('.')[-1]}") as tmp_file:
                tmp_file.write(audio_file.getvalue())
                tmp_file_path = tmp_file.name
            
            # Transcribe the uploaded audio file using OpenAI Whisper
            with st.spinner("🔄 Transcribing audio... This may take a moment."):
                with open(tmp_file_path, "rb") as audio_data:
                    response = client.audio.transcriptions.create(
                        model=transcription_model,
                        file=audio_data,
                        response_format="text"
                    )
                
                # Clean up temporary file
                os.unlink(tmp_file_path)
                
                st.session_state.transcription_count += 1
                
                st.markdown('<div class="success-box">✅ Transcription completed successfully!</div>', unsafe_allow_html=True)
                
                # Display transcription
                st.subheader("📜 Transcribed Text")
                st.text_area("Transcription:", value=response, height=150, key="transcription_text")
                
                # Generate filename with timestamp
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                transcription_filename = f"transcription_{timestamp}.txt"
                
                # Download button for transcription
                st.download_button(
                    "⬇️ Download Transcription",
                    response,
                    file_name=transcription_filename,
                    mime="text/plain"
                )
                
                # Store transcription in session state for translation
                st.session_state.current_transcription = response
        
        except Exception as e:
            st.error(f"❌ Transcription failed: {str(e)}")
            st.error("Please check your API key and try again.")
    
    # Translation section
    if hasattr(st.session_state, 'current_transcription') and language != "None (Keep English)":
        st.subheader("🌐 Translation")
        
        if st.button("🌍 Translate Text", type="secondary"):
            try:
                with st.spinner(f"🔄 Translating to {language}..."):
                    translation_response = client.chat.completions.create(
                        model=translation_model,
                        messages=[
                            {
                                "role": "system", 
                                "content": f"You are a professional translator. Translate the given text accurately to {language}. Maintain the original meaning, tone, and context. If the text is already in {language}, indicate that no translation is needed."
                            },
                            {
                                "role": "user", 
                                "content": f"Translate this text to {language}:\n\n{st.session_state.current_transcription}"
                            }
                        ],
                        temperature=0.3
                    )
                    
                    translated_text = translation_response.choices[0].message.content
                    st.session_state.translation_count += 1
                    
                    st.markdown('<div class="success-box">✅ Translation completed successfully!</div>', unsafe_allow_html=True)
                    
                    # Display translation
                    st.text_area("Translation:", value=translated_text, height=150, key="translation_text")
                    
                    # Generate filename with timestamp
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    translation_filename = f"translation_{language}_{timestamp}.txt"
                    
                    # Download button for translation
                    st.download_button(
                        "⬇️ Download Translation",
                        translated_text,
                        file_name=translation_filename,
                        mime="text/plain"
                    )
                    
            except Exception as e:
                st.error(f"❌ Translation failed: {str(e)}")
                st.error("Please check your API key and try again.")

# Footer information
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; margin-top: 2rem;">
    <p>Powered by OpenAI Whisper & GPT • Built with Streamlit</p>
    <p><small>⚡ Fast • 🔒 Secure • 🌍 Multi-language</small></p>
</div>
""", unsafe_allow_html=True)

# Usage tips in expandable section
with st.expander("💡 Tips for Better Results"):
    st.markdown("""
    **For Better Transcription:**
    - Use clear, high-quality audio recordings
    - Minimize background noise
    - Speak at a moderate pace
    - Ensure good microphone positioning
    
    **For Better Translation:**
    - Review transcription accuracy first
    - Consider context and cultural nuances
    - Use GPT-4 for complex or technical content
    - Verify important translations manually
    
    **Cost Optimization:**
    - Use GPT-4o-mini for general translations (faster & cheaper)
    - Use GPT-4 only for complex or critical content
    - Keep audio files under 25MB
    """)

# API usage information
with st.expander("📊 API Usage Information"):
    st.markdown("""
    **Whisper Transcription:**
    - Cost: $0.006 per minute of audio
    - File size limit: 25 MB
    - Supported formats: MP3, MP4, MPEG, MPGA, M4A, WAV, WEBM
    
    **GPT Translation:**
    - GPT-4o-mini: ~$0.00015 per 1K tokens (cheaper)
    - GPT-3.5-turbo: ~$0.0015 per 1K tokens
    - GPT-4: ~$0.03 per 1K tokens (more accurate)
    """)
