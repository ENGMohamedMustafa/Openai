# 🎨 AI Image Generator

A professional-grade Streamlit application that generates stunning images using OpenAI's DALL-E 3 API. Create, customize, and download AI-generated artwork with an intuitive web interface.

![AI Image Generator](https://img.shields.io/badge/AI-Image%20Generator-blue?style=for-the-badge&logo=openai)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

## ✨ Features

### 🎯 Core Functionality
- **DALL-E 3 Integration**: Uses OpenAI's most advanced image generation model
- **Real-time Generation**: Create images instantly from text descriptions
- **Multiple Formats**: Support for various image sizes and quality settings
- **Batch Processing**: Generate multiple variations of your concept
- **Smart Downloads**: Organized file naming with timestamps

### 🎨 Creative Tools
- **Style Suggestions**: Pre-built artistic styles (photorealistic, oil painting, anime, etc.)
- **Prompt Examples**: Quick-start templates for inspiration
- **Style Mixer**: Combine multiple artistic styles automatically
- **Prompt Enhancement**: AI-revised prompts for better results
- **Creative Guidance**: Built-in tips and best practices

### 📊 Advanced Management
- **Generation History**: Track all your created images
- **Session Statistics**: Monitor usage and creation counts
- **Image Metadata**: Size, quality, timestamp information
- **Bulk Export**: Download all images at once
- **URL Sharing**: Easy image sharing capabilities

### 🎛️ Customization Options
- **Image Sizes**: 1024x1024, 1024x1792, 1792x1024
- **Quality Settings**: Standard and HD options
- **Auto-download**: Automatic file saving
- **Custom Naming**: Timestamped or custom filenames
- **Display Preferences**: Customizable image captions

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- OpenAI API key with DALL-E access
- Internet connection for API calls

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd ai-image-generator
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
   streamlit run image_generator.py
   ```

5. **Open in browser**
   Navigate to `http://localhost:8501`

## 📋 Requirements

```txt
streamlit>=1.28.0
openai>=1.0.0
python-dotenv>=1.0.0
requests>=2.31.0
Pillow>=10.0.0
```

## 🎯 Usage Guide

### Basic Image Generation
1. **Enter a Prompt**: Describe the image you want to create
2. **Choose Settings**: Select size, quality, and number of images
3. **Generate**: Click the "Generate Image" button
4. **Download**: Save your creations locally

### Advanced Techniques

#### Writing Effective Prompts
```
✅ Good: "A majestic dragon perched on a crystal mountain peak at sunset, with golden scales reflecting the warm light, detailed fantasy art style"

❌ Poor: "dragon"
```

#### Using Style Suggestions
- Select from pre-built styles: photorealistic, oil painting, watercolor, etc.
- Combine multiple styles for unique effects
- Use the "Suggested Prompt" feature for automatic style integration

#### Batch Generation
- Increase "Number of Images" for multiple variations
- Use different prompts with similar themes
- Experiment with various quality settings

## ⚙️ Configuration

### Environment Variables
| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `OPENAI_API_KEY` | Your OpenAI API key | Yes | - |

### Settings Options
| Setting | Options | Description |
|---------|---------|-------------|
| Image Size | 1024x1024, 1024x1792, 1792x1024 | Output image dimensions |
| Quality | standard, hd | Image quality level |
| Auto-download | True/False | Automatically save images |
| Timestamps | True/False | Add timestamps to filenames |

## 🏗️ Project Structure

```
ai-image-generator/
├── image_generator.py      # Main application file
├── requirements.txt        # Python dependencies
├── .env                   # Environment variables (create this)
├── README.md              # This documentation
└── generated_images/      # Default download directory (auto-created)
```

## 🎨 Example Prompts

### Photorealistic Images
- "A professional headshot of a confident businesswoman in a modern office"
- "A cozy coffee shop interior with warm lighting and vintage furniture"
- "A stunning landscape of northern lights over a snowy mountain range"

### Artistic Styles
- "A portrait of a wise old wizard, oil painting style with rich colors"
- "A cute cartoon cat wearing a detective hat, Disney animation style"
- "An abstract representation of music, with flowing colors and geometric shapes"

### Fantasy & Sci-Fi
- "A futuristic city floating among the clouds with flying vehicles"
- "A magical forest with glowing mushrooms and fairy lights at twilight"
- "A steampunk workshop filled with intricate mechanical inventions"

## 📊 Cost Management

### DALL-E 3 Pricing (as of 2024)
- **Standard Quality**: ~$0.040 per image
- **HD Quality**: ~$0.080 per image
- **1024x1792 or 1792x1024**: ~$0.120 per image (HD)

### Cost Optimization Tips
- Start with standard quality for testing
- Use HD only for final versions
- Batch similar requests together
- Monitor usage in the sidebar statistics

## 🔧 Customization

### Adding New Image Sizes
```python
# In the sidebar section
image_size = st.selectbox(
    "Image Size",
    options=["1024x1024", "1024x1792", "1792x1024", "512x512"],  # Add new size
    index=0
)
```

### Custom Style Presets
```python
# Add to style_options list
style_options = [
    "photorealistic", "oil painting", "watercolor", "digital art",
    "your_custom_style"  # Add your style here
]
```

### Theming
Modify the CSS in the `st.markdown()` section to customize:
- Colors and gradients
- Button styles
- Layout spacing
- Font choices

## 🐛 Troubleshooting

### Common Issues

**"OpenAI API key not found"**
- Ensure `.env` file exists in project root
- Verify `OPENAI_API_KEY` is correctly set
- Check for typos in the API key

**"Image generation failed"**
- Check your OpenAI account has sufficient credits
- Verify internet connection
- Try a simpler prompt
- Check if prompt violates OpenAI's usage policies

**"App won't start"**
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Check Python version (3.8+ required)
- Try a different port: `streamlit run image_generator.py --server.port 8502`

**"Images not downloading"**
- Check file permissions in the directory
- Ensure sufficient storage space
- Try disabling antivirus temporarily

### Debug Mode
Enable detailed logging:
```bash
streamlit run image_generator.py --logger.level debug
```

### API Limits
- DALL-E 3 supports only 1 image per request
- Rate limits apply based on your OpenAI plan
- Monitor usage in OpenAI dashboard

## 🔒 Security & Privacy

### API Key Security
- Never commit `.env` files to version control
- Use environment variables in production
- Rotate API keys regularly
- Monitor API usage for unauthorized access

### Content Policy
- Follow OpenAI's usage policies
- Avoid generating harmful or inappropriate content
- Respect copyright and intellectual property
- Use generated images responsibly

### Data Privacy
- Images are not stored on OpenAI servers after generation
- Local storage only (session-based)
- No personal data collection
- Clear browser data to remove session history

## 🚀 Deployment

### Local Development
```bash
streamlit run image_generator.py
```

### Streamlit Cloud
1. Push code to GitHub repository
2. Connect to Streamlit Cloud
3. Add `OPENAI_API_KEY` to secrets
4. Deploy automatically

### Heroku Deployment
```bash
# Create Procfile
echo "web: streamlit run image_generator.py --server.port $PORT --server.headless true" > Procfile

# Deploy
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

CMD ["streamlit", "run", "image_generator.py", "--server.headless", "true"]
```

## 🔮 Future Enhancements

### Planned Features
- [ ] **Image Editing**: Basic editing tools (crop, resize, filters)
- [ ] **Batch Processing**: Generate multiple images from CSV prompts
- [ ] **Image History**: Persistent storage with database
- [ ] **User Accounts**: Personal galleries and preferences
- [ ] **Social Features**: Share and rate generated images
- [ ] **API Integration**: Support for other AI image generators
- [ ] **Mobile App**: React Native or Flutter version

### Advanced Features
- [ ] **Prompt Engineering**: AI-assisted prompt optimization
- [ ] **Style Transfer**: Apply styles from uploaded images
- [ ] **Image Variations**: Generate variations of existing images
- [ ] **Collaborative Mode**: Team image generation workspace
- [ ] **Analytics Dashboard**: Detailed usage statistics
- [ ] **Custom Models**: Fine-tuned model integration

## 📈 Performance Optimization

### Speed Improvements
- Implement caching for repeated prompts
- Add progress bars for long generations
- Optimize image loading and display
- Use WebP format for smaller file sizes

### Scalability
- Add database support for large-scale usage
- Implement queue system for batch processing
- Add Redis caching for session data
- Load balancing for multiple users

## 🤝 Contributing

We welcome contributions! Please follow these guidelines:

### Development Setup
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Install dev dependencies: `pip install -r requirements-dev.txt`
4. Make your changes
5. Run tests: `pytest`
6. Submit a pull request

### Code Style
- Follow PEP 8 guidelines
- Use type hints where possible
- Add docstrings for functions
- Write unit tests for new features

### Reporting Issues
- Use GitHub Issues for bug reports
- Include system information and error logs
- Provide steps to reproduce the issue
- Suggest potential solutions if possible

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **OpenAI**: For providing the DALL-E 3 API
- **Streamlit**: For the amazing web app framework
- **Python Community**: For the excellent libraries and tools
- **Contributors**: Thank you to all who help improve this project

## 📞 Support

### Get Help
- 📖 Check this README for common solutions
- 🐛 Open an issue on GitHub for bugs
- 💡 Use GitHub Discussions for questions
- 📧 Contact maintainers for urgent issues

### Resources
- [OpenAI DALL-E Documentation](https://platform.openai.com/docs/guides/images)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Python.org](https://www.python.org/)

---

**Create Amazing AI Art Today! 🎨✨**

*Made with ❤️ by the AI Art Community*

![Footer](https://capsule-render.vercel.app/api?type=waving&color=gradient&height=100&section=footer)
