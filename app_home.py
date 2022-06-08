import streamlit as st
from PIL import Image
import streamlit as st
import base64

def run_home():
    st.subheader('이 앱은 고객 데이터와 자동차 구매에 대한 내용을 담고 있습니다.')
    st.text('MENU에서 원하는 정보를 얻을 수 있습니다.')

    img = Image.open('data/car.jpg')
    st.image(img,use_column_width=True)


   

    # main_bg = "car.jpg"
    # main_bg_ext = "jpg"

    # side_bg = "car.jpg"
    # side_bg_ext = "jpg"

    # st.markdown(
    #     f"""
    #     <style>
    #     .reportview-container {{
    #         background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "car.jpg").read()).decode()})
    #     }}
    # .sidebar .sidebar-content {{
    #         background: url(data:image/{side_bg_ext};base64,{base64.b64encode(open(side_bg, "car.jpg").read()).decode()})
    #     }}
    #     </style>
    #     """,
    #     unsafe_allow_html=True
    # )
