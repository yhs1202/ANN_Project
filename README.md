# Implementation of Korean Sign Language Translation Model with MediaPipe

Aihub에서 제공하는 [길찾기, 교통, 주소 등과 관련된 지문자 한국수어 영상](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=103)을 바탕으로 데이터셋을 구축하고, MediaPipe를 적용해 손 관절의 좌표 값을 학습하는 모델입니다.

##  Installation

### 1. Clone this repository

```
$ git clone https://github.com/yhs1202/ANN_Project
```

### 2. Create your own keras venv (conda / python venv)
</br>

### 3. Install dependencies

```
pip install -r requirements.txt
```

## Collecting Datasets
---
```
dataset (6600 images) (train:5940 / test:660)
│ 
├── 자음 (300*14 = 4200 images)
│   ├── ㄱ (300 images)
│   │   ├── image1.jpg
│   │   ├── image2.jpg
│   │   └── ...
│   ├── ㄴ (300 images)
│   │   ├── image1.jpg
│   │   ├── image2.jpg
│   │   └── ...
│   ├── ㄷ (300 images)
│   │   ├── image1.jpg
│   │   ├── image2.jpg
│   │   └── ...
│   └── ...
└── 모음 (200*12 = 2400 images)
    ├── ㅏ (200 images)
    │   ├── image1.jpg
    │   ├── image2.jpg
    │   └── ...
    ├── ㅑ (200 images)
    │   ├── image1.jpg
    │   ├── image2.jpg
    │   └── ...
    ├── ㅓ (200 images)
    │   ├── image1.jpg
    │   ├── image2.jpg
    │   └── ...
    └── ...
```

<img width="745" alt="1" src="https://github.com/yhs1202/ANN_Project/assets/50286291/8dc69f0a-2e64-4842-a628-ced09c8b7903"> 

</br>

![2](https://github.com/yhs1202/ANN_Project/assets/50286291/99dcf612-a2c2-4f30-b688-4517f1c26652)

</br>

![3](https://github.com/yhs1202/ANN_Project/assets/50286291/d4d7227d-aafa-4ceb-8bd1-ff7fdc1a5e16)

</br>

<img width="313" alt="6" src="https://github.com/yhs1202/ANN_Project/assets/50286291/00e46ee1-21dd-4744-8a21-227ab9f7fae2">

</br>

<img width="634" alt="123" src="https://github.com/yhs1202/ANN_Project/assets/50286291/f06fdc82-5846-4c3a-861e-11405235a677">

</br></br></br>

- ### Example with 3 images

<img width="822" alt="4" src="https://github.com/yhs1202/ANN_Project/assets/50286291/15bcf876-0d82-44d0-995e-4b7a3af7119e">

</br>

<img width="1325" alt="5" src="https://github.com/yhs1202/ANN_Project/assets/50286291/b87db200-fabf-4377-a527-8b6be4039ea1">

</br></br></br>

- ### 2023-06-07 데이터 확보 상태

<img width="682" alt="234" src="https://github.com/yhs1202/ANN_Project/assets/50286291/60ceb4f9-09d9-458d-a5a4-b58a35697260">

</br></br>

## Results
---
![제목 없음](https://github.com/user-attachments/assets/b7d048ab-fbc4-4965-8433-22d118bde277)


