
---![olav-tvedt--oVaYMgBMbs-unsplash](https://user-images.githubusercontent.com/105832393/172632213-cc056e7a-c0a8-4f36-93b2-853dbc7a86d4.jpg)



# 자동차 가격 예측 앱

< 자동차 가격을 예측할 수 있는 앱 >

이 앱은 자동차 가격을 성별과 월급 등으로 유추하여 정보를 예측 할 수 있는 앱 입니다.
메뉴 -> HOME은 대쉬보드의 메인화면으로, 사진과 간략한 소개를 넣었다.
메뉴 -> EDA는 데이터프레임과 통계치를 나타내었다.
메뉴 -> ML은 머신러닝으로, 성별,월급등으로 선호하는 차종을 유추할 수 있는 인공지능 데이터이다.

    - app.py : 실행을 위한 메인 파일
    - app_home.py : 앱 실행시 가장 먼저 보여질 홈
    - app_eda.py : 데이터를 분석하여 차트 출력
    - app_ml.py : 분석한 데이터를 이용하여 인공지능 예측
    - data 폴더 : 앱 실행시 필요한 추가 파일
    - train.csv : 데이터셋
    - car.jpg : 홈화면에서 보여질 이미지 파일
    
# Pre-requisite
- Library
``` phtyon
pip install streamlit-option-menu
```

# Connect URL
http://ec2-3-39-177-185.ap-northeast-2.compute.amazonaws.com:8501/


