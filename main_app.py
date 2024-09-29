import streamlit as st
from movie_utils import search_movies, load_css

# เรียกใช้ CSS จากไฟล์แยก
load_css("static/style.css")

# ส่วนหัวของเว็บ
st.title("Movie Recommender")

# ส่วนสำหรับใส่ชื่อหนังและปุ่ม search
movie_query = st.text_input("Enter movie name", "")
search_button = st.button("Search")

# เมื่อกด search
if search_button and movie_query:
    # ดึงข้อมูลหนังจากฟังก์ชัน search_movies
    movies = search_movies(movie_query)

    # แสดงรายการหนัง
    st.markdown('<div class="movie-container">', unsafe_allow_html=True)
    
    for movie in movies:
        st.markdown(
            f"""
            <div class="movie-item">
                <p class="movie-title">{movie['title']}</p>
                <img src="{movie['poster_url']}" alt="{movie['title']}">
            </div>
            """, 
            unsafe_allow_html=True
        )
    
    st.markdown('</div>', unsafe_allow_html=True)
