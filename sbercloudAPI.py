import requests


BASE_API_URL = 'https://api.aicloud.sbercloud.ru/public/v1/public_inference'
PREDICT_URL = "/gpt3/predict"


def get_answer(message: str):
    res = requests.post(f"{BASE_API_URL}{PREDICT_URL}", json={
        "text": message
    })
    if res.status_code == 200:
        return res.json().get("predictions")
    elif res.status_code == 422:
        return res.json().get("detail").get("msg")
    else:
        return None
