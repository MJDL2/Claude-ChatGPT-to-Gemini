# 🤖 Claude & ChatGPT → Gemini 변환기

Claude와 ChatGPT 대화 내보내기 파일을 **NotebookLM (Gemini)** 호환 형식으로 변환하여 강력한 분석과 인사이트를 얻으세요.

## 🎯 이 도구가 하는 일

AI 대화 히스토리를 정리된 검색 가능한 지식 베이스로 변환하여 NotebookLM의 AI 기반 인사이트로 분석할 수 있게 해줍니다.

### ✨ 주요 기능

- 🔍 **자동 감지**: Claude vs ChatGPT 데이터 형식 자동 식별
- 🏷️ **스마트 분류**: AI 대화를 주제별로 자동 정렬 (프로그래밍, 데이터 분석, AI 기술 등)
- 📊 **NotebookLM 최적화**: 50만 단어 제한에 맞춰 파일 분할
- 🚀 **원클릭 처리**: 간단한 배치 파일 실행
- 🔧 **오류 복구**: 포괄적인 오류 처리 및 진단
- 🌏 **한국어/영어 지원**: 이중 언어 키워드 기반 분류
- 📋 **상세 리포트**: 처리 통계 및 파일 가이드

## 🚀 빠른 시작

### 1. 데이터 내보내기
**Claude**: 설정 → 데이터 내보내기 → 대화 다운로드  
**ChatGPT**: 설정 → 데이터 제어 → 데이터 내보내기

### 2. 도구 실행
1. `conversations.json` 파일을 `input/` 폴더에 넣기
2. `process_conversations.bat` 더블클릭
3. 처리 완료까지 대기

### 3. NotebookLM에 업로드
1. [NotebookLM](https://notebooklm.google.com) 접속
2. 새 노트북 생성
3. 생성된 `notebooklm_part_*.txt` 파일들 업로드
4. 대화 히스토리에 대해 질문 시작!

## 📊 생성되는 파일들

### 분할된 파일들
- `notebooklm_part_01_Programming.txt` - 코딩, 개발 토론
- `notebooklm_part_02_Data_Analysis.txt` - 데이터 사이언스, 분석 프로젝트  
- `notebooklm_part_03_AI_Tech.txt` - AI, 머신러닝 주제
- `notebooklm_part_04_Problem_Solving.txt` - 문제 해결, 디버깅
- `notebooklm_part_05_General.txt` - 일반적인 대화
- `notebooklm_part_06_Daily_Mixed.txt` - 개인적 대화, 기타 주제

### 분석 리포트
- `processing_report.txt` - 처리 통계
- `conversations_index.txt` - 전체 대화 목록
- `notebooklm_index.txt` - 생성된 파일 사용 가이드

## 💡 NotebookLM 활용 예시

업로드 후 다음과 같은 질문을 해보세요:
- *"내가 프로그래밍에서 가장 자주 겪은 어려움은?"*
- *"시간이 지나면서 AI 사용 패턴이 어떻게 변했나?"*
- *"AI 어시스턴트와 주로 논의한 주제들은?"*
- *"내가 사용하는 문제 해결 접근법은?"*
- *"데이터 분석 프로젝트 대화들을 보여줘"*

## 🛠️ 기술 사양

### 지원 형식
- ✅ Claude `conversations.json` (웹 내보내기)
- ✅ ChatGPT `conversations.json` (웹 내보내기)

### 시스템 요구사항
- Windows 10/11
- Python 3.7+
- 1GB+ 여유 공간

### 처리 성능
- **Claude 데이터**: ~1,000개 대화/분
- **ChatGPT 데이터**: ~500개 대화/분  
- **파일 크기**: 최대 500MB 입력 파일
- **출력**: NotebookLM 50만 단어 제한에 최적화

## 📁 프로젝트 구조

```
Claude-ChatGPT-to-Gemini/
├── 🚀 process_conversations.bat        # 메인 실행 스크립트
├── 📄 README.md                        # 이 파일 (영어)
├── 📄 README_KR.md                     # 한국어 버전
├── 📄 QUICKSTART_KR.md                 # 한국어 빠른 시작
├── 📄 INSTRUCTIONS_KR.md               # 한국어 상세 가이드
├── 📄 TROUBLESHOOTING_KR.md            # 한국어 문제 해결
├── 📁 modules/                         # 처리 모듈들
├── 📁 input/                           # JSON 파일을 여기에
├── 📁 output/                          # 생성된 파일들
└── 📁 temp/                            # 로그 및 임시 파일
```

## 🔧 고급 사용법

### 환경 테스트
```bash
cd modules
python test_environment.py
```

### 오류 진단
```bash
cd modules
python error_recovery.py
```

### 수동 처리
```bash
cd modules
python main_processor_fixed.py ../input/conversations.json
```

## ⚠️ 문제 해결

### 자주 발생하는 문제들
- **"Python을 찾을 수 없습니다"** → Python 3.7+를 "PATH에 추가" 옵션과 함께 설치
- **"conversations.json을 찾을 수 없습니다"** → 파일이 `input/` 폴더에 있는지 확인
- **"권한이 거부됨"** → 관리자 권한으로 실행
- **메모리 오류** → 다른 프로그램 종료 후 컴퓨터 재시작

### 도움 받기
1. 자세한 해결 방법은 `TROUBLESHOOTING_KR.md` 확인
2. 자동 진단을 위해 `error_recovery.py` 실행
3. `temp/` 폴더의 로그 파일 검토
4. 지원되는 내보내기 형식인지 확인

## 🎉 성공 사례

대화를 인사이트로 변환하세요:
- **연구**: 학습 패턴과 지식 격차 분석
- **생산성**: 일반적인 문제와 해결책 식별
- **문서화**: 대화에서 검색 가능한 지식 베이스 생성
- **성찰**: 사고 과정의 진화 이해

## 📈 로드맵

- [ ] 다른 AI 플랫폼 지원 (Perplexity, Bing Chat)
- [ ] 대화 병합 및 중복 제거
- [ ] 시각적 분석 대시보드
- [ ] 자동 백업 및 버전 관리
- [ ] 다른 형식으로 내보내기 (Obsidian, Notion)

## 🤝 기여하기

기여를 환영합니다! 모듈화된 설계로 다음이 쉽습니다:
- 새로운 AI 플랫폼 지원 추가
- 분류 알고리즘 개선
- 오류 처리 강화
- 새로운 출력 형식 추가

## 📄 라이선스

MIT 라이선스 - 자유롭게 사용, 수정, 배포하세요!

---

**🎯 NotebookLM으로 AI 대화를 가치 있는 인사이트로 바꿔보세요!**

*AI 네이티브 세대를 위한 디지털 상호작용 이해 도구*

## 🔗 관련 문서

- [🚀 빠른 시작 가이드 (한국어)](QUICKSTART_KR.md)
- [📖 상세 사용법 (한국어)](INSTRUCTIONS_KR.md)  
- [🔧 문제 해결 (한국어)](TROUBLESHOOTING_KR.md)
- [📄 English README](README.md)