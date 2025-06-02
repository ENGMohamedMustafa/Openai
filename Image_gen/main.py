# Enhanced AI Image Generator using OpenAI DALL-E API
import streamlit as st
import openai
import os
import requests
import base64
from datetime import datetime
from PIL import Image
import io
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Configure Streamlit page
st.set_page_config(
    page_title="AI Image Generator",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .stButton > button {
        width: 100%;
        border-radius: 20px;
        border: none;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-weight: bold;
    }
    .stTextInput > div > div > input {
        border-radius: 20px;
    }
    .image-container {
        border: 3px solid #667eea;
        border-radius: 15px;
        padding: 10px;
        background: #f8f9ff;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-header">
    <h1>🎨 AI Image Generator</h1>
    <p>Create stunning images with OpenAI's DALL-E</p>
</div>
""", unsafe_allow_html=True)

# Initialize session state
if 'generated_images' not in st.session_state:
    st.session_state.generated_images = []
if 'generation_history' not in st.session_state:
    st.session_state.generation_history = []

# Sidebar configuration
with st.sidebar:
    st.header("⚙️ Settings")
    
    # Image settings
    image_size = st.selectbox(
        "Image Size",
        options=["1024x1024", "1024x1792", "1792x1024"],
        index=0,
        help="Choose the dimensions for your generated image"
    )
    
    image_quality = st.selectbox(
        "Image Quality",
        options=["standard", "hd"],
        index=0,
        help="HD quality takes longer but produces better results"
    )
    
    num_images = st.slider(
        "Number of Images",
        min_value=1,
        max_value=4,
        value=1,
        help="Generate multiple variations (costs more)"
    )
    
    st.header("📊 Statistics")
    st.metric("Images Generated", len(st.session_state.generation_history))
    st.metric("Current Session", len(st.session_state.generated_images))
    
    # Clear history button
    if st.button("🗑️ Clear History"):
        st.session_state.generated_images = []
        st.session_state.generation_history = []
        st.success("History cleared!")
        st.rerun()

# Main content
col1, col2 = st.columns([2, 1])

with col1:
    st.header("✍️ Create Your Image")
    
    # Prompt input with examples
    prompt_examples = [
        "A futuristic cityscape at sunset with flying cars",
        "A cute robot reading a book in a cozy library",
        "An underwater palace with colorful coral gardens",
        "A magical forest with glowing mushrooms and fairy lights",
        "A steampunk workshop with intricate mechanical devices"
    ]
    
    selected_example = st.selectbox(
        "Or choose from examples:",
        options=[""] + prompt_examples,
        index=0
    )
    
    user_prompt = st.text_area(
        "Enter your image description:",
        value=selected_example,
        height=100,
        placeholder="Describe the image you want to generate in detail...",
        help="Be specific and descriptive for better results"
    )
    
    # Style suggestions
    with st.expander("💡 Style Suggestions"):
        style_options = [
            "photorealistic", "oil painting", "watercolor", "digital art", 
            "cartoon style", "anime style", "sketch", "3D render",
            "vintage photograph", "impressionist", "abstract", "minimalist"
        ]
        
        selected_styles = st.multiselect(
            "Add artistic styles to your prompt:",
            style_options
        )
        
        if selected_styles:
            style_text = ", ".join(selected_styles)
            suggested_prompt = f"{user_prompt}, in {style_text} style" if user_prompt else f"in {style_text} style"
            st.text_area("Suggested prompt with styles:", value=suggested_prompt, height=60)
            if st.button("Use Suggested Prompt"):
                user_prompt = suggested_prompt
                st.rerun()

with col2:
    st.header("🎛️ Quick Actions")
    
    # Generation button
    generate_button = st.button("🎨 Generate Image", type="primary")
    
    # Advanced options
    with st.expander("🔧 Advanced Options"):
        add_timestamp = st.checkbox("Add timestamp to filename", value=True)
        auto_download = st.checkbox("Auto-download images", value=False)
        show_prompt_in_caption = st.checkbox("Show prompt in caption", value=True)

# Image generation logic
if generate_button and user_prompt:
    if not openai.api_key:
        st.error("❌ OpenAI API key not found! Please set your OPENAI_API_KEY in the .env file.")
    else:
        try:
            with st.spinner(f"🎨 Generating {num_images} image(s)... This may take a moment."):
                # Generate images using DALL-E 3
                response = openai.images.generate(
                    model="dall-e-3",  # Using DALL-E 3 for better quality
                    prompt=user_prompt,
                    size=image_size,
                    quality=image_quality,
                    n=1  # DALL-E 3 only supports n=1
                )
                
                # Process generated images
                for i, image_data in enumerate(response.data):
                    image_url = image_data.url
                    revised_prompt = getattr(image_data, 'revised_prompt', user_prompt)
                    
                    # Download image
                    image_response = requests.get(image_url, timeout=30)
                    
                    if image_response.status_code == 200:
                        # Create image info
                        image_info = {
                            'url': image_url,
                            'prompt': user_prompt,
                            'revised_prompt': revised_prompt,
                            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                            'size': image_size,
                            'quality': image_quality,
                            'image_data': image_response.content
                        }
                        
                        # Store in session state
                        st.session_state.generated_images.append(image_info)
                        st.session_state.generation_history.append(image_info)
                        
                        # Auto-download if enabled
                        if auto_download:
                            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S") if add_timestamp else ""
                            filename = f"ai_generated_image_{timestamp}_{i+1}.png"
                            with open(filename, "wb") as f:
                                f.write(image_response.content)
                
                st.success(f"✅ Successfully generated {len(response.data)} image(s)!")
                st.rerun()
                
        except Exception as e:
            st.error(f"❌ Error generating image: {str(e)}")
            st.info("💡 Tips: Make sure your prompt is descriptive and try again. Check your API key and internet connection.")

elif generate_button and not user_prompt:
    st.warning("⚠️ Please enter a description for your image!")

# Display generated images
if st.session_state.generated_images:
    st.header("🖼️ Generated Images")
    
    # Display images in a grid
    for idx, img_info in enumerate(reversed(st.session_state.generated_images)):
        with st.container():
            col1, col2 = st.columns([3, 1])
            
            with col1:
                # Display image
                caption = f"Prompt: {img_info['prompt']}" if show_prompt_in_caption else f"Generated on {img_info['timestamp']}"
                
                st.markdown('<div class="image-container">', unsafe_allow_html=True)
                st.image(
                    img_info['image_data'], 
                    caption=caption,
                    use_column_width=True
                )
                st.markdown('</div>', unsafe_allow_html=True)
                
                # Show revised prompt if different
                if img_info['revised_prompt'] != img_info['prompt']:
                    with st.expander("🔄 AI Revised Prompt"):
                        st.write(img_info['revised_prompt'])
            
            with col2:
                st.write(f"**Size:** {img_info['size']}")
                st.write(f"**Quality:** {img_info['quality']}")
                st.write(f"**Created:** {img_info['timestamp']}")
                
                # Download button
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S") if add_timestamp else ""
                filename = f"ai_image_{timestamp}_{idx+1}.png"
                
                st.download_button(
                    label="⬇️ Download",
                    data=img_info['image_data'],
                    file_name=filename,
                    mime="image/png",
                    key=f"download_{idx}"
                )
                
                # Copy URL button
                if st.button("📋 Copy URL", key=f"copy_{idx}"):
                    st.code(img_info['url'])
                
            st.divider()

# Generation history
if st.session_state.generation_history:
    with st.expander(f"📈 Generation History ({len(st.session_state.generation_history)} images)"):
        history_df_data = []
        for img in st.session_state.generation_history:
            history_df_data.append({
                'Timestamp': img['timestamp'],
                'Prompt': img['prompt'][:50] + "..." if len(img['prompt']) > 50 else img['prompt'],
                'Size': img['size'],
                'Quality': img['quality']
            })
        
        if history_df_data:
            st.dataframe(history_df_data, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray; font-size: 0.8em;'>
    🎨 AI Image Generator | Powered by OpenAI DALL-E 3 | Built with Streamlit
    <br>
    💡 Tip: Be creative and specific with your prompts for the best results!
</div>
""", unsafe_allow_html=True)

# Instructions for first-time users
if not st.session_state.generated_images:
    st.info("""
    🚀 **Getting Started:**
    1. Enter a detailed description of the image you want to create
    2. Adjust settings in the sidebar (size, quality, etc.)
    3. Click "Generate Image" and wait for the magic!
    4. Download your creations and share them with the world
    
    💡 **Pro Tips:**
    - Be specific and descriptive in your prompts
    - Try different artistic styles for variety
    - Use the example prompts to get started
    - Experiment with different sizes and quality settings
    """)
