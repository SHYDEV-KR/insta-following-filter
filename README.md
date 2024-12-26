# Instagram Profile Filter Tool

인스타그램 프로필을 필터링하고 선택할 수 있는 Streamlit 웹 애플리케이션입니다.

## 설치 방법

1. 가상환경 생성 및 활성화:
```bash
python -m venv .venv
source .venv/bin/activate  # Mac/Linux
# or
.venv\Scripts\activate  # Windows
```

2. 의존성 설치:
```bash
pip install -r requirements.txt
```

## 실행 방법

```bash
streamlit run app.py
```

## 사용 방법

1. 웹 브라우저에서 애플리케이션이 실행됩니다
2. JSON 형식의 데이터를 텍스트 영역에 붙여넣습니다
3. 각 프로필을 확인하고 체크박스로 선택합니다
4. 선택된 사용자 이름 목록이 하단에 표시됩니다

## 입력 데이터 형식

JSON 데이터는 다음과 같은 형식이어야 합니다:
```json
[
    {
        "username": "사용자이름",
        "src": "프로필_이미지_URL"
    },
    ...
]
``` 