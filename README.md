# 자동차 가격 예측 앱

< 자동차 가격을 예측할 수 있는 앱 >

이 앱은 자동차 가격을 성별과 월급 등으로 유추하여 정보를 예측 할 수 있는 앱 입니다.
메뉴 -> HOME은 대쉬보드의 메인화면으로, 사진과 간략한 소개를 넣었다.
메뉴 -> EDA는 데이터프레임과 통계치를 나타내었다.
메뉴 -> ML은 머신러닝으로, 성별,월급등으로 선호하는 차종을 유추할 수 있는 인공지능 데이터이다.

# Overview
- 날짜와 날씨, 여러가지 환경이 기입된 자전거 대여량의 데이터를 포함하고 있습니다.
- 데이터는 매 시간주기로 기록이 되어있습니다.
- 스케일러와 인공지능 모델은 pkl 파일화하여 진행하였습니다.
- 해당 깃허브에는 pkl 파일이 내포되어있지 않기 때문에 깃허브의 파일만으로는 정상적인 실행이 되지 않음을 알려드립니다.

# Repository File Structure
![file_dir](https://user-images.githubusercontent.com/105832446/172329301-f29efdcf-2db2-4197-ad78-bb0d201e6444.png)

- app.py : 실행을 위한 메인 파일
    - app_home.py : 앱 실행시 가장 먼저 보여질 홈
    - app_eda.py : 데이터를 분석하여 차트 출력
    - app_ml.py : 분석한 데이터를 이용하여 인공지능 예측
- data 폴더 : 앱 실행시 필요한 추가 파일
    - train.csv : 데이터셋
    - bike_img01.png : 사이드바에 보여질 이미지 파일
    - bike_img02.png : 홈화면에서 보여질 이미지 파일
    
# Pre-requisite
- Library
``` phtyon
pip install streamlit-option-menu
```
- File
    - RF_Model : https://drive.google.com/file/d/1--XZYxNSMiFs4N4QdiLL_4JOTqDvfSDz/view?usp=sharing
    - X_Scaler : https://drive.google.com/file/d/1gTozcZZiKaXFTZInbuUgQ0e_0TaXlZAd/view?usp=sharing
    - y_Scaler : https://drive.google.com/file/d/1-4WCYnV3eBWWTeMzXgoI6O6IKbSz6WMb/view?usp=sharing

# Dataset
**Kaggle Competitions**  
Bike Sharing Demand - Forecast use of a city bikeshare system  
https://www.kaggle.com/competitions/bike-sharing-demand/data

# Dataset Columns Detail
- datetime : 날짜와 시간
- season : 계절 (1:봄, 2:여름, 3:가을, 4:겨울
- holiday : 공휴일 여부 (0:평일, 1:공휴일)
- workingday : 평일 여부 (0:휴일, 1:평일)
- weather : 날씨 (1:맑음, 2:흐림, 3:이슬비, 4:호우)
- temp : 온도
- atemp : 체감온도
- humidity : 습도
- windspeed : 풍속
- casual : 미등록 회원 대여 횟수
- registered : 등록 회원 대여 횟수
- count : 총 대여 횟수

# Feature Engineering - Datetime
- 세밀한 데이터 분석을 위해 날짜와 시간을 분리
``` python
train['year'] = train['datetime'].dt.year
train['month'] = train['datetime'].dt.month
train['day'] = train['datetime'].dt.day
train['hour'] = train['datetime'].dt.hour
train["dayofweek"] = train["datetime"].dt.dayofweek
def concatenate_year_month(datetime):
    return "{0}-{1}".format(datetime.year, datetime.month)
train["year_month"] = train["datetime"].apply(concatenate_year_month)
```

# Drop X(Train) Data
  - datetime : 피쳐 엔지니어링을 통해 날짜와 시간을 분리
  - year_month : 연도, 월 컬럼이 단독으로 존재
  -  day : working day, holiday 이용
  - count : 결과값이므로 y 변수에 대입

# Split Data - X(train data), y(test data)
- X = 학습시킬 데이터
- y = count(대여량) 컬럼
- test size : 25%
- X의 데이터에서 필요없는 컬럼 삭제(datetime, year_month, count, day)
``` python
X = train
X.drop(['datetime','year_month','count','day'], axis=1)
y = train['count']
y = y.to_frame()
```

# Feature Scaling
- Using Scaler : Standard Scaler
- Apply Variable : X, y

# Machine Learning
- Using Model : Random Forest Regression

# Connect URL
http://ec2-3-35-209-81.ap-northeast-2.compute.amazonaws.com:8502