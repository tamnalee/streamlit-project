from numpy import imag
import streamlit as st
from app_home import run_home
from app_eda import run_eda
from app_ml import run_ml
from PIL import Image
from streamlit_option_menu import option_menu

def main():
    st.title('자동차 가격을 예측할 수 있는 앱')
    with st.sidebar:
        choice = option_menu("MENU", ['HOME','EDA','ML'],
                            icons=['house-fill', 'file-bar-graph-fill','gear-fill'],
                            menu_icon="app-indicator", default_index=0,
                            styles={
            "container": {"padding": "5!important", "background-color": "#fafafa"},
            "icon": {"color": "orange", "font-size": "25px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#02ab21"},
        }
        )


    if choice == 'HOME':
        run_home()
    elif choice == 'EDA':
        run_eda()
    elif choice == 'ML':
        run_ml()


if __name__ == '__main__':
    main()
