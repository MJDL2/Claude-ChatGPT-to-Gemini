# ⚠️ Troubleshooting Guide

## 🚨 Common Errors and Solutions

### 1. **ModuleNotFoundError: No module named 'categorizer'**
```
❌ Error: Python cannot find modules
✅ Solution: Ensure running from modules/ folder
```

### 2. **UnicodeDecodeError: 'cp949' codec can't decode**
```
❌ Error: Korean encoding issue
✅ Solution: Re-save conversations.json as UTF-8
```

### 3. **JSONDecodeError: Expecting value**
```
❌ Error: JSON file is corrupted
✅ Solution: Re-download the file
```

### 4. **MemoryError**
```
❌ Error: Insufficient memory (large files)
✅ Solution: Close other programs and retry
```

### 5. **PermissionError: [Errno 13]**
```
❌ Error: No file write permission
✅ Solution: Run as administrator
```

## 🔧 Step-by-Step Resolution Guide

### Step 1: Basic Checks
```bash
# Check Python installation
python --version

# Check file exists
dir input\conversations.json

# Check module files
dir modules\*.py
```

### Step 2: Environment Test
```bash
# Run environment test
cd modules
python test_environment.py
```

### Step 3: Auto Diagnosis
```bash
# Run error diagnosis and recovery
cd modules  
python error_recovery.py
```

### Step 4: Manual Execution
```bash
# Run main processor directly
cd modules
python main_processor_fixed.py
```

## 🐛 Debugging Tips

### Check Log Files
```
temp/
├── processing_YYYYMMDD_HHMMSS.log  # Processing logs
├── error_YYYYMMDD_HHMMSS.log       # Error details
└── diagnostic_report_*.txt         # Diagnosis results
```

### File Size Guidelines
```
< 1MB    : Normal processing
1-50MB   : Standard processing time
50-200MB : Long processing (5-10 minutes)
200MB+   : Very long, watch memory
500MB+   : Consider splitting
```

### Memory Optimization
```python
# For large file processing:
1. Close all other programs
2. Minimize browser tabs
3. Restart system before running
4. Increase virtual memory settings
```

## 🔄 Recovery Procedures

### Complete Reset
```bash
1. Delete all contents of temp/ folder
2. Delete all contents of output/ folder  
3. Delete Python cache (__pycache__)
4. Re-run script
```

### Selective Recovery
```bash
1. Environment test only: test_environment.py
2. File diagnosis only: error_recovery.py
3. Main processing only: main_processor_fixed.py
```

## 📞 Advanced Troubleshooting

### Windows Permission Issues
```cmd
# Run command prompt as administrator
runas /user:Administrator cmd

# Temporarily disable UAC
# Control Panel → User Accounts → Change UAC settings
```

### Python Path Issues  
```cmd
# Check Python path
where python

# Check PATH environment variable
echo %PATH%

# Reinstall Python with "Add to PATH" checked
```

### Antivirus Interference
```
1. Temporarily disable Windows Defender real-time protection
2. Temporarily disable third-party antivirus real-time scanning
3. Add project folder to antivirus exception list
```

## 🚀 Performance Optimization

### Speed Improvements
```python
1. Use SSD (5-10x faster than HDD)
2. Sufficient RAM (8GB+ recommended)
3. Minimize background programs
4. Check file size beforehand
```

### Batch Processing
```bash
# Process multiple files sequentially
for %%f in (*.json) do (
    copy "%%f" input\conversations.json
    call process_conversations.bat
    move output\* backup\%%~nf\
)
```

## 🔍 Diagnostic Commands

### System Information
```cmd
# Python version and path
python --version
where python

# System resources
systeminfo | findstr /C:"Total Physical Memory"

# Disk space
dir C:\ /-c
```

### File Analysis
```python
# Check JSON structure
import json
with open('input/conversations.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    print(f"Type: {type(data)}")
    print(f"Length: {len(data)}")
    if data: print(f"First keys: {list(data[0].keys())}")
```

## 🆘 Emergency Fixes

### If Nothing Works
```
1. Download fresh copy of the tool
2. Use different computer/environment
3. Try smaller sample of data first
4. Contact for support with log files
```

### Quick Fixes
```bash
# Fix most common issues
1. Restart computer
2. Re-download conversations.json
3. Run as administrator
4. Disable antivirus temporarily
5. Use English-only folder path
```

## 📊 Error Codes

### Exit Codes
```
0   : Success
1   : General error
2   : File not found
3   : Permission denied
4   : Memory error
5   : JSON parsing error
```

### Log Levels
```
[INFO]    : Normal operation
[WARNING] : Non-critical issues
[ERROR]   : Critical problems
[DEBUG]   : Detailed information
```

---

**💡 If problems persist, environment-specific solutions may be needed.**

## 🎯 Prevention Tips

### Before Running
- [ ] Check Python installation
- [ ] Verify file location and name
- [ ] Ensure sufficient disk space
- [ ] Close unnecessary programs

### During Processing
- [ ] Don't close console window
- [ ] Don't modify input files
- [ ] Monitor progress messages
- [ ] Watch for error messages

### After Completion
- [ ] Verify all output files exist
- [ ] Check processing report
- [ ] Backup important results
- [ ] Clean up temp files if needed