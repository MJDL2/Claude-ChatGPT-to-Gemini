#!/usr/bin/env python3
"""
대화 주제별 분류 모듈
한국어와 영어 키워드를 기반으로 대화를 카테고리별로 분류
"""


def categorize_conversation(title, content_sample):
    """
    대화 제목과 내용 샘플을 기반으로 카테고리 분류
    
    Args:
        title: 대화 제목
        content_sample: 대화 내용 샘플 (첫 1000자 정도)
    
    Returns:
        str: 분류된 카테고리명
    """
    
    # 카테고리별 키워드 정의 (한국어 + 영어)
    categories = {
        'Programming': [
            # 한국어
            '코딩', '코드', '프로그래밍', '개발', '버그', '오류', '디버깅',
            '알고리즘', '함수', '변수', '클래스', '모듈', '라이브러리',
            '프레임워크', 'api', '데이터베이스', '서버', '클라이언트',
            'ssh', 'vscode', 'git', '배포', '테스트',
            # 영어
            'programming', 'coding', 'code', 'development', 'developer',
            'bug', 'error', 'debug', 'algorithm', 'function', 'variable',
            'class', 'module', 'library', 'framework', 'database',
            'server', 'client', 'javascript', 'python', 'java', 'react',
            'node', 'html', 'css', 'sql', 'typescript'
        ],
        
        'Data_Analysis': [
            # 한국어
            '데이터', '분석', '크롤링', '스크래핑', '뉴스', '정보수집',
            '통계', '시각화', '차트', '그래프', '엑셀', '파싱',
            '수집', '추출', '변환', '정제', '가공',
            # 영어  
            'data', 'analysis', 'analytics', 'crawling', 'scraping',
            'crawler', 'scraper', 'news', 'parsing', 'extraction',
            'statistics', 'visualization', 'chart', 'graph', 'excel',
            'csv', 'json', 'xml', 'api', 'url', 'web', 'site'
        ],
        
        'AI_Tech': [
            # 한국어
            '인공지능', '머신러닝', '딥러닝', '모델', '학습', '훈련',
            '예측', '분류', '자연어처리', '이미지처리', '음성인식',
            'ai', 'gpt', 'claude', 'ollama', 'mcp',
            # 영어
            'artificial intelligence', 'machine learning', 'deep learning',
            'neural network', 'model', 'training', 'prediction', 'classification',
            'nlp', 'computer vision', 'tensorflow', 'pytorch', 'llm',
            'transformer', 'embedding', 'fine-tuning'
        ],
        
        'Problem_Solving': [
            # 한국어
            '문제', '해결', '도움', '질문', '답변', '상담', '지원',
            '트러블슈팅', '해결방법', '방법', '어떻게', '왜', '수정',
            '고치기', '개선', '최적화',
            # 영어
            'problem', 'issue', 'solve', 'solution', 'fix', 'repair',
            'help', 'support', 'troubleshoot', 'debug', 'resolve',
            'how to', 'why', 'what', 'when', 'where', 'improve', 'optimize'
        ],
        
        'Daily_Chat': [
            # 한국어
            '일상', '잡담', '개인', '생각', '감정', '기분', '느낌',
            '경험', '이야기', '대화', '친구', '가족', '관계',
            '취미', '여가', '휴식', '스트레스', '고민', '상담',
            '어둠', '익숙함', '피곤', '휴식', '편안',
            # 영어
            'daily', 'life', 'personal', 'feeling', 'emotion', 'mood',
            'experience', 'story', 'chat', 'talk', 'friend', 'family',
            'relationship', 'hobby', 'leisure', 'stress', 'worry'
        ],
        
        'Korean_Culture': [
            # 한국어
            '정치', '정책', '정부', '대통령', '국회', '선거', '투표',
            '정당', '법률', '제도', '사회', '문화', '한국', '우리나라',
            '공약', '개혁', '정치인', '시민', '국민', '여론',
            # 영어
            'politics', 'policy', 'government', 'president', 'election',
            'vote', 'party', 'law', 'legislation', 'society', 'culture',
            'korea', 'korean', 'seoul', 'citizen', 'democracy'
        ],
        
        'Health_Life': [
            # 한국어
            '건강', '의학', '병원', '의사', '치료', '약', '질병',
            '증상', '진료', '검사', '수술', '운동', '다이어트',
            '영양', '음식', '요리', '레시피', '생활습관',
            '발톱', '피지', '샤워', '통증', '아픔', '몸',
            # 영어
            'health', 'medical', 'doctor', 'hospital', 'treatment',
            'medicine', 'disease', 'symptom', 'diagnosis', 'surgery',
            'exercise', 'diet', 'nutrition', 'food', 'recipe',
            'lifestyle', 'wellness', 'fitness'
        ],
        
        'Business': [
            # 한국어
            '비즈니스', '사업', '회사', '경영', '관리', '매출', '수익',
            '마케팅', '광고', '홍보', '브랜드', '고객', '서비스',
            '전략', '계획', '목표', '성과', '실적', '경쟁', '시장',
            '투자', '자금', '예산', '비용', '경제',
            # 영어
            'business', 'company', 'management', 'revenue', 'profit',
            'marketing', 'advertising', 'brand', 'customer', 'service',
            'strategy', 'plan', 'goal', 'performance', 'competition',
            'market', 'investment', 'budget', 'cost', 'economy'
        ]
    }
    
    # 텍스트 전처리
    text = f"{title} {content_sample}".lower()
    
    # 카테고리별 점수 계산
    category_scores = {}
    
    for category, keywords in categories.items():
        score = 0
        for keyword in keywords:
            # 키워드가 텍스트에 포함된 횟수만큼 점수 증가
            score += text.count(keyword.lower())
        
        category_scores[category] = score
    
    # 가장 높은 점수의 카테고리 반환
    if max(category_scores.values()) > 0:
        best_category = max(category_scores, key=category_scores.get)
        return best_category
    
    # 매칭되는 키워드가 없으면 General
    return 'General'


