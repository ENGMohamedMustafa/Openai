# 🗣️ Audio Transcription & Translation

A professional-grade Streamlit application that transcribes audio files using OpenAI's Whisper API and translates the text into multiple languages using GPT models. Perfect for content creators, researchers, journalists, and anyone working with multilingual audio content.

![Audio Transcription](https://img.shields.io/badge/Audio-Transcription-blue?style=for-the-badge&logo=openai)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)

## ✨ Features

### 🎤 Audio Transcription
- **Whisper Integration**: Powered by OpenAI's state-of-the-art Whisper model
- **Multiple Formats**: Support for MP3, WAV, M4A, FLAC, OGG, WebM
- **High Accuracy**: Industry-leading speech recognition technology
- **Real-time Processing**: Fast transcription with progress indicators
- **File Validation**: Automatic size and format checking

### 🌍 Multi-language Translation
- **16+ Languages**: Arabic, Chinese, French, German, Spanish, Japanese, and more
- **Multiple Models**: Choose between GPT-4o-mini, GPT-3.5-turbo, or GPT-4
- **Context-Aware**: Professional translation maintaining tone and meaning
- **Cost Optimization**: Smart model selection for budget control

### 📊 Advanced Management
- **Session Statistics**: Track transcriptions and translations
- **Timestamped Files**: Organized downloads with automatic naming
- **Audio Preview**: Built-in player for uploaded files
- **Usage Monitoring**: Real-time session metrics
- **Error Handling**: Comprehensive error messages and troubleshooting

### 🎨 User Experience
- **Modern Interface**: Clean, responsive design with custom styling
- **Sidebar Controls**: Organized settings and configuration options
- **Progress Indicators**: Visual feedback during processing
- **Expandable Sections**: Tips, usage info, and cost guidance
- **Mobile Friendly**: Works on desktop and mobile devices

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- OpenAI API key with Whisper and GPT access
- Internet connection for API calls

### Installation

1. **Clone or download the application**
   ```bash
   git clone <repository-url>
   cd audio-transcribe-translate
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

4. **Run the application**
   ```bash
   streamlit run audio_transcribe_translate.py
   ```

5. **Open in browser**
   Navigate to `http://localhost:8501`

## 📋 Requirements

```txt
streamlit>=1.28.0
openai>=1.0.0
python-dotenv>=1.0.0
```

## 🎯 Usage Guide

### Basic Workflow
1. **Upload Audio**: Select an audio file (up to 25MB)
2. **Preview**: Listen to your audio in the built-in player
3. **Transcribe**: Click "Start Transcription" to convert speech to text
4. **Translate** (Optional): Choose a language and translate the text
5. **Download**: Save both transcription and translation files

### Supported Audio Formats
| Format | Extension | Quality | Notes |
|--------|-----------|---------|-------|
| MP3 | .mp3 | Good | Most common format |
| WAV | .wav | Excellent | Uncompressed, larger files |
| M4A | .m4a | Very Good | Apple's audio format |
| FLAC | .flac | Excellent | Lossless compression |
| OGG | .ogg | Good | Open source format |
| WebM | .webm | Good | Web-optimized format |

### Supported Languages
- **European**: English, French, German, Spanish, Italian, Dutch, Portuguese, Polish, Swedish, Russian
- **Asian**: Chinese (Simplified/Traditional), Japanese, Korean, Hindi
- **Middle Eastern**: Arabic, Turkish

### Model Selection Guide

#### Transcription Models
- **Whisper-1**: OpenAI's production Whisper model (only option currently)

#### Translation Models
| Model | Speed | Cost | Quality | Best For |
|-------|-------|------|---------|----------|
| GPT-4o-mini | Fast | Low | Good | General translations, casual content |
| GPT-3.5-turbo | Medium | Medium | Very Good | Professional content, longer texts |
| GPT-4 | Slower | High | Excellent | Critical translations, technical content |

## ⚙️ Configuration Options

### Sidebar Settings
- **Translation Language**: Choose from 16+ supported languages
- **Transcription Model**: Select Whisper model (currently Whisper-1)
- **Translation Model**: Choose between GPT models based on needs
- **Auto-download**: Automatically save files (optional)

### Advanced Features
- **Session Statistics**: Monitor usage in real-time
- **File Information**: Display file size and format details
- **Progress Tracking**: Visual indicators for all operations
- **Error Recovery**: Detailed error messages with solutions

## 💰 Cost Management

### OpenAI Pricing (as of 2024)
| Service | Cost | Notes |
|---------|------|-------|
| **Whisper Transcription** | $0.006/minute | Based on audio length |
| **GPT-4o-mini** | ~$0.00015/1K tokens | Most cost-effective |
| **GPT-3.5-turbo** | ~$0.0015/1K tokens | Balanced option |
| **GPT-4** | ~$0.03/1K tokens | Premium quality |

### Cost Optimization Tips
- Start with GPT-4o-mini for testing and general use
- Use GPT-4 only for critical or complex translations
- Keep audio files under 25MB (Whisper limit)
- Batch similar content together
- Monitor usage in the sidebar statistics

## 🔧 Customization

### Adding New Languages
```python
# In the language selectbox
language = st.selectbox(
    "🌍 Translate to:",
    [
        # Add your new language here
        "Your_New_Language"
    ]
)
```

### Custom Styling
The app includes custom CSS that you can modify:
```python
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #1f77b4;  # Change header color
    }
    # Add your custom styles here
</style>
""", unsafe_allow_html=True)
```

### Model Configuration
```python
# Add new models to the selectbox
translation_model = st.selectbox(
    "Translation Model:",
    ["gpt-4o-mini", "gpt-3.5-turbo", "gpt-4", "your-custom-model"]
)
```

## 🐛 Troubleshooting

### Common Issues

**"OpenAI API key not found"**
- Ensure `.env` file exists in project root
- Verify `OPENAI_API_KEY` is correctly set
- Check for typos in the API key
- Restart the application after adding the key

**"File size exceeds 25MB limit"**
- OpenAI Whisper has a 25MB file size limit
- Compress your audio file using tools like Audacity
- Convert to MP3 format for smaller file sizes
- Split longer recordings into segments

**"Transcription failed"**
- Check your OpenAI account has sufficient credits
- Verify internet connection is stable
- Ensure audio file is not corrupted
- Try a different audio format

**"Translation failed"**
- Verify the transcription completed successfully
- Check API rate limits in your OpenAI dashboard
- Try a different translation model
- Ensure the source text is not too long

**"App won't start"**
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Check Python version (3.8+ required)
- Try a different port: `streamlit run app.py --server.port 8502`
- Clear browser cache and cookies

### Audio Quality Tips
- Use clear, high-quality recordings for best results
- Minimize background noise and echo
- Speak clearly at moderate pace
- Use a good microphone when possible
- Convert to WAV format for maximum quality

### Debug Mode
Enable detailed logging:
```bash
streamlit run audio_transcribe_translate.py --logger.level debug
```

## 🔒 Security & Privacy

### API Key Security
- Never commit `.env` files to version control
- Use environment variables in production deployments
- Rotate API keys regularly for security
- Monitor API usage for unauthorized access
- Store keys securely in production environments

### Data Privacy
- Audio files are processed by OpenAI's APIs
- Transcriptions and translations are not stored by OpenAI after processing
- Local session data is cleared when browser is closed
- No personal data is collected by the application
- Audio files are temporarily stored only during processing

### Content Guidelines
- Follow OpenAI's usage policies for content
- Avoid processing sensitive or confidential audio
- Respect copyright and intellectual property rights
- Use generated transcriptions responsibly
- Review translations for accuracy in important contexts

## 🚀 Deployment Options

### Local Development
```bash
# Standard run
streamlit run audio_transcribe_translate.py

# Custom port
streamlit run audio_transcribe_translate.py --server.port 8502

# Debug mode
streamlit run audio_transcribe_translate.py --logger.level debug
```

### Streamlit Cloud
1. Push code to GitHub repository
2. Connect repository to Streamlit Cloud
3. Add `OPENAI_API_KEY` to Streamlit secrets
4. Deploy automatically from main branch

### Heroku Deployment
```bash
# Create Procfile
echo "web: streamlit run audio_transcribe_translate.py --server.port $PORT --server.headless true" > Procfile

# Deploy to Heroku
heroku create your-app-name
heroku config:set OPENAI_API_KEY=your_key_here
git push heroku main
```

### Docker Deployment
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8501

CMD ["streamlit", "run", "audio_transcribe_translate.py", "--server.headless", "true", "--server.port", "8501"]
```

### Environment Variables for Production
```bash
# Set in your deployment environment
OPENAI_API_KEY=your_production_api_key
STREAMLIT_SERVER_HEADLESS=true
STREAMLIT_SERVER_PORT=8501
```

## 📈 Performance Optimization

### Speed Improvements
- Use GPT-4o-mini for faster translations
- Implement caching for repeated content
- Optimize file handling and temporary storage
- Add progress bars for better user experience

### Scalability Considerations
- Monitor API rate limits and quotas
- Implement queue system for batch processing
- Add database support for persistent storage
- Consider load balancing for multiple users

### Memory Management
- Clean up temporary files automatically
- Limit concurrent processing sessions
- Implement file size restrictions
- Monitor server resource usage

## 🔮 Future Enhancements

### Planned Features
- [ ] **Batch Processing**: Upload multiple audio files
- [ ] **Speaker Diarization**: Identify different speakers
- [ ] **Custom Vocabularies**: Improve accuracy for specific domains
- [ ] **Real-time Transcription**: Live audio processing
- [ ] **Audio Editing**: Basic trimming and enhancement
- [ ] **Export Formats**: SRT, VTT subtitle formats
- [ ] **API Integration**: Support for other transcription services

### Advanced Features
- [ ] **Voice Cloning**: Generate speech from transcriptions
- [ ] **Sentiment Analysis**: Analyze emotional content
- [ ] **Keyword Extraction**: Automatic topic identification
- [ ] **Summary Generation**: AI-powered content summaries
- [ ] **Multi-speaker Support**: Better handling of conversations
- [ ] **Custom Training**: Fine-tuned models for specific use cases

## 🤝 Contributing

We welcome contributions! Here's how to get involved:

### Development Setup
1. Fork the repository on GitHub
2. Clone your fork: `git clone https://github.com/yourusername/audio-transcribe-translate.git`
3. Create a feature branch: `git checkout -b feature/amazing-feature`
4. Install development dependencies: `pip install -r requirements-dev.txt`
5. Make your changes and test thoroughly
6. Run code quality checks: `flake8` and `black`
7. Submit a pull request with detailed description

### Code Standards
- Follow PEP 8 style guidelines
- Use type hints where possible
- Add docstrings for all functions
- Write unit tests for new features
- Update documentation for changes

### Reporting Issues
- Use GitHub Issues for bug reports and feature requests
- Include system information and error logs
- Provide steps to reproduce issues
- Suggest potential solutions when possible
- Label issues appropriately (bug, enhancement, question)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for complete details.

## 🙏 Acknowledgments

- **OpenAI**: For providing Whisper and GPT APIs
- **Streamlit**: For the excellent web app framework
- **Python Community**: For amazing libraries and tools
- **Contributors**: Thank you to everyone who helps improve this project
- **Open Source Community**: For inspiration and best practices

## 📞 Support & Resources

### Getting Help
- 📖 Check this README for solutions to common issues
- 🐛 Open GitHub Issues for bugs and feature requests
- 💬 Use GitHub Discussions for questions and ideas
- 📧 Contact maintainers for urgent issues

### Useful Links
- [OpenAI Whisper Documentation](https://platform.openai.com/docs/guides/speech-to-text)
- [OpenAI GPT Documentation](https://platform.openai.com/docs/guides/text-generation)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Python Audio Processing](https://wiki.python.org/moin/Audio/)

### Community
- 🌟 Star the repository if you find it useful
- 🍴 Fork and contribute to make it better
- 📢 Share with others who might benefit
- 🗣️ Join discussions and provide feedback

---

**Transform Audio into Text in Any Language! 🗣️✨**

*Made with ❤️ for the global community*

![Footer Wave](https://capsule-render.vercel.app/api?type=waving&color=gradient&height=100&section=footer)
