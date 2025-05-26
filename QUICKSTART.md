# 🚀 원클릭 실행 가이드

## 빠른 시작 (3단계)

### 1️⃣ 파일 준비
- Claude 또는 ChatGPT에서 `conversations.json` 파일 다운로드
- `input/` 폴더에 복사

### 2️⃣ 실행
- `process_conversations.bat` 더블클릭

### 3️⃣ 결과 확인
- `output/` 폴더에서 NotebookLM용 파일들 확인

---

## 📂 파일 구조
```
Claude-ChatGPT-to-Gemini/
├── 📄 process_conversations.bat  ← 이 파일 실행!
├── 📁 input/
│   └── conversations.json        ← 여기에 파일 복사
├── 📁 output/                    ← 결과 파일 생성됨
└── 📁 modules/                   ← 처리 모듈들
```

## ⚠️ 문제 해결

### "Python을 찾을 수 없습니다"
→ https://python.org 에서 Python 설치

### "conversations.json을 찾을 수 없습니다"  
→ input/ 폴더에 파일명 정확히 확인

### "처리 실패"
→ temp/ 폴더의 로그 파일 확인

---

**💡 도움이 필요하면 INSTRUCTIONS.md 파일을 참조하세요!**