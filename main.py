import random
import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="💖 MBTI 뽀짝 여행 추천 💖", page_icon="✈️", layout="centered"
)

# 귀여운 스타일링 적용
st.markdown(
    """
    <style>
    .main {
        background-color: #FFF5F7;
    }
    .stButton>button {
        background-color: #FFB6C1;
        color: white;
        border-radius: 20px;
        border: none;
        padding: 10px 24px;
        font-weight: bold;
        font-size: 16px;
    }
    .stButton>button:hover {
        background-color: #FF69B4;
        color: white;
    }
    .title-text {
        color: #FF1493;
        text-align: center;
        font-weight: bold;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# 앱 타이틀
st.markdown(
    "<h1 class='title-text'>🎀 뽀짝 MBTI 여행지 추천 🎀</h1>",
    unsafe_allow_html=True,
)
st.write(" ")
st.write("나의 MBTI를 선택하면 딱 맞는 찰떡 여행지를 알려줄게! ✨")

# MBTI 데이터 베이스
mbti_destinations = {
    "ISTJ": {
        "place": "경주 역사유적지구 🏯",
        "desc": "계획대로 착착! 깔끔하고 차분하게 고즈넉한 역사를 즐길 수 있는 경주가 딱이야!",
    },
    "ISFJ": {
        "place": "제주도 힐링 숲길 🌿",
        "desc": "마음이 따뜻해지는 소소하고 다정한 여행, 삼다수 숲길을 도란도란 걸어보는 건 어때?",
    },
    "INFJ": {
        "place": "스위스 인터라켄 🏔️",
        "desc": "조용히 자연을 바라보며 깊은 생각을 정리하기 좋은 동화 같은 곳이야!",
    },
    "INTJ": {
        "place": "영국 런던 🏰",
        "desc": "알찬 박물관 투어와 완벽한 동선 계획이 빛을 발하는 지적인 도시!",
    },
    "ISTP": {
        "place": "뉴질랜드 퀸스타운 🪂",
        "desc": "액티비티 만점! 짜릿한 익스트림 스포츠를 즐기며 스트레스를 날려보자!",
    },
    "ISFP": {
        "place": "치앙마이 감성 카페거리 ☕",
        "desc": "느긋하게 마음에 드는 카페에 앉아 여유를 즐길 수 있는 힐링 마법의 도시!",
    },
    "INFP": {
        "place": "아이슬란드 오로라 마을 🌌",
        "desc": "몽환적이고 감성 넘치는 오로라를 보며 나만의 밤하늘을 간직해봐!",
    },
    "INTP": {
        "place": "일본 도쿄 아키하바라&과학관 🤖",
        "desc": "호기심을 자극하는 흥미진진한 탐구 거리들이 가득한 곳으로 떠나보자!",
    },
    "ESTP": {
        "place": "발리 서핑 비치 🏄",
        "desc": "지루할 틈이 없다! 션한 바다에서 파도를 타며 온몸으로 즐기는 여행!",
    },
    "ESFP": {
        "place": "스페인 바르셀로나 🎉",
        "desc": "열정과 흥이 가득한 거리! 신나는 음악과 맛있는 타파스가 너를 기다려!",
    },
    "ENFP": {
        "place": "미국 캘리포니아 디즈니랜드 🎈",
        "desc": "상상했던 모든 것이 현실로! 하루 종일 텐션 업업 되는 꿈과 희망의 나라!",
    },
    "ENTP": {
        "place": "방콕 야시장 & 루프탑 🌃",
        "desc": "새로운 자극과 다채로운 즐길 거리가 매시간 넘쳐나는 핫플레이스!",
    },
    "ESTJ": {
        "place": "싱가포르 도시 투어 🏙️",
        "desc": "체계적이고 정돈된 최고급 도시 환경에서 깔끔한 야경 투어를 즐겨봐!",
    },
    "ESFJ": {
        "place": "다낭 리조트 휴양 🏊",
        "desc": "소중한 사람들과 다 함께 하하호호 웃으며 추억 만들기 제일 좋은 여행지!",
    },
    "ENFJ": {
        "place": "이탈리아 피렌체 🎨",
        "desc": "로맨틱한 예술과 따뜻한 정이 넘치는 낭만 가득 언덕 위에 올라가보자!",
    },
    "ENTJ": {
        "place": "뉴욕 맨해튼 🗽",
        "desc": "세상의 중심에서 펼쳐지는 스파크! 끊임없이 영감을 주는 에너제틱한 도시!",
    },
}

# 셀렉트박스로 MBTI 선택
selected_mbti = st.selectbox(
    "💖 너의 MBTI를 알려줘!", list(mbti_destinations.keys())
)

# 추천 버튼
if st.button("✨ 짠! 여행지 추천받기 ✨"):
    st.balloons()  # 폭죽 효과

    info = mbti_destinations[selected_mbti]

    st.markdown("---")
    st.subheader(f"👉 {selected_mbti}에게 딱 어울리는 곳은?")
    st.header(info["place"])
    st.write(info["desc"])

    # 응원 메세지 리스트
    cheers = [
        "지금 당장 비행기표 알아볼까? ✈️",
        "생각만 해도 두근두근거리지 않아? 💓",
        "가서 맛있는 것도 많이 먹고 오자! 🍧",
        "너의 멋진 여행을 항상 응원해! 🌟",
    ]
    st.info(random.choice(cheers))

st.markdown("---")
st.caption("제작: 세상에서 제일 귀여운 여행 가이드 🐾")
