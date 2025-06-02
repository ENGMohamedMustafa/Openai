# 🤖 OpenAI Applications Suite

> **A modern, enterprise-grade AI-powered application built with OpenAI's cutting-edge models and Streamlit's interactive web framework.**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-green.svg)](https://openai.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Maintenance](https://img.shields.io/badge/Maintained-Yes-brightgreen.svg)](https://github.com/ENGMohamedMustafa/openai-applications)

## 🎯 Overview

A comprehensive AI application suite that combines multiple OpenAI services into a single, powerful Streamlit web application. This project demonstrates advanced integration of conversational AI, image generation, and speech-to-text capabilities in a user-friendly interface.

---

## ✨ Features

### 🧠 **Intelligent Chatbot**
- **Advanced Conversational AI** powered by GPT-4/GPT-3.5
- **Context-Aware Responses** with conversation memory
- **Customizable AI Personality** and behavior settings
- **Real-Time Streaming** responses for better UX
- **Conversation History** with export capabilities

### 🎨 **AI Image Generation**
- **DALL-E 3 Integration** for high-quality image creation
- **Multiple Resolution Support** (1024x1024, 1792x1024, 1024x1792)
- **Style and Quality Controls** for fine-tuned outputs
- **Batch Generation** capabilities
- **Image Gallery** with download functionality

### 🎙️ **Speech-to-Text Processing**
- **Whisper Model Integration** for accurate transcription
- **Multi-Format Audio Support** (MP3, WAV, M4A, FLAC, OGG)
- **Real-Time Processing** with progress indicators
- **Language Auto-Detection** 
- **Transcript Export** in multiple formats

---

## 🚀 Quick Start

### Prerequisites

```bash
Python 3.8 or higher
OpenAI API Key
Streamlit
```

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/ENGMohamedMustafa/openai-applications.git
   cd openai-applications
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Environment Setup**
   ```bash
   # Copy the example environment file
   cp .env.example .env
   
   # Edit .env file with your OpenAI API key
   nano .env
   ```

4. **Run the Application**
   ```bash
   streamlit run main.py
   ```

---

## 🔐 Configuration

### Environment Variables

Create a `.env` file based on `.env.example`:

```env
# OpenAI Configuration
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_ORG_ID=your_organization_id_optional

# Application Settings
APP_TITLE=OpenAI Applications Suite
APP_ICON=🤖
DEBUG_MODE=False

# Model Configuration
CHAT_MODEL=gpt-4-turbo-preview
IMAGE_MODEL=dall-e-3
AUDIO_MODEL=whisper-1

# Performance Settings
MAX_TOKENS=4096
TEMPERATURE=0.7
MAX_FILE_SIZE=25MB
```

### Streamlit Configuration

The application supports custom Streamlit configuration:

```toml
# .streamlit/config.toml
[theme]
primaryColor = "#FF6B6B"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
font = "sans serif"

[server]
maxUploadSize = 200
enableCORS = false
enableXsrfProtection = true
```

---

## 📁 Project Structure

```
openai-applications/
├── 📄 main.py                    # Main Streamlit application
├── 📋 requirements.txt           # Python dependencies
├── 🔒 .env.example              # Environment variables template
├── 🔒 .env                      # Your environment variables (not tracked)
├── 📝 .gitignore               # Git ignore rules
├── 📝 gitignore                # Additional ignore patterns
├── 📖 README.md                # Project documentation
├── 📁 .streamlit/              # Streamlit configuration (optional)
│   └── config.toml
```

---

## 🛠️ Technology Stack

### Core Technologies
- **Python 3.8+** - Programming language
- **Streamlit** - Web application framework
- **OpenAI API** - AI model integration

### AI Models
- **GPT-4/GPT-3.5 Turbo** - Conversational AI
- **DALL-E 3** - Image generation
- **Whisper** - Speech-to-text

### Key Libraries
```python
streamlit>=1.28.0
openai>=1.0.0
python-dotenv>=1.0.0
pillow>=10.0.0
requests>=2.31.0
pandas>=2.0.0
numpy>=1.24.0
```

---

## 🎮 Application Usage

### Launch Options

**Standard Launch:**
```bash
streamlit run main.py
```

**Custom Port:**
```bash
streamlit run main.py --server.port 8502
```

**Development Mode:**
```bash
streamlit run main.py --server.runOnSave true
```

### Application Navigation

The application typically includes:
1. **Main Dashboard** - Overview and navigation
2. **Chatbot Interface** - Conversational AI
3. **Image Generation Studio** - DALL-E integration
4. **Audio Transcription** - Speech-to-text processing
5. **Settings & Configuration** - User preferences

---

## 🔧 Advanced Configuration

### Custom Model Settings

```python
# In main.py or config file
MODEL_CONFIG = {
    "chat": {
        "model": "gpt-4-turbo-preview",
        "temperature": 0.7,
        "max_tokens": 4096,
        "stream": True
    },
    "image": {
        "model": "dall-e-3",
        "size": "1024x1024",
        "quality": "hd",
        "n": 1
    },
    "audio": {
        "model": "whisper-1",
        "response_format": "json",
        "temperature": 0
    }
}
```

### Performance Optimization

```python
# Caching configuration
@st.cache_data
def cached_api_call(prompt, model="gpt-3.5-turbo"):
    # Your API call implementation
    pass

@st.cache_resource
def load_model_config():
    # Load and cache model configuration
    pass
```

---

## 🚀 Deployment

### Local Development
```bash
# Install in development mode
pip install -e .

# Run with auto-reload
streamlit run main.py --server.runOnSave true
```





**Streamlit Cloud:**
1. Connect your GitHub repository
2. Set environment variables in Streamlit Cloud dashboard
3. Deploy automatically on push

**Heroku Deployment:**
```bash
# Create Procfile
echo "web: streamlit run main.py --server.port $PORT --server.address 0.0.0.0" > Procfile

# Deploy to Heroku
heroku create your-app-name
git push heroku main
```

---

## 🔒 Security Best Practices

### API Key Management
- ✅ Never commit API keys to version control
- ✅ Use environment variables for sensitive data
- ✅ Implement proper error handling for API failures
- ✅ Monitor API usage and set quotas

### Application Security
- 🔒 Input validation and sanitization
- 🔒 File upload restrictions
- 🔒 Rate limiting for API calls
- 🔒 Secure session management

---

## 🧪 Testing

### Running Tests
```bash
# Install test dependencies
pip install pytest pytest-streamlit

# Run tests
pytest tests/

# Run with coverage
pytest --cov=. tests/
```

### Test Structure
```
tests/
├── test_main.py              # Main application tests
├── test_api_integration.py   # OpenAI API tests
├── test_components.py        # Component tests
└── conftest.py              # Test configuration
```

---

## 📊 Performance Monitoring

### Metrics to Track
- **API Response Times** - Monitor OpenAI API latency
- **Application Load Times** - Streamlit performance
- **Error Rates** - Track and log errors
- **User Interactions** - Usage analytics

### Monitoring Tools
```python
# Example monitoring integration
import streamlit as st
from datetime import datetime

# Track API calls
def track_api_call(model, tokens_used, response_time):
    st.session_state.setdefault('api_metrics', []).append({
        'timestamp': datetime.now(),
        'model': model,
        'tokens': tokens_used,
        'response_time': response_time
    })
```

---

## 🤝 Contributing

We welcome contributions! Please see our contributing guidelines:

### Development Setup
```bash
# Fork the repository
git fork https://github.com/ENGMohamedMustafa/openai-applications

# Create development branch
git checkout -b feature/new-feature

# Install development dependencies
pip install -r requirements-dev.txt

# Make changes and test
pytest tests/

# Commit and push
git commit -m "feat: add new feature"
git push origin feature/new-feature
```

### Code Standards
- Follow PEP 8 style guidelines
- Write comprehensive docstrings
- Include unit tests for new features
- Update documentation as needed

---

## 📚 Documentation

### Additional Resources
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Streamlit Documentation](https://docs.streamlit.io)
- [Python Best Practices](https://docs.python-guide.org)

### API Reference
```python
# Main application structure
def main():
    """Main application entry point"""
    
def setup_sidebar():
    """Configure application sidebar"""
    
def render_chatbot():
    """Render chatbot interface"""
    
def render_image_generator():
    """Render image generation interface"""
    
def render_speech_to_text():
    """Render speech-to-text interface"""
```

---

## 🆘 Troubleshooting

### Common Issues

**API Key Errors:**
```bash
# Check if API key is set
echo $OPENAI_API_KEY

# Verify API key format
python -c "import openai; print('API key valid' if openai.api_key else 'No API key')"
```

**Streamlit Issues:**
```bash
# Clear Streamlit cache
streamlit cache clear

# Reset Streamlit configuration
rm -rf ~/.streamlit/
```



## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **OpenAI** for providing world-class AI models
- **Streamlit** for the amazing web application framework
- **The Python Community** for excellent libraries and tools
- **Contributors** who help improve this project

---

<div align="center">

**Built with ❤️ by Mohamed Mustafa**

*Last Updated: June 2025*

[⭐ Star this repository](https://github.com/ENGMohamedMustafa/openai-applications) | [🍴 Fork it](https://github.com/ENGMohamedMustafa/openai-applications/fork) | [📝 Report Issues](https://github.com/ENGMohamedMustafa/openai-applications/issues)

</div>
