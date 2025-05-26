# 📖 Detailed Usage Guide

## 🎯 Purpose
This document provides detailed instructions for using the AI conversation data migration tool.

## 📥 Step 1: Export Data

### Exporting from Claude
1. **Visit Claude website**: https://claude.ai
2. **Settings menu**: Top-right profile → Settings
3. **Data management**: "Data & Privacy" or "Data Export" menu
4. **Execute export**: Click "Download conversations" or "Export data"
5. **Download file**: Download the `conversations.json` file
6. **Verify file**: 
   - Ensure file size is not 0KB
   - Verify JSON format (open with text editor, should start with `[{`)

### Exporting from ChatGPT
1. **Visit ChatGPT website**: https://chat.openai.com
2. **Settings menu**: Bottom-left profile → Settings
3. **Data controls**: "Data controls" menu
4. **Request export**: Click "Export data"
5. **Check email**: Wait for export completion email (usually minutes to hours)
6. **Download**: Click download link in email
7. **Extract**: Unzip the file and find `conversations.json`

## 📂 Step 2: File Preparation

### File Placement
```
Claude-ChatGPT-to-Gemini/
├── input/
│   └── conversations.json  ← Place file here!
```

### File Verification
After placement, verify:
- File name is exactly `conversations.json`
- File size is not 0KB  
- File is correctly located in `input/` folder

## ⚙️ Step 3: Execution

### Basic Execution (Recommended)
1. **Run BAT file**: Double-click `process_conversations.bat`
2. **Wait for processing**: Monitor progress in console window
3. **Wait for completion**: Until "Press any key to continue..." message

### Advanced Execution (For troubleshooting)
```bash
# Run from command prompt
cd "path/to/Claude-ChatGPT-to-Gemini"
process_conversations.bat

# Or run Python directly
cd modules
python main_processor_fixed.py ../input/conversations.json
```

## 📊 Step 4: Verify Results

### Check Generated Files
After completion, check the `output/` folder:

#### Essential Generated Files
- ✅ `conversations_organized.txt` - Organized complete conversations
- ✅ `conversations_index.txt` - Conversation list
- ✅ `processing_report.txt` - Processing summary

#### NotebookLM Split Files
- ✅ `notebooklm_part_01_*.txt` 
- ✅ `notebooklm_part_02_*.txt`
- ✅ `notebooklm_part_03_*.txt`
- ✅ `notebooklm_index.txt` - Split file guide

### Quality Verification
Check `processing_report.txt` for:
```
Original conversations: XXX
Processed conversations: XXX  ← Should match
Total words: XXX,XXX
Generated files: X
```

## 🎯 Step 5: Using NotebookLM

### Upload to NotebookLM
1. **Access NotebookLM**: https://notebooklm.google.com
2. **Create new notebook**: Click "New notebook"
3. **Upload files**: 
   - "Upload" → "Upload files"
   - Select split files from `output/` folder
   - Can upload all files at once

### Recommended Upload Order
1. **Largest files first**: Files with most words
2. **Priority topics**: Programming → Data Analysis → AI Tech → Others
3. **Gradual expansion**: Add more files as needed

### NotebookLM Usage Tips
```
Example Questions:
- "What programming challenges did I face most often?"
- "How did my AI usage patterns evolve over time?"
- "What are the main topics I discussed with AI assistants?"
- "What problem-solving approaches do I use?"
- "Show me conversations about data analysis projects"
```

## 🔧 Troubleshooting

### Common Issues

#### "Python not found"
**Solution:**
1. Install Python from https://python.org
2. Check "Add Python to PATH" during installation
3. Restart computer after installation

#### "conversations.json not found"
**Solution:**
1. Check file path: `input/conversations.json`
2. Verify filename accuracy (case-sensitive)
3. Ensure file permissions

#### "Memory insufficient" error
**Solution:**
1. Close other programs
2. Check file size (recommend <500MB)
3. Restart system and retry

### Data-Specific Notes

#### Claude Data
- **Normal processing**: Simple array structure, fast processing
- **Note**: Messages are within content arrays

#### ChatGPT Data  
- **Complex structure**: mapping-based node tree
- **Processing time**: Takes longer than Claude
- **Verification needed**: Possible conversation loss

### Using Log Files

#### Track Processing
```bash
# Check real-time logs
type temp\processing.log

# Check error logs  
type temp\error.log
```

#### Log Interpretation
```
[INFO] Starting conversation extraction... ← Normal
[WARNING] Empty message found... ← Ignorable
[ERROR] JSON parsing failed... ← Action needed
```

## 📈 Advanced Usage

### Customizing Categories
Modify keywords in `modules/categorizer.py`:
```python
keywords = {
    'Programming': ['coding', 'python', 'javascript', 'development'],
    'Custom_Category': ['my keyword1', 'my keyword2']
}
```

### Adjusting Split Size
Change word limit in `modules/notebooklm_splitter.py`:
```python
target_words_per_file = 400000  # Default value
# Change to 300000 etc. if needed
```

### Manual Execution Script
```python
# Step-by-step manual execution
from modules.claude_processor import process_claude_data
from modules.chatgpt_processor import process_chatgpt_data
from modules.notebooklm_splitter import split_for_notebooklm

# Step 1: Process data
result = process_claude_data('input/conversations.json')

# Step 2: Split
split_for_notebooklm(result, 'output/')
```

## 🔄 Updates and Maintenance

### Check New Versions
- Check README.md for version information
- Re-download for feature additions or bug fixes

### Data Backup
```
Recommended backup structure:
backups/
├── 2024-12-01_claude_backup/
│   ├── input/conversations.json
│   └── output/ (entire folder)
└── 2024-12-01_chatgpt_backup/
    ├── input/conversations.json  
    └── output/ (entire folder)
```

### Regular Processing
- Monthly: Export new conversation data
- Cumulative processing: Merge with existing data

---

**💡 Tip: Test with small data first when using for the first time!**