import json
import streamlit as st

# ฟังก์ชันโหลด CSS จากไฟล์
def load_css(css_file_path):
    with open(css_file_path, encoding="utf-8") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


# ฟังก์ชันค้นหาหนัง (สามารถปรับให้ใช้ API จริงได้)
def search_movies(query):
    # ในกรณีที่คุณต้องการใช้ไฟล์ JSON เก็บข้อมูลหนัง
    with open('data/movies.json', 'r') as f:
        all_movies = json.load(f)
    
    # สมมุติว่าค้นหาชื่อหนังในข้อมูลที่มี
    matching_movies = [
        movie for movie in all_movies if query.lower() in movie['title'].lower()
    ]
    
    return matching_movies[:10]  # แสดงแค่ 10 อันดับแรก
