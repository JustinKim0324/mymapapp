import streamlit as st
import folium
from streamlit_folium import st_folium

# 도쿄 관광지 및 맛집 데이터
places = [
    {
        "name": "신주쿠 교엔",
        "location": [35.6852, 139.7100],
        "description": "도쿄 중심의 아름다운 정원과 공원. 벚꽃 명소로 유명.",
        "restaurant": {
            "name": "후우운지 라멘",
            "location": [35.6879, 139.7015],
            "description": "츠케멘 맛집으로 유명한 라멘집."
        }
    },
    {
        "name": "센소지(아사쿠사)",
        "location": [35.7148, 139.7967],
        "description": "도쿄에서 가장 오래된 절로 아사쿠사의 상징.",
        "restaurant": {
            "name": "아사쿠사 규카츠",
            "location": [35.7127, 139.7956],
            "description": "겉은 바삭, 속은 부드러운 규카츠로 유명한 맛집."
        }
    },
    {
        "name": "시부야 스크램블 교차로",
        "location": [35.6595, 139.7006],
        "description": "세계적으로 유명한 시부야의 대표적인 교차로.",
        "restaurant": {
            "name": "스시노미도리",
            "location": [35.6586, 139.7015],
            "description": "가성비 좋은 스시로 유명한 곳."
        }
    }
]

# Streamlit 앱 구성
st.title("🇯🇵 도쿄 관광 명소 및 맛집 추천")
st.markdown("한국인들이 좋아하는 도쿄의 관광 명소 3곳과 꼭 먹어야 할 맛집을 추천합니다.")

# Folium 지도 생성
m = folium.Map(location=[35.6828, 139.759], zoom_start=12)

# 관광 명소 및 맛집 마커 추가
for place in places:
    # 관광지 마커 추가
    folium.Marker(
        location=place["location"],
        popup=f"<b>{place['name']}</b><br>{place['description']}",
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(m)

    # 맛집 마커 추가
    folium.Marker(
        location=place["restaurant"]["location"],
        popup=f"<b>{place['restaurant']['name']}</b><br>{place['restaurant']['description']}",
        icon=folium.Icon(color="red", icon="cutlery", prefix='fa')
    ).add_to(m)

# 지도를 Streamlit 앱에 표시
st_folium(m, width=700, height=500)
