import streamlit as st

st.set_page_config(
    page_title = "로그인하세요-클링픽업-"
)

# 기본 사용자 정보
USER_CREDENTIALS = {"웃음코드": "vkdlxld"}

# 세션 상태 초기화
if 'login' not in st.session_state:
    st.session_state['login'] = False

# 로그인 처리 함수
def login(username, password):
    if USER_CREDENTIALS.get(username) == password:
        st.session_state['login'] = True
        st.success("로그인 되었습니다!")
        redirect_url = "링크 넣어야돼여!!!!!!!!!!!!!"
        st.write(f'<meta http-equiv="refresh" content="0; url={redirect_url}">', unsafe_allow_html=True)

    else:
        st.error("잘못된 아이디/패스워드입니다.")

# 로그인 상태 확인
if not st.session_state['login']:
    st.title("로그인하십시오.")

    username = st.text_input("아이디")
    password = st.text_input("패스워드", type="password")
    
    if st.button("Login"):
        login(username, password)
else:
    st.title("안녕하세요!")

    if st.button("Logout"):
        st.session_state['login'] = False
        st.experimental_rerun()
