import streamlit as st

# 페이지 설정 (와이드 레이아웃 & 어두운 테마 느낌)
st.set_page_config(
    page_title="Celestial Myth & Constellation",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="expanded",
)

# 웅장하고 아늑한 우주 테마 CSS 스타일링
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700;900&family=Noto+Serif+KR:wght@300;500;700&display=swap');

    .main {
        background: linear-gradient(180deg, #050515 0%, #0a0a28 50%, #11113a 100%);
        color: #e2e8f0;
        font-family: 'Noto Serif KR', serif;
    }
    .stAppHeader {
        background-color: transparent !important;
    }
    h1, h2, h3 {
        font-family: 'Cinzel', 'Noto Serif KR', serif !important;
        letter-spacing: 2px;
    }
    .hero-title {
        text-align: center;
        font-size: 3rem;
        font-weight: 900;
        background: linear-gradient(135deg, #FFE259 0%, #FFA751 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
        text-shadow: 0 0 25px rgba(255, 215, 0, 0.3);
    }
    .hero-subtitle {
        text-align: center;
        font-size: 1.1rem;
        color: #94a3b8;
        margin-bottom: 2rem;
        font-style: italic;
    }
    .myth-card {
        background: rgba(15, 23, 42, 0.75);
        border: 1px solid rgba(212, 175, 55, 0.3);
        border-radius: 16px;
        padding: 28px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5), inset 0 0 15px rgba(212, 175, 55, 0.05);
        backdrop-filter: blur(8px);
    }
    .gold-accent {
        color: #f1c40f;
        font-weight: 700;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# 헤더 섹션
st.markdown(
    "<div class='hero-title'>⚔️ CELESTIAL MYTHS 🌌</div>",
    unsafe_allow_html=True,
)
st.markdown(
    "<div class='hero-subtitle'>밤하늘을 수놓은 영원한 별들과 그 속에 숨겨진 신화의 기록</div>",
    unsafe_allow_html=True,
)

# 별자리 데이터 및 SVG 백터 그래픽 (외부 이미지 라이브러리 없이 자체 렌더링)
constellations = {
    "황소자리 (Taurus)": {
        "period": "04.20 ~ 05.20",
        "element": "흙 (Earth) / 수호성: 금성",
        "summary": "황금 뿔을 가진 신성한 소, 제우스의 강렬한 사랑과 매혹의 변신",
        "story": """
        신들의 왕 제우스는 페니키아의 아름다운 공주 에우로파에게 한눈에 반하게 됩니다. 
        제우스는 그녀에게 다가가기 위해 눈처럼 하얗고 융단처럼 부드러운 털, 그리고 달콤한 향기를 내뿜는 황금 뿔을 가진 거대한 **황소**로 변신했습니다.

        바닷가에서 한가로이 거닐던 에우로파는 황소의 눈부신 아름다움과 온순함에 매료되어 그 등 위에 올라탔습니다. 
        그 순간 황소는 바다로 뛰어들어 크레타 섬까지 파도를 가르며 헤엄쳐 갔습니다. 크레타에 도착한 제우스는 본 모습을 드러내고 사랑을 고백하였고, 
        이 위대한 변신과 사랑을 기념하기 위해 하늘에 **황소자리**를 헌정했습니다.
        """,
        "svg": """
        <svg viewBox="0 0 400 400" width="100%" height="320" xmlns="http://www.w3.org/2000/svg" style="background:#030712; border-radius:12px; border:1px solid #334155;">
            <!-- Background Glow -->
            <circle cx="200" cy="200" r="150" fill="none" stroke="#f1c40f" stroke-opacity="0.08" stroke-width="1" />
            <circle cx="200" cy="200" r="100" fill="none" stroke="#f1c40f" stroke-opacity="0.05" stroke-width="1" />
            <!-- Constellation Lines -->
            <polyline points="70,120 130,170 190,190 280,180 340,110" fill="none" stroke="#60a5fa" stroke-width="2" stroke-dasharray="4,2"/>
            <polyline points="190,190 250,250 320,280" fill="none" stroke="#60a5fa" stroke-width="2" stroke-dasharray="4,2"/>
            <polyline points="130,170 210,130 280,180" fill="none" stroke="#60a5fa" stroke-width="2" stroke-dasharray="4,2"/>
            <!-- Stars -->
            <circle cx="70" cy="120" r="5" fill="#fef08a"/><text x="60" y="105" fill="#93c5fd" font-size="10">El Nath</text>
            <circle cx="130" cy="170" r="4" fill="#ffffff"/>
            <!-- Aldebaran (Alpha) -->
            <circle cx="190" cy="190" r="9" fill="#f97316"/>
            <circle cx="190" cy="190" r="15" fill="#f97316" fill-opacity="0.3"/>
            <text x="195" y="210" fill="#f97316" font-size="11" font-weight="bold">Aldebaran (알데바란)</text>
            <circle cx="280" cy="180" r="4" fill="#ffffff"/>
            <circle cx="340" cy="110" r="5" fill="#fef08a"/>
            <circle cx="250" cy="250" r="4" fill="#ffffff"/>
            <circle cx="320" cy="280" r="4" fill="#ffffff"/>
            <circle cx="210" cy="130" r="4" fill="#ffffff"/>
            <!-- Pleiades Cluster representation -->
            <g transform="translate(115, 155)">
                <circle cx="0" cy="0" r="2" fill="#93c5fd"/>
                <circle cx="4" cy="-3" r="2" fill="#93c5fd"/>
                <circle cx="-3" cy="5" r="2" fill="#93c5fd"/>
                <circle cx="6" cy="3" r="2" fill="#93c5fd"/>
            </g>
        </svg>
        """,
    },
    "오리온자리 (Orion)": {
        "period": "겨울철 대표 별자리",
        "element": "불 (Fire) / 거인 사냥꾼",
        "summary": "밤하늘의 위풍당당한 사냥꾼, 달의 여신 아르테미스와의 비극적 서사",
        "story": """
        오리온은 바다의 신 포세이돈의 아들이자 세상에서 가장 용맹하고 당당한 **거인 사냥꾼**이었습니다. 
        그는 달과 사냥의 여신인 아르테미스와 깊은 사랑에 빠졌으나, 이를 질투한 아르테미스의 오빠 아폴론의 계략에 빠지게 됩니다.

        아폴론은 바다 멀리 헤엄치는 오리온을 겨누며 아르테미스에게 저 멀리 보이는 검은 표적을 맞출 수 있겠냐고 도발했습니다. 
        자신의 활솜씨에 자부심이 높던 아르테미스는 그것이 사랑하는 오리온인 줄도 모른 채 화살을 쏘아 맞추고 말았습니다. 
        뒤늦게 자신이 오리온을 쏘았음을 알게 된 아르테미스는 통곡하였고, 제우스에게 부탁하여 그를 밤하늘에 별자리로 만들어 영원히 기억되게 했습니다.
        """,
        "svg": """
        <svg viewBox="0 0 400 400" width="100%" height="320" xmlns="http://www.w3.org/2000/svg" style="background:#030712; border-radius:12px; border:1px solid #334155;">
            <!-- Outer Glow -->
            <circle cx="200" cy="200" r="160" fill="none" stroke="#38bdf8" stroke-opacity="0.08" stroke-width="1" />
            <!-- Skeleton Lines -->
            <line x1="120" y1="90" x2="280" y2="110" stroke="#f43f5e" stroke-width="1.5" stroke-dasharray="3,3"/>
            <line x1="120" y1="90" x2="160" y2="200" stroke="#f43f5e" stroke-width="1.5"/>
            <line x1="280" y1="110" x2="240" y2="200" stroke="#f43f5e" stroke-width="1.5"/>
            <!-- Orion Belt -->
            <line x1="160" y1="200" x2="240" y2="200" stroke="#fbbf24" stroke-width="2.5"/>
            <line x1="160" y1="200" x2="140" y2="310" stroke="#f43f5e" stroke-width="1.5"/>
            <line x1="240" y1="200" x2="260" y2="300" stroke="#f43f5e" stroke-width="1.5"/>
            <line x1="140" y1="310" x2="260" y2="300" stroke="#f43f5e" stroke-width="1.5" stroke-dasharray="3,3"/>
            <!-- Betelgeuse (Red Supergiant) -->
            <circle cx="120" cy="90" r="9" fill="#ef4444"/>
            <circle cx="120" cy="90" r="16" fill="#ef4444" fill-opacity="0.25"/>
            <text x="35" y="85" fill="#ef4444" font-size="11" font-weight="bold">Betelgeuse (베텔게우스)</text>
            <!-- Bellatrix -->
            <circle cx="280" cy="110" r="6" fill="#38bdf8"/>
            <text x="290" y="105" fill="#38bdf8" font-size="10">Bellatrix</text>
            <!-- Belt Stars -->
            <circle cx="160" cy="200" r="5" fill="#ffffff"/>
            <circle cx="200" cy="200" r="5" fill="#ffffff"/>
            <circle cx="240" cy="200" r="5" fill="#ffffff"/>
            <text x="175" y="220" fill="#fbbf24" font-size="10">Orion's Belt</text>
            <!-- Saiph -->
            <circle cx="140" cy="310" r="5" fill="#38bdf8"/>
            <!-- Rigel (Blue Supergiant) -->
            <circle cx="260" cy="300" r="8" fill="#38bdf8"/>
            <circle cx="260" cy="300" r="15" fill="#38bdf8" fill-opacity="0.3"/>
            <text x="275" y="320" fill="#38bdf8" font-size="11" font-weight="bold">Rigel (리겔)</text>
        </svg>
        """,
    },
    "카시오페아자리 (Cassiopeia)": {
        "period": "북쪽 밤하늘의 W 별자리",
        "element": "허영과 오만의 보응, 왕비의 의자",
        "summary": "허영심의 대가로 밤하늘에 묶여 거꾸로 매달린 에티오피아의 왕비",
        "story": """
        카시오페아는 에티오피아의 왕비로, 뛰어난 미모를 가졌지만 자만심이 넘쳤습니다. 
        그녀는 "나와 내 딸 안드로메다가 바다의 요정 네레이스들보다 훨씬 아름답다"고 자만했고, 이에 분노한 바다의 신 포세이돈은 에티오피아에 괴물 고래를 보내 대지를 황폐화시켰습니다.

        결국 딸 안드로메다를 괴물에게 바물로 바쳐야 했던 카시오페아는 사후 하늘에 올라가 별자리가 되었으나, 
        그녀의 오만함을 경계하는 의미로 의자에 묶인 채 **하루의 절반을 거꾸로 매달려 있는 형벌**을 받게 되었습니다. 
        오늘날 북쪽 하늘에서 뚜렷한 **'W'** 자 모양으로 빛나는 별자리가 바로 카시오페아입니다.
        """,
        "svg": """
        <svg viewBox="0 0 400 400" width="100%" height="320" xmlns="http://www.w3.org/2000/svg" style="background:#030712; border-radius:12px; border:1px solid #334155;">
            <circle cx="200" cy="200" r="140" fill="none" stroke="#a855f7" stroke-opacity="0.1" stroke-width="1" />
            <!-- W Shape Lines -->
            <polyline points="60,160 130,240 200,170 280,250 340,150" fill="none" stroke="#c084fc" stroke-width="2.5"/>
            <!-- Stars -->
            <circle cx="60" cy="160" r="6" fill="#fef08a"/><text x="45" y="145" fill="#e9d5ff" font-size="10">Caph</text>
            <circle cx="130" cy="240" r="7" fill="#fef08a"/><text x="110" y="265" fill="#e9d5ff" font-size="10">Schedar</text>
            <circle cx="200" cy="170" r="8" fill="#ffffff"/>
            <circle cx="200" cy="170" r="14" fill="#ffffff" fill-opacity="0.2"/>
            <text x="185" y="150" fill="#ffffff" font-size="11" font-weight="bold">Gamma Cas</text>
            <circle cx="280" cy="250" r="6" fill="#fef08a"/><text x="280" y="270" fill="#e9d5ff" font-size="10">Ruchbah</text>
            <circle cx="340" cy="150" r="5" fill="#fef08a"/><text x="330" y="135" fill="#e9d5ff" font-size="10">Segin</text>
        </svg>
        """,
    },
    "사자자리 (Leo)": {
        "period": "07.23 ~ 08.22",
        "element": "불 (Fire) / 수호성: 태양",
        "summary": "네메아 계곡을 호령하던 용맹하고 단단한 맹수, 헤라클레스의 첫 과업",
        "story": """
        네메아 계곡에 살던 사자는 무서운 크기와 강력한 힘을 가지고 있었을 뿐만 아니라, 
        어떠한 창이나 칼, 화살로도 뚫을 수 없는 철갑 같은 가죽을 가지고 있어 사람들에게 공포의 대상이었습니다.

        그리스 신화 최고의 영웅 **헤라클레스**는 12가지 과업 중 첫 번째로 이 무시무시한 사자를 퇴치하라는 명령을 받았습니다. 
        무기로는 사자를 쓰러뜨릴 수 없음을 깨달은 헤라클레스는 사자와 격투를 벌여 제압했습니다. 
        제우스는 이 용맹했던 네메아 사자의 비범함과 헤라클레스의 영웅적 승리를 기억하기 위해 그 사자를 하늘로 올려 보내 **사자자리**로 만들었습니다.
        """,
        "svg": """
        <svg viewBox="0 0 400 400" width="100%" height="320" xmlns="http://www.w3.org/2000/svg" style="background:#030712; border-radius:12px; border:1px solid #334155;">
            <!-- Sickle / Head -->
            <polyline points="280,120 250,90 200,100 180,140 210,180 260,180" fill="none" stroke="#f59e0b" stroke-width="2"/>
            <!-- Body -->
            <polyline points="260,180 130,220 90,280 190,270 260,180" fill="none" stroke="#f59e0b" stroke-width="2"/>
            <polyline points="130,220 70,200" fill="none" stroke="#f59e0b" stroke-width="2" stroke-dasharray="3,3"/>
            <!-- Regulus (Alpha Star) -->
            <circle cx="260" cy="180" r="9" fill="#38bdf8"/>
            <circle cx="260" cy="180" r="16" fill="#38bdf8" fill-opacity="0.25"/>
            <text x="275" y="185" fill="#38bdf8" font-size="11" font-weight="bold">Regulus (레굴루스)</text>
            <!-- Denebola (Tail) -->
            <circle cx="70" cy="200" r="7" fill="#fef08a"/>
            <text x="35" y="190" fill="#fef08a" font-size="10">Denebola</text>
            <!-- Other Main Stars -->
            <circle cx="280" cy="120" r="5" fill="#ffffff"/>
            <circle cx="250" cy="90" r="4" fill="#ffffff"/>
            <circle cx="200" cy="100" r="5" fill="#ffffff"/>
            <circle cx="180" cy="140" r="5" fill="#ffffff"/>
            <circle cx="130" cy="220" r="5" fill="#ffffff"/>
            <circle cx="190" cy="270" r="5" fill="#ffffff"/>
        </svg>
        """,
    },
}

# 별자리 선택 사이드바
with st.sidebar:
    st.markdown("### 📜 SELECT CONSTELLATION")
    selected_name = st.radio(
        "탐색할 별자리를 선택하세요:", list(constellations.keys())
    )

    st.markdown("---")
    st.markdown(
        """
        <div style='font-size: 0.85rem; color: #64748b; text-align: center;'>
            별자리 오디세이 웹 앱<br>
            <i>Pure Python & Streamlit Engine</i>
        </div>
        """,
        unsafe_allow_html=True,
    )

selected_data = constellations[selected_name]

# 메인 콘텐츠 레이아웃
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.markdown(
        f"""
        <div class='myth-card'>
            <h2 style='color: #f1c40f; margin-top:0;'>{selected_name}</h2>
            <p><span class='gold-accent'>🗓️ 수호 주기:</span> {selected_data['period']}</p>
            <p><span class='gold-accent'>✨ 속성:</span> {selected_data['element']}</p>
            <hr style='border-color: rgba(212,175,55,0.2); margin: 15px 0;'>
            <h4 style='color: #e2e8f0;'>“{selected_data['summary']}”</h4>
            <br>
            <div style='line-height: 1.8; color: #cbd5e1; text-align: justify;'>
                {selected_data['story']}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        "<h3 style='text-align: center; color: #93c5fd;'>🌌 CONSTELLATION MAP</h3>",
        unsafe_allow_html=True,
    )
    # SVG 렌더링
    st.markdown(selected_data["svg"], unsafe_allow_html=True)
    st.caption("※ 성도 속 범주: 붉은색/파란색 큰 원은 주요 알파성(Alpha Star)을 나타냅니다.")

st.markdown("<br><hr style='border-color: #1e293b;'><br>", unsafe_allow_html=True)

# 하단 웅장한 가이드 인포박스
st.info("🌌 **Tip:** 밤하늘에서 별자리를 찾으려면 도시 불빛이 적은 곳에서 밝은 알파성을 먼저 찾아보세요.")
