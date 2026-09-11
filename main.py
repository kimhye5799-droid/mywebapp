from datetime import date
import streamlit as st

# 페이지 구성
st.set_page_config(
    page_title="Zodiac Myth & Constellation",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="expanded",
)

# 웅장한 우주 테마 CSS 스타일
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700;900&family=Noto+Serif+KR:wght@300;500;700&display=swap');

    .main {
        background: linear-gradient(180deg, #030712 0%, #0b0f19 50%, #111827 100%);
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
        font-size: 2.8rem;
        font-weight: 900;
        background: linear-gradient(135deg, #FFE259 0%, #FFA751 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.3rem;
        text-shadow: 0 0 25px rgba(255, 215, 0, 0.2);
    }
    .hero-subtitle {
        text-align: center;
        font-size: 1.05rem;
        color: #94a3b8;
        margin-bottom: 2rem;
        font-style: italic;
    }
    .myth-card {
        background: rgba(15, 23, 42, 0.85);
        border: 1px solid rgba(212, 175, 55, 0.35);
        border-radius: 16px;
        padding: 28px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6), inset 0 0 20px rgba(212, 175, 55, 0.05);
        backdrop-filter: blur(10px);
    }
    .gold-accent {
        color: #f1c40f;
        font-weight: 700;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# 헤더
st.markdown(
    "<div class='hero-title'>⚔️ ZODIAC MYTHS 🌌</div>", unsafe_allow_html=True
)
st.markdown(
    "<div class='hero-subtitle'>당신이 태어난 날 하늘을 수놓았던 황도 12궁 신화의 기록</div>",
    unsafe_allow_html=True,
)

# 황도 12궁 전체 데이터 및 SVG 성도
zodiac_data = {
    "양자리 (Aries)": {
        "start": (3, 21),
        "end": (4, 19),
        "element": "불 (Fire) / 수호성: 화성",
        "summary": "어린 남매를 구하기 위해 하늘을 날아오른 황금 털의 신성한 양",
        "story": "아카마스의 왕비 네펠레는 계모의 간계로 목숨이 위태로워진 자식들(프릭소스와 헬레)을 구하기 위해 전령의 신 헤르메스에게 도움을 청했습니다. 헤르메스는 하늘을 날 수 있는 **황금 털을 가진 양**을 보내 아이들을 태우고 안전한 곳으로 탈출시켰습니다. 훗날 제우스는 남매를 구한 이 용맹하고 헌신적인 양의 공로를 기려 밤하늘의 별자리로 새겼습니다.",
        "svg": """<svg viewBox="0 0 400 350" width="100%" height="300" xmlns="http://www.w3.org/2000/svg" style="background:#030712; border-radius:12px; border:1px solid #334155;"><polyline points="80,220 180,180 270,120 320,160" fill="none" stroke="#ef4444" stroke-width="2.5"/><circle cx="80" cy="220" r="5" fill="#ffffff"/><circle cx="180" cy="180" r="5" fill="#ffffff"/><circle cx="270" cy="120" r="9" fill="#f97316"/><circle cx="270" cy="120" r="16" fill="#f97316" fill-opacity="0.3"/><text x="250" y="95" fill="#f97316" font-size="12" font-weight="bold">Hamal (하말)</text><circle cx="320" cy="160" r="6" fill="#fef08a"/><text x="310" y="185" fill="#fef08a" font-size="11">Sheratan</text></svg>""",
    },
    "황소자리 (Taurus)": {
        "start": (4, 20),
        "end": (5, 20),
        "element": "흙 (Earth) / 수호성: 금성",
        "summary": "공주 에우로파에게 다가가기 위해 변신한 제우스의 아름다운 황소",
        "story": "제우스는 페니키아의 아름다운 공주 에우로파에 반해 눈처럼 하얗고 온순한 **황소**로 변신했습니다. 에우로파가 호기심에 황소 등 위에 올라타자, 황소는 바다를 가르며 크레타 섬까지 헤엄쳐 갔습니다. 크레타에서 본 모습을 드러내 사랑을 고백한 제우스는 이 위대한 변신과 사랑을 기념하여 하늘에 황소자리를 헌정했습니다.",
        "svg": """<svg viewBox="0 0 400 350" width="100%" height="300" xmlns="http://www.w3.org/2000/svg" style="background:#030712; border-radius:12px; border:1px solid #334155;"><polyline points="70,100 130,150 190,170 280,160 340,90" fill="none" stroke="#60a5fa" stroke-width="2" stroke-dasharray="4,2"/><polyline points="190,170 250,230 320,260" fill="none" stroke="#60a5fa" stroke-width="2" stroke-dasharray="4,2"/><polyline points="130,150 210,110 280,160" fill="none" stroke="#60a5fa" stroke-width="2" stroke-dasharray="4,2"/><circle cx="70" cy="100" r="5" fill="#fef08a"/><circle cx="190" cy="170" r="9" fill="#f97316"/><circle cx="190" cy="170" r="16" fill="#f97316" fill-opacity="0.3"/><text x="180" y="198" fill="#f97316" font-size="12" font-weight="bold">Aldebaran (알데바란)</text><circle cx="340" cy="90" r="5" fill="#fef08a"/><circle cx="320" cy="260" r="5" fill="#ffffff"/></svg>""",
    },
    "쌍둥이자리 (Gemini)": {
        "start": (5, 21),
        "end": (6, 21),
        "element": "공기 (Air) / 수호성: 수성",
        "summary": "죽음도 갈라놓지 못한 카스토르와 폴룩스 형제의 영원한 우애",
        "story": "우애 깊은 형제 **카스토르와 폴룩스** 중 카스토르가 전쟁에서 죽자, 신의 피를 물려받아 불사의 몸을 가졌던 폴룩스는 슬픔을 견디지 못하고 제우스에게 자신도 죽게 해달라고 간청했습니다. 이에 감동한 제우스는 형제가 하루의 절반은 이승에서, 절반은 하늘에서 함께할 수 있도록 두 사람을 별자리로 만들어주었습니다.",
        "svg": """<svg viewBox="0 0 400 350" width="100%" height="300" xmlns="http://www.w3.org/2000/svg" style="background:#030712; border-radius:12px; border:1px solid #334155;"><line x1="140" y1="80" x2="160" y2="270" stroke="#38bdf8" stroke-width="2"/><line x1="260" y1="90" x2="240" y2="280" stroke="#38bdf8" stroke-width="2"/><line x1="140" y1="80" x2="260" y2="90" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3,3"/><line x1="150" y1="170" x2="250" y2="180" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3,3"/><circle cx="140" cy="80" r="7" fill="#ffffff"/><text x="100" y="65" fill="#ffffff" font-size="11" font-weight="bold">Castor (카스토르)</text><circle cx="260" cy="90" r="8" fill="#fef08a"/><circle cx="260" cy="90" r="14" fill="#fef08a" fill-opacity="0.2"/><text x="270" y="95" fill="#fef08a" font-size="11" font-weight="bold">Pollux (폴룩스)</text></svg>""",
    },
    "게자리 (Cancer)": {
        "start": (6, 22),
        "end": (7, 22),
        "element": "물 (Water) / 수호성: 달",
        "summary": "친구 히드라를 돕기 위해 영웅 헤라클레스에게 집게발을 내던진 우직함",
        "story": "영웅 헤라클레스가 머리 아홉 개의 독사 히드라와 격렬한 전투를 벌일 때, 히드라의 친구였던 거대한 **게**가 히드라를 돕기 위해 늪지대에서 기어 나왔습니다. 게는 자신의 발이 밟혀 죽는 순간까지 집게발로 헤라클레스의 발가락을 찍으며 싸웠습니다. 여신 헤라는 이 무모하지만 의리 있는 게의 집념을 기려 하늘의 별자리로 올렸습니다.",
        "svg": """<svg viewBox="0 0 400 350" width="100%" height="300" xmlns="http://www.w3.org/2000/svg" style="background:#030712; border-radius:12px; border:1px solid #334155;"><polyline points="120,220 200,180 280,210" fill="none" stroke="#38bdf8" stroke-width="2"/><line x1="200" y1="180" x2="210" y2="100" stroke="#38bdf8" stroke-width="2"/><circle cx="120" cy="220" r="5" fill="#ffffff"/><circle cx="200" cy="180" r="7" fill="#38bdf8"/><circle cx="280" cy="210" r="5" fill="#ffffff"/><circle cx="210" cy="100" r="6" fill="#fef08a"/><text x="220" y="95" fill="#fef08a" font-size="11">Asellus Australis</text></svg>""",
    },
    "사자자리 (Leo)": {
        "start": (7, 23),
        "end": (8, 22),
        "element": "불 (Fire) / 수호성: 태양",
        "summary": "네메아 계곡을 호령하던 용맹한 맹수, 헤라클레스의 첫 과업",
        "story": "네메아 계곡의 사자는 어떤 칼이나 창으로도 뚫을 수 없는 단단한 가죽을 가진 무시무시한 맹수였습니다. 헤라클레스는 12가지 과업 중 첫 번째로 이 사자와 맨손 격투를 벌여 제압했습니다. 제우스는 사자의 강인함과 헤라클레스의 영웅적 승리를 영원히 기리기 위해 그 사자를 밤하늘의 별자리로 만들었습니다.",
        "svg": """<svg viewBox="0 0 400 350" width="100%" height="300" xmlns="http://www.w3.org/2000/svg" style="background:#030712; border-radius:12px; border:1px solid #334155;"><polyline points="280,100 250,70 200,80 180,120 210,160 260,160" fill="none" stroke="#f59e0b" stroke-width="2"/><polyline points="260,160 130,200 90,260 190,250 260,160" fill="none" stroke="#f59e0b" stroke-width="2"/><line x1="130" y1="200" x2="70" y2="180" stroke="#f59e0b" stroke-width="2" stroke-dasharray="3,3"/><circle cx="260" cy="160" r="9" fill="#38bdf8"/><circle cx="260" cy="160" r="16" fill="#38bdf8" fill-opacity="0.25"/><text x="275" y="165" fill="#38bdf8" font-size="12" font-weight="bold">Regulus (레굴루스)</text><circle cx="70" cy="180" r="6" fill="#fef08a"/><text x="35" y="170" fill="#fef08a" font-size="11">Denebola</text></svg>""",
    },
    "처녀자리 (Virgo)": {
        "start": (8, 23),
        "end": (9, 22),
        "element": "흙 (Earth) / 수호성: 수성",
        "summary": "인간이 악해진 타락의 시대에도 끝까지 지상을 지켰던 정의의 여신",
        "story": "신과 인간이 함께 살던 황금 시대가 지나고 인간들이 싸움과 탐욕에 빠지자 다른 신들은 모두 승천했습니다. 그러나 정의의 여신 아스트라이아(혹은 대지의 여신 데메테르의 딸 페르세포네)는 끝까지 지상에 남아 인간들에게 정의를 호소했습니다. 마침내 인간이 전쟁을 일삼자 그녀도 하늘로 올라가 처녀자리가 되었습니다.",
        "svg": """<svg viewBox="0 0 400 350" width="100%" height="300" xmlns="http://www.w3.org/2000/svg" style="background:#030712; border-radius:12px; border:1px solid #334155;"><polyline points="80,100 140,150 210,180 300,220" fill="none" stroke="#a855f7" stroke-width="2"/><polyline points="140,150 120,230 200,280" fill="none" stroke="#a855f7" stroke-width="2"/><line x1="210" y1="180" x2="200" y2="280" stroke="#a855f7" stroke-width="2"/><circle cx="200" cy="280" r="9" fill="#38bdf8"/><circle cx="200" cy="280" r="16" fill="#38bdf8" fill-opacity="0.25"/><text x="215" y="295" fill="#38bdf8" font-size="12" font-weight="bold">Spica (스피카)</text><circle cx="80" cy="100" r="5" fill="#ffffff"/><circle cx="300" cy="220" r="5" fill="#ffffff"/></svg>""",
    },
    "천칭자리 (Libra)": {
        "start": (9, 23),
        "end": (10, 23),
        "element": "공기 (Air) / 수호성: 금성",
        "summary": "인간의 선함과 악함을 공정하게 달아 측정하는 정의의 저울",
        "story": "정의의 여신 아스트라이아가 인간의 죄와 저울질할 때 사용하던 **정의의 저울**입니다. 인간이 죽은 후 사후세계로 가면 이 저울의 한쪽에는 사자의 영혼을, 다른 쪽에는 진실의 깃털을 올려놓아 선악을 엄격하게 심판했습니다. 정의가 바로 서기를 바라는 마음을 담아 처녀자리 바로 옆 밤하늘에 놓였습니다.",
        "svg": """<svg viewBox="0 0 400 350" width="100%" height="300" xmlns="http://www.w3.org/2000/svg" style="background:#030712; border-radius:12px; border:1px solid #334155;"><polygon points="200,80 120,180 280,180" fill="none" stroke="#fbbf24" stroke-width="2"/><line x1="120" y1="180" x2="100" y2="260" stroke="#fbbf24" stroke-width="2"/><line x1="280" y1="180" x2="300" y2="260" stroke="#fbbf24" stroke-width="2"/><circle cx="200" cy="80" r="6" fill="#ffffff"/><circle cx="120" cy="180" r="7" fill="#fef08a"/><text x="50" y="180" fill="#fef08a" font-size="11">Zubeneschamali</text><circle cx="280" cy="180" r="7" fill="#fef08a"/><text x="290" y="180" fill="#fef08a" font-size="11">Zubenelgenubi</text><circle cx="100" cy="260" r="5" fill="#ffffff"/><circle cx="300" cy="260" r="5" fill="#ffffff"/></svg>""",
    },
    "전갈자리 (Scorpio)": {
        "start": (10, 24),
        "end": (11, 22),
        "element": "물 (Water) / 수호성: 명왕성/화성",
        "summary": "자만했던 거인 사냥꾼 오리온을 제압한 치명적인 독침의 전갈",
        "story": "거인 사냥꾼 오리온이 '세상의 어떤 짐승도 나를 쓰러뜨릴 수 없다'고 자만하자, 신들의 여신 헤라는 오리온을 벌하기 위해 **치명적인 독전갈**을 보냈습니다. 전갈은 단 한 번의 독침 공격으로 오리온을 제압했습니다. 이 공로로 별자리가 된 전갈은 지금도 밤하늘에서 오리온자리가 떠오르면 반대편으로 지며 영원한 앙숙으로 남아있습니다.",
        "svg": """<svg viewBox="0 0 400 350" width="100%" height="300" xmlns="http://www.w3.org/2000/svg" style="background:#030712; border-radius:12px; border:1px solid #334155;"><path d="M 80,120 Q 150,150 180,180 T 260,250 T 320,200 T 300,160" fill="none" stroke="#ef4444" stroke-width="2.5"/><line x1="80" y1="120" x2="60" y2="80" stroke="#ef4444" stroke-width="2"/><line x1="80" y1="120" x2="100" y2="70" stroke="#ef4444" stroke-width="2"/><circle cx="180" cy="180" r="9" fill="#ef4444"/><circle cx="180" cy="180" r="16" fill="#ef4444" fill-opacity="0.3"/><text x="195" y="175" fill="#ef4444" font-size="12" font-weight="bold">Antares (안타레스)</text><circle cx="300" cy="160" r="6" fill="#fef08a"/><text x="310" y="150" fill="#fef08a" font-size="11">Shaula (독침)</text></svg>""",
    },
    "궁수자리 (Sagittarius)": {
        "start": (11, 23),
        "end": (12, 21),
        "element": "불 (Fire) / 수호성: 목성",
        "summary": "지혜와 무술을 겸비했던 현명한 반인반마 켄타우로스 케이론",
        "story": "켄타우로스족인 **케이론**은 야만적인 다른 동족들과 달리 지혜롭고 박학다식하여 아킬레우스, 헤라클레스 같은 수많은 영웅들의 스승이었습니다. 불행히도 헤라클레스가 쏜 독화살에 스쳐 불사의 고통을 겪게 되자, 그는 자신의 불사 능력을 프로메테우스에게 양도하고 안식을 택했습니다. 제우스는 그의 지혜를 찬양하며 활을 든 별자리로 새겼습니다.",
        "svg": """<svg viewBox="0 0 400 350" width="100%" height="300" xmlns="http://www.w3.org/2000/svg" style="background:#030712; border-radius:12px; border:1px solid #334155;"><polygon points="120,200 180,180 220,240 150,260" fill="none" stroke="#f97316" stroke-width="2"/><line x1="180" y1="180" x2="290" y2="100" stroke="#f97316" stroke-width="2.5"/><polyline points="260,90 290,100 280,130" fill="none" stroke="#f97316" stroke-width="2"/><circle cx="290" cy="100" r="7" fill="#ffffff"/><circle cx="180" cy="180" r="6" fill="#fef08a"/><text x="180" y="160" fill="#fef08a" font-size="11">Kaus Australis</text></svg>""",
    },
    "염소자리 (Capricorn)": {
        "start": (12, 22),
        "end": (1, 19),
        "element": "흙 (Earth) / 수호성: 토성",
        "summary": "괴물 티폰의 습격에 놀라 상반신은 염소, 하반신은 물고기로 변한 판 신",
        "story": "목신 **판(Pan)**이 신들의 연회에서 피리를 불며 즐기던 중, 무시무시한 거대 괴물 티폰이 나타났습니다. 놀란 신들은 동물로 변신해 도망쳤고, 판도 강에 뛰어들어 물고기로 변하려 했습니다. 하지만 너무 서두른 탓에 상반신은 염소, 하반신은 물고기 지느러미인 기묘한 모습이 되었고, 제우스는 이 유쾌하고 우스꽝스러운 모습을 별자리로 남겼습니다.",
        "svg": """<svg viewBox="0 0 400 350" width="100%" height="300" xmlns="http://www.w3.org/2000/svg" style="background:#030712; border-radius:12px; border:1px solid #334155;"><polygon points="90,120 220,100 310,180 240,260 140,220" fill="none" stroke="#10b981" stroke-width="2"/><line x1="90" y1="120" x2="140" y2="220" stroke="#10b981" stroke-width="2"/><circle cx="90" cy="120" r="6" fill="#fef08a"/><text x="50" y="115" fill="#fef08a" font-size="11">Algedi</text><circle cx="310" cy="180" r="7" fill="#ffffff"/><text x="320" y="185" fill="#ffffff" font-size="11">Deneb Algedi</text></svg>""",
    },
    "물병자리 (Aquarius)": {
        "start": (1, 20),
        "end": (2, 18),
        "element": "공기 (Air) / 수호성: 천왕성/목성",
        "summary": "신들의 연회장에서 영원한 생명의 신주를 따르는 미소년 가니메데",
        "story": "트로이의 왕자 **가니메데**는 세상에서 가장 아름다운 미소년이었습니다. 그 외모에 반한 제우스는 독수리로 변신해 가니메데를 올림포스 산으로 데려왔습니다. 가니메데는 올림포스 신들의 연회에서 영원한 청춘과 신주(Ambrosia)를 항아리에 담아 신들에게 따르는 역할을 맡게 되었고, 그 항아리가 밤하늘의 물병자리가 되었습니다.",
        "svg": """<svg viewBox="0 0 400 350" width="100%" height="300" xmlns="http://www.w3.org/2000/svg" style="background:#030712; border-radius:12px; border:1px solid #334155;"><polygon points="180,100 230,120 200,160 150,140" fill="none" stroke="#06b6d4" stroke-width="2"/><path d="M 200,160 Q 180,220 220,250 T 200,300" fill="none" stroke="#06b6d4" stroke-width="2" stroke-dasharray="4,2"/><path d="M 200,160 Q 220,220 250,250 T 240,300" fill="none" stroke="#06b6d4" stroke-width="2" stroke-dasharray="4,2"/><circle cx="180" cy="100" r="6" fill="#ffffff"/><circle cx="230" cy="120" r="7" fill="#06b6d4"/><text x="245" y="125" fill="#06b6d4" font-size="11">Sadalmelik</text></svg>""",
    },
    "물고기자리 (Pisces)": {
        "start": (2, 19),
        "end": (3, 20),
        "element": "물 (Water) / 수호성: 해왕성/목성",
        "summary": "위험 속에서도 서로를 놓지 않기 위해 끈으로 꼬리를 묶은 아프로디테와 에로스",
        "story": "미의 여신 **아프로디테**와 그녀의 아들 **에로스**가 유프라테스 강가에서 거닐던 중, 괴물 티폰이 기습했습니다. 놀란 모자는 물고기로 변신해 강물 속으로 헤엄쳐 도망쳤습니다. 이때 거센 물살 속에서 서로를 놓치지 않기 위해 어머니와 아들은 끈으로 서로의 꼬리를 묶었습니다. 이 따뜻한 모성애의 끈이 밤하늘의 별자리로 새겨졌습니다.",
        "svg": """<svg viewBox="0 0 400 350" width="100%" height="300" xmlns="http://www.w3.org/2000/svg" style="background:#030712; border-radius:12px; border:1px solid #334155;"><path d="M 100,150 Q 200,260 280,130" fill="none" stroke="#6366f1" stroke-width="2"/><circle cx="100" cy="150" r="15" fill="none" stroke="#6366f1" stroke-width="1.5"/><circle cx="280" cy="130" r="18" fill="none" stroke="#6366f1" stroke-width="1.5"/><circle cx="200" cy="225" r="7" fill="#fef08a"/><text x="180" y="250" fill="#fef08a" font-size="11">Alrescha (리본 매듭)</text></svg>""",
    },
}


# 날짜로 별자리 찾는 함수
def get_zodiac(month, day):
    for name, data in zodiac_data.items():
        s_m, s_d = data["start"]
        e_m, e_d = data["end"]

        # 12월 ~ 1월 예외 처리 (염소자리)
        if s_m > e_m:
            if (month == s_m and day >= s_d) or (month == e_m and day <= e_d):
                return name
        else:
            if (month == s_m and day >= s_d) or (
                month == e_m and day <= e_d
            ) or (s_m < month < e_m):
                return name
    return "양자리 (Aries)"


# 사이드바: 생일 입력 받기
with st.sidebar:
    st.markdown("### 🎂 생일 입력하기")
    birth_date = st.date_input(
        "당신의 생일을 선택해주세요:",
        value=date(2000, 1, 1),
        min_value=date(1900, 1, 1),
        max_value=date(2026, 12, 31),
    )

    found_zodiac = get_zodiac(birth_date.month, birth_date.day)

    st.markdown("---")
    st.markdown("### 📜 직접 수동 선택")
    selected_name = st.selectbox(
        "다른 별자리 찾아보기:",
        list(zodiac_data.keys()),
        index=list(zodiac_data.keys()).index(found_zodiac),
    )

selected_data = zodiac_data[selected_name]

# 메인 레이아웃 (2컬럼)
col1, col2 = st.columns([1.1, 0.9], gap="large")

with col1:
    st.markdown(
        f"""
        <div class='myth-card'>
            <div style='color: #94a3b8; font-size: 0.9rem;'>{birth_date.strftime('%m월 %d일')} 생일의 수호 별자리</div>
            <h2 style='color: #f1c40f; margin-top: 5px; margin-bottom: 15px;'>{selected_name}</h2>
            <p><span class='gold-accent'>🗓️ 수호 기간:</span> {selected_data['start'][0]}월 {selected_data['start'][1]}일 ~ {selected_data['end'][0]}월 {selected_data['end'][1]}일</p>
            <p><span class='gold-accent'>✨ 별자리 속성:</span> {selected_data['element']}</p>
            <hr style='border-color: rgba(212,175,55,0.2); margin: 20px 0;'>
            <h4 style='color: #e2e8f0; line-height: 1.4;'>“{selected_data['summary']}”</h4>
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
        "<h3 style='text-align: center; color: #93c5fd; margin-bottom: 15px;'>🌌 CONSTELLATION MAP</h3>",
        unsafe_allow_html=True,
    )
    st.markdown(selected_data["svg"], unsafe_allow_html=True)
    st.caption("※ 성도에서 밝게 빛나는 알파성(주요 별)의 이름이 표시됩니다.")

st.markdown("<br><hr style='border-color: #1e293b;'><br>", unsafe_allow_html=True)
st.info(
    "💡 **Tip:** 왼쪽 사이드바 달력에서 생일을 바꾸면 자동으로 당신만의 별자리와 신화 이야기가 짜잔 나타납니다!"
)
