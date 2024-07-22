# vending-ai-2024
2024년 대학생 Deep Learning 기반 무인판매대 상품인식 인공지능 경진대회  


## Info
darknet 프레임워크와 yolo v3을 이용하여 무인판매대 내 상품의 변동사항을 인식하여 실시간 재고를 예측하는 프로그램


## Run Programe
```shell
pip install -r requirements.txt
python3 main.py
```


## Workflow
1. 데이터 분류
2. 학습, weight 파일 생성
3. 각 카메라의 프레임별 테스트 결과 예측
4. 각 카메라의 테스트 결과 하나로 취합, 상품 변동사항 예측
5. 프레임별 상품 재고 csv 파일로 저장


## ETC

### 대회 소개
https://www.disu.ac.kr/LOCnLOS/AIX/notice?md=v&bbsidx=7747  

### 차세대반도체 혁신융합대학
https://www.disu.ac.kr  


## Team
|Name|역할|
|---|---|
|[castberry](https://github.com/castberry10)|데이터 라벨링 및 AI 학습|
|[Mule1291](https://github.com/Mule129)|무인판매대 Programe algoream 제작|
|[bolbot](https://github.com/bb2002)|보고서 작성|