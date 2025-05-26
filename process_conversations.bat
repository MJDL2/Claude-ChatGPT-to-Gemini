@echo off
echo ========================================
echo AI 대화 데이터 마이그레이션 도구
echo ========================================
echo.

REM 관리자 권한 확인
net session >nul 2>&1
if %errorLevel% == 0 (
    echo [✅] 관리자 권한으로 실행 중...
) else (
    echo [⚠️] 관리자 권한이 필요할 수 있습니다.
)

echo.
echo [📁] 입력 파일 확인 중...

REM 입력 파일 존재 확인
if not exist "input\conversations.json" (
    echo [❌] 오류: input\conversations.json 파일을 찾을 수 없습니다.
    echo.
    echo 💡 해결 방법:
    echo    1. Claude 또는 ChatGPT에서 대화 데이터를 내보내기 하세요
    echo    2. conversations.json 파일을 input\ 폴더에 복사하세요
    echo    3. 파일명이 정확히 "conversations.json"인지 확인하세요
    echo.
    pause
    exit /b 1
)

echo [✅] conversations.json 파일 발견

REM Python 설치 확인
python --version >nul 2>&1
if %errorLevel% neq 0 (
    echo [❌] Python이 설치되지 않았습니다.
    echo.
    echo 💡 Python 설치 방법:
    echo    1. https://python.org 에서 Python 다운로드
    echo    2. 설치 시 "Add Python to PATH" 체크
    echo    3. 설치 후 이 스크립트를 다시 실행
    echo.
    pause
    exit /b 1
)

echo [✅] Python 감지됨

echo.
echo [📊] 데이터 처리 시작...
echo.

REM 출력 디렉토리 생성
if not exist "output" mkdir output
if not exist "temp" mkdir temp

REM Python 스크립트 실행
cd modules
python main_processor_fixed.py
set EXIT_CODE=%errorLevel%
cd ..

echo.
if %EXIT_CODE% equ 0 (
    echo ========================================
    echo [🎉] 처리 완료!
    echo ========================================
    echo.
    echo 📁 결과 파일 위치: output\
    echo.
    echo 💡 다음 단계:
    echo    1. output\ 폴더의 파일들을 확인하세요
    echo    2. NotebookLM에 업로드하여 활용하세요
    echo    3. processing_report.txt에서 상세 결과를 확인하세요
    echo.
    
    REM 결과 폴더 열기 제안
    set /p OPEN_FOLDER="📂 결과 폴더를 열까요? (y/n): "
    if /i "%OPEN_FOLDER%"=="y" (
        start explorer "output"
    )
    
) else (
    echo ========================================
    echo [❌] 처리 실패
    echo ========================================
    echo.
    echo 💡 문제 해결:
    echo    1. temp\ 폴더의 로그 파일을 확인하세요
    echo    2. conversations.json 파일이 올바른 형식인지 확인하세요
    echo    3. 관리자 권한으로 다시 실행해보세요
    echo.
)

echo.
pause