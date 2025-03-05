import streamlit as st
from utils import get_daily_greeting, get_current_date

def main():
    st.set_page_config(
        page_title="오늘의 아침 인사",
        page_icon="☀️",
        layout="centered"
    )

    st.title("🌅 오늘의 아침 인사")
    st.subheader(get_current_date())
    
    # 사용자 입력
    user_input = st.text_input("인사해주세요!", placeholder="안녕?")
    
    if user_input and user_input.strip():
        # 응답 메시지
        st.write("오늘의 문구를 드릴까요? 💌")
        
        # 잠시 기다리는 효과
        with st.spinner('문구를 생성하고 있습니다...'):
            greeting = get_daily_greeting()
            
            # 인사말 표시 (아이콘과 함께)
            st.success(f"### {greeting['icon']} {greeting['message']}")
            st.caption(f"*오늘의 인사말 톤: {greeting['tone']}*")
        
        # 새로고침 버튼
        if st.button("✨ 다른 인사말 보기"):
            st.experimental_rerun()

if __name__ == "__main__":
    main() 