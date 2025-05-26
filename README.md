# 🤖 Claude & ChatGPT to Gemini Converter

Convert your Claude and ChatGPT conversation exports to **NotebookLM (Gemini)** compatible format for powerful analysis and insights.

## 🎯 What This Does

Transform your AI conversation history into organized, searchable knowledge bases that you can analyze with NotebookLM's AI-powered insights.

### ✨ Key Features

- 🔍 **Auto-Detection**: Automatically identifies Claude vs ChatGPT data formats
- 🏷️ **Smart Categorization**: AI conversations sorted by topics (Programming, Data Analysis, AI Tech, etc.)
- 📊 **NotebookLM Optimization**: Files split to respect 500K word limits
- 🚀 **One-Click Processing**: Simple batch file execution
- 🔧 **Error Recovery**: Comprehensive error handling and diagnostics
- 🌏 **Korean/English Support**: Bilingual keyword-based categorization
- 📋 **Detailed Reports**: Processing statistics and file guides

## 🚀 Quick Start

### 1. Export Your Data
**Claude**: Settings → Data Export → Download conversations
**ChatGPT**: Settings → Data Controls → Export data

### 2. Run the Tool
1. Place `conversations.json` in the `input/` folder
2. Double-click `process_conversations_v2.bat`
3. Wait for processing to complete

### 3. Upload to NotebookLM
1. Go to [NotebookLM](https://notebooklm.google.com)
2. Create a new notebook
3. Upload the generated `notebooklm_part_*.txt` files
4. Start asking questions about your conversation history!

## 📊 What You Get

### Generated Files
- `notebooklm_part_01_Programming.txt` - Coding, development discussions
- `notebooklm_part_02_Data_Analysis.txt` - Data science, analysis projects  
- `notebooklm_part_03_AI_Tech.txt` - AI, machine learning topics
- `notebooklm_part_04_Problem_Solving.txt` - Troubleshooting, debugging
- `notebooklm_part_05_General.txt` - General conversations
- `notebooklm_part_06_Daily_Mixed.txt` - Personal chats, misc topics

### Analysis Reports
- `processing_report.txt` - Processing statistics
- `conversations_index.txt` - Complete conversation list
- `notebooklm_index.txt` - Usage guide for generated files

## 💡 Example NotebookLM Questions

Once uploaded, you can ask NotebookLM:
- *"What programming challenges did I face most often?"*
- *"How did my AI usage patterns evolve over time?"*
- *"What are the main topics I discussed with AI assistants?"*
- *"What problem-solving approaches do I use?"*
- *"Show me conversations about data analysis projects"*

## 🛠️ Technical Details

### Supported Formats
- ✅ Claude `conversations.json` (web export)
- ✅ ChatGPT `conversations.json` (web export)

### System Requirements
- Windows 10/11
- Python 3.7+
- 1GB+ free space

### Processing Capabilities
- **Claude Data**: ~1,000 conversations/minute
- **ChatGPT Data**: ~500 conversations/minute  
- **File Size**: Up to 500MB input files
- **Output**: Optimized for NotebookLM's 500K word limit

## 📁 Project Structure

```
Claude-ChatGPT-to-Gemini/
├── 🚀 process_conversations_v2.bat    # Main execution script
├── 📄 README.md                       # This file
├── 📄 QUICKSTART.md                   # Quick start guide
├── 📄 INSTRUCTIONS.md                 # Detailed instructions
├── 📄 NEW_USER_GUIDE.md               # Complete user guide
├── 📄 TROUBLESHOOTING.md              # Error solutions
├── 📁 modules/                        # Processing modules
├── 📁 input/                          # Place your JSON files here
├── 📁 output/                         # Generated files appear here
└── 📁 temp/                           # Logs and temporary files
```

## 🔧 Advanced Usage

### Environment Testing
```bash
cd modules
python test_environment.py
```

### Error Diagnosis
```bash
cd modules
python error_recovery.py
```

### Manual Processing
```bash
cd modules
python main_processor_fixed.py ../input/conversations.json
```

## ⚠️ Troubleshooting

### Common Issues
- **"Python not found"** → Install Python 3.7+ with "Add to PATH"
- **"conversations.json not found"** → Check file is in `input/` folder
- **"Permission denied"** → Run as administrator
- **Memory errors** → Close other programs, restart computer

### Getting Help
1. Check `TROUBLESHOOTING.md` for detailed solutions
2. Run `error_recovery.py` for automatic diagnosis
3. Review log files in `temp/` folder
4. Ensure file formats match supported exports

## 🎉 Success Stories

Transform your conversations into insights:
- **Research**: Analyze your learning patterns and knowledge gaps
- **Productivity**: Identify common problems and solutions
- **Documentation**: Create searchable knowledge bases from conversations
- **Reflection**: Understand how your thinking has evolved

## 📈 Roadmap

- [ ] Support for other AI platforms (Perplexity, Bing Chat)
- [ ] Conversation merging and deduplication
- [ ] Visual analytics dashboard
- [ ] Automated backup and versioning
- [ ] Export to other formats (Obsidian, Notion)

## 🤝 Contributing

Contributions welcome! The modular design makes it easy to:
- Add support for new AI platforms
- Improve categorization algorithms
- Enhance error handling
- Add new output formats

## 📄 License

MIT License - feel free to use, modify, and distribute!

---

**🎯 Turn your AI conversations into valuable insights with NotebookLM!**

*Made for the AI-native generation who want to understand their digital interactions*