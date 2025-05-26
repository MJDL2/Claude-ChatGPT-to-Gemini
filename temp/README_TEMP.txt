🔧 임시 파일 및 로그

이 폴더에는 처리 과정의 로그와 임시 파일들이 저장됩니다.

📋 생성되는 파일들:
- processing_YYYYMMDD_HHMMSS.log  (처리 과정 로그)
- error_YYYYMMDD_HHMMSS.log       (오류 로그)
- temp_*.json                     (임시 JSON 파일)

🔍 문제 해결시 확인할 로그:
- processing.log: 전체 처리 과정
- error.log: 오류 상세 정보

💡 로그 활용법:
- 처리가 실패하면 가장 최근 error 로그 확인
- 진행 상황을 보려면 processing 로그 확인
- 로그 파일을 텍스트 편집기로 열어서 확인

⚠️ 주의:
- 이 폴더의 파일들은 삭제해도 됩니다
- 로그 파일은 자동으로 누적됩니다
- 용량 관리를 위해 주기적으로 정리하세요