def get_category_description(category):
    """
    카테고리 설명 반환
    """
    descriptions = {
        'Programming': '프로그래밍, 코딩, 개발 관련 대화',
        'Data_Analysis': '데이터 분석, 크롤링, 정보 수집 관련 대화', 
        'AI_Tech': 'AI, 머신러닝, GPT/Claude 등 인공지능 기술 관련 대화',
        'Problem_Solving': '문제 해결, 기술 지원, 트러블슈팅 관련 대화',
        'Daily_Chat': '일상 대화, 개인적 이야기, 잡담',
        'Korean_Culture': '정치, 정책, 한국 사회/문화 관련 대화',
        'Health_Life': '건강, 의학, 생활습관 관련 대화',
        'Business': '비즈니스, 경영, 경제 관련 대화',
        'General': '일반적 주제, 기타 분류되지 않은 대화'
    }
    
    return descriptions.get(category, '기타 주제의 대화')


def get_all_categories():
    """
    모든 카테고리 목록 반환
    """
    return [
        'Programming',
        'Data_Analysis', 
        'AI_Tech',
        'Problem_Solving',
        'Daily_Chat',
        'Korean_Culture',
        'Health_Life',
        'Business',
        'General'
    ]


def analyze_conversation_distribution(conversations_data):
    """
    대화들의 카테고리 분포 분석
    """
    category_counts = {}
    category_words = {}
    
    for conv in conversations_data:
        category = conv.get('category', 'General')
        word_count = conv.get('word_count', 0)
        
        if category not in category_counts:
            category_counts[category] = 0
            category_words[category] = 0
        
        category_counts[category] += 1
        category_words[category] += word_count
    
    print("\n📊 카테고리별 분포:")
    for category in get_all_categories():
        if category in category_counts:
            count = category_counts[category]
            words = category_words[category]
            description = get_category_description(category)
            print(f"- {category}: {count}개 대화, {words:,} 단어 - {description}")
    
    return category_counts, category_words