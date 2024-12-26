import streamlit as st
import requests
import base64
from io import BytesIO

# 이미지를 base64로 변환하는 함수
def get_image_as_base64(url):
    try:
        response = requests.get(url)
        return base64.b64encode(response.content).decode()
    except:
        return None

# Streamlit 웹앱
st.set_page_config(page_title="Profile Filter Tool", layout="wide")

# 데이터셋 입력
st.title("Instagram Profile Filter Tool")
st.write("데이터셋을 JSON 형태로 붙여넣으세요 (username, src 키 필요)")
input_data = st.text_area("Paste your dataset here", height=200)

if input_data:
    try:
        # JSON 데이터 로드
        import json
        profiles = json.loads(input_data)

        # 필터링된 username 저장 리스트
        selected_usernames = st.session_state.get("selected_usernames", [])

        # UI 생성
        cols = st.columns([0.5, 1, 2])
        cols[0].markdown("**Select**")
        cols[1].markdown("**Profile Photo**")
        cols[2].markdown("**Username**")

        for profile in profiles:
            username = profile.get("username", "Unknown")
            src = profile.get("src", "")

            # Profile UI
            with st.container():
                col1, col2, col3 = st.columns([0.5, 1, 2])
                
                # 체크박스를 첫 번째 열로 이동 (여백 제거)
                is_checked = col1.checkbox(f"Select {username}", key=username, label_visibility="collapsed")
                
                # 이미지 처리 (왼쪽 정렬)
                if src:
                    img_base64 = get_image_as_base64(src)
                    if img_base64:
                        col2.markdown(f'<div style="margin-left: -15px;"><img src="data:image/jpeg;base64,{img_base64}" width="50"></div>', unsafe_allow_html=True)
                    else:
                        col2.markdown('<div style="margin-left: -15px;">❌</div>', unsafe_allow_html=True)
                else:
                    col2.markdown('<div style="margin-left: -15px;">❌</div>', unsafe_allow_html=True)
                
                col3.markdown(f"[{username}](https://www.instagram.com/{username}/)")

                # 체크박스에 따라 선택 상태 업데이트
                if is_checked and username not in selected_usernames:
                    selected_usernames.append(username)
                elif not is_checked and username in selected_usernames:
                    selected_usernames.remove(username)

        # 최종 선택된 username 표시
        st.markdown("---")
        st.subheader("Selected Usernames")
        st.write(selected_usernames)

    except json.JSONDecodeError:
        st.error("Invalid JSON format. Please check your input.") 