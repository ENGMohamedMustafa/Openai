# 🧠 Enhanced Chatbot with Memory

A sophisticated Streamlit-based chatbot application that remembers information about users across conversations and provides intelligent, context-aware responses using OpenAI's GPT models.

## ✨ Features

### 🧠 Intelligent Memory System
- **Automatic Fact Extraction**: Learns about users from natural conversation
- **Multi-Pattern Recognition**: Detects names, interests, age, location, profession, and more
- **Memory Persistence**: Maintains context throughout the conversation
- **Memory Management**: Export, clear, or selectively manage stored information

### 💬 Enhanced Chat Experience
- **Real-time Conversation**: Smooth, responsive chat interface
- **Context-Aware Responses**: AI uses remembered facts for personalized replies
- **Visual Feedback**: Success notifications when new facts are learned
- **Message History**: Complete conversation tracking with timestamps

### 📊 Conversation Analytics
- **Real-time Stats**: Track messages exchanged and facts remembered
- **Session Information**: Monitor conversation start time and duration
- **Export Options**: Download conversations in multiple formats (TXT, JSON)

### ⚙️ Customizable Settings
- **Response Creativity**: Adjust AI temperature (0.0 - 1.0)
- **Response Length**: Control maximum token output (50 - 500)
- **Model Selection**: Compatible with various OpenAI models

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- OpenAI API key
- Required Python packages (see requirements.txt)

### Installation

1. **Clone or download the project files**
   ```bash
   git clone <repository-url>
   cd enhanced-chatbot
   ```

2. **Install required packages**
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
   streamlit run chatbot.py
   ```

5. **Open your browser**
   Navigate to `http://localhost:8501`

## 📋 Requirements

Create a `requirements.txt` file with:

```txt
streamlit>=1.28.0
openai>=0.28.0
python-dotenv>=1.0.0
```

## 🎯 Usage Guide

### Starting a Conversation
1. Launch the app and wait for it to load
2. Type your message in the input field
3. Press Enter or click outside the field to send

### Teaching the Bot About Yourself
The bot automatically learns from natural conversation. Try phrases like:
- "My name is John"
- "I'm interested in photography"
- "I live in New York"
- "I work as a software engineer"
- "I'm 25 years old"

### Memory Management
- **View Memory**: Expand the "Memory Bank" section to see what the bot remembers
- **Export Memory**: Save your memory data as JSON
- **Clear Memory**: Remove specific memories or clear all at once

### Conversation Controls
- **Adjust Settings**: Use the sidebar to modify response creativity and length
- **Export Chat**: Download your conversation as TXT or JSON
- **Clear All**: Reset the entire conversation and memory

## 🔧 Configuration

### Environment Variables
| Variable | Description | Required |
|----------|-------------|----------|
| `OPENAI_API_KEY` | Your OpenAI API key | Yes |

### Customizable Parameters
- **Temperature**: Controls response creativity (0.0 = focused, 1.0 = creative)
- **Max Tokens**: Limits response length (50-500 tokens)
- **Model**: OpenAI model to use (default: gpt-3.5-turbo)

## 🏗️ Architecture

### Core Components
```
├── chatbot.py              # Main application file
├── .env                    # Environment variables
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

### Memory System
The chatbot uses regex patterns to extract facts from user input:
- **Name Detection**: "My name is X", "I'm X", "Call me X"
- **Interest Extraction**: "I like X", "I'm interested in X"
- **Location Recognition**: "I live in X", "I'm from X"
- **Professional Info**: "I work as X", "My job is X"
- **Age Detection**: "I'm X years old", "I am X"

### Data Flow
1. User input → Fact extraction → Memory update
2. Memory context → AI prompt → Response generation
3. Response → Display → History storage

## 🎨 Customization

### Adding New Fact Types
To extract additional user information, modify the `extract_facts_from_text()` function:

```python
# Example: Extract favorite color
color_match = re.search(r"my favorite color is (\w+)", text_lower)
if color_match:
    facts["favorite_color"] = color_match.group(1)
```

### Styling
Customize the app appearance by modifying:
- `st.set_page_config()` for page settings
- CSS in `st.markdown()` for custom styling
- Streamlit theme settings

### Memory Storage
Currently uses session state. For persistence:
- Add file-based storage (JSON, SQLite)
- Implement cloud storage integration
- Add user authentication for multi-user scenarios

## 🔒 Security Considerations

- **API Key Protection**: Never commit `.env` files to version control
- **Input Validation**: Consider adding sanitization for user inputs
- **Rate Limiting**: Implement usage limits to control API costs
- **Data Privacy**: Memory data is session-based and not permanently stored

## 🐛 Troubleshooting

### Common Issues

**"OpenAI API Error"**
- Verify your API key is correct and active
- Check your OpenAI account has sufficient credits
- Ensure stable internet connection

**"Module Not Found"**
- Run `pip install -r requirements.txt`
- Ensure you're in the correct virtual environment

**"App Won't Load"**
- Check if port 8501 is available
- Try `streamlit run chatbot.py --server.port 8502`

### Debug Mode
Add debug information by enabling Streamlit's debug mode:
```bash
streamlit run chatbot.py --logger.level debug
```

## 🔮 Future Enhancements

### Planned Features
- [ ] **Voice Integration**: Speech-to-text and text-to-speech
- [ ] **Multi-Language Support**: Conversation in different languages
- [ ] **Advanced Memory**: Semantic search and relationship mapping
- [ ] **Export Options**: PDF, Word document formats
- [ ] **Conversation Templates**: Pre-built conversation starters
- [ ] **Analytics Dashboard**: Detailed conversation insights

### Technical Improvements
- [ ] **Database Integration**: PostgreSQL/MongoDB for scalable storage
- [ ] **User Authentication**: Multi-user support with profiles
- [ ] **API Abstraction**: Support for multiple AI providers
- [ ] **Mobile Optimization**: Responsive design improvements
- [ ] **Real-time Sync**: WebSocket-based real-time updates

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📞 Support

If you encounter any issues or have questions:
- Open an issue on GitHub
- Check the troubleshooting section above
- Review OpenAI's documentation for API-related questions

## 🎉 Acknowledgments

- Built with [Streamlit](https://streamlit.io/) for the web interface
- Powered by [OpenAI](https://openai.com/) for intelligent responses
- Inspired by the need for more personalized AI interactions

---

**Happy Chatting! 🚀**

*Made with ❤️ and lots of ☕*
