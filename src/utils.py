import json
import random
from datetime import datetime

def load_greetings():
    """인사말 데이터를 로드합니다."""
    with open('data/greetings.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data['greetings']

def get_daily_greeting():
    """오늘의 인사말을 랜덤하게 선택합니다."""
    greetings = load_greetings()
    return random.choice(greetings)

def get_current_date():
    """현재 날짜를 한글 형식으로 반환합니다."""
    now = datetime.now()
    weekdays = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
    return f"{now.year}년 {now.month}월 {now.day}일 {weekdays[now.weekday()]}" 