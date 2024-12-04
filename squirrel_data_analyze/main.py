import pandas as pd
import folium


file_path = "/Users/siyun/Library/CloudStorage/OneDrive-개인/Programming/python/squirrel_data_analyze/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"
squirrel_data = pd.read_csv(file_path)

# 색깔별 다람쥐 수 분석
grouped_by_color = squirrel_data.groupby("Primary Fur Color")
for color, data in grouped_by_color:
    print(f" Color : {color}, Count : {len(data)} ")

# 시간대별 다람쥐 관찰빈도 분석
grouped_by_time = squirrel_data.groupby("Shift")
for time, data in grouped_by_time:
    print(f"Time : {time}, Count : {len(data)}")

# 나이별 분포 분석
grouped_by_age = squirrel_data.groupby("Age")
for age, data in grouped_by_age:
    print(f"Age : {age}, Count :{len(data)}")

# Age가 ? 인 경우의 ID 찾기
age_unknown = squirrel_data[squirrel_data["Age"] == "?"]
unique_ids = age_unknown["Unique Squirrel ID"]
for squirrel_id in unique_ids:
    print(squirrel_id)

# 행동분석
# Folium 지도 생성 (중심 좌표 설정)
center_latitude = squirrel_data['Y'].mean()
center_longitude = squirrel_data['X'].mean()
squirrel_map = folium.Map(location=[center_latitude, center_longitude], zoom_start=14)

# 지도에 각 다람쥐 위치 추가
for index, row in squirrel_data.iterrows():
    latitude = row['Y']
    longitude = row['X']
    folium.Marker(
        location=[latitude, longitude],
        popup=f"Squirrel ID: {row['Unique Squirrel ID']}",
        icon=folium.Icon(color="red", icon="info-sign")
    ).add_to(squirrel_map)

# 지도를 HTML 파일로 저장
squirrel_map.save("squirrel_map.html")

print("지도 생성 완료! 'squirrel_map.html' 파일을 열어보세요.")


'''
### 2. **중급 데이터 분석**  
- **위치 기반 분석**:
  - 다람쥐의 GPS 좌표(`X`, `Y`)를 사용해 공원 내 관찰 위치를 시각화.

- **희귀 데이터 분석**:
  - `Highlight Fur Color`와 같이 관찰 데이터가 적은 특성을 탐구.

---

### 3. **시각화 프로젝트**
- **히스토그램**:
  - 색깔별 다람쥐 수, 나이별 다람쥐 수 등의 데이터를 히스토그램으로 시각화.

- **파이차트**:
  - 다람쥐 행동 분포를 파이차트로 표현.

- **지리적 데이터 시각화**:
  - `folium` 라이브러리를 사용해 다람쥐 관찰 위치를 지도 위에 표시.

---

### 4. **데이터 처리 및 전처리**
- **결측치 처리**:
  - 데이터에서 누락된 값(`NaN`)을 처리하는 방법 배우기.

- **필터링**:
  - 특정 조건(예: Gray 색상 다람쥐만, AM 시간대만)에 해당하는 데이터를 필터링.

- **데이터 저장**:
  - 특정 조건에 맞는 데이터를 새로운 CSV 파일로 저장.

---

### 5. **Python 학습에 적합한 과제**
- **함수 활용**:
  - 예를 들어, 색깔별 다람쥐 수를 계산하는 함수 작성.

- **클래스 생성**:
  - 다람쥐 관찰 데이터를 객체로 관리하는 클래스 설계.

- **파일 입출력**:
  - 데이터를 파일로 읽고, 필요한 결과를 다른 파일에 저장.

---

### 6. **프로젝트 아이디어**
- **공원 내 다람쥐의 행동 지도 만들기**:
  - 다람쥐 행동 데이터를 바탕으로 행동 유형별 밀도를 지도에 표현.
  
- **관찰 데이터 통계 요약 보고서 생성**:
  - Python으로 자동 보고서 생성(Summary: 색깔, 행동, 위치 등).

- **모델링과 예측**:
  - 간단한 머신러닝 모델로 공원 내 특정 시간에 다람쥐 관찰 가능성을 예측(예: AM/PM 데이터 사용).

---

### 7. **Python 패키지 활용**
- `matplotlib` 또는 `seaborn`: 데이터 시각화.
- `numpy`: 통계적 계산.
- `folium`: 지도 시각화.
- `scikit-learn`: 간단한 모델링 및 예측.

---
😊'''