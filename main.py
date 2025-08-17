from typing import Optional
from fastapi import FastAPI
import requests, random

app = FastAPI()

# session global عشان ما نعيد تهيئتها كل مرة
session = requests.Session()
session.headers.update({
    "User-Agent": "Instagram 275.0.0.27.98 Android (29/10; 320dpi; 720x1369; Xiaomi; Redmi 8A; olivelite; qcom; en_US; 458229237)"
})
f = [
    "https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/", ###
    "https://i.instagram.com/api/v1/accounts/create_business/", ####
    "https://i.instagram.com/api/v1/users/check_username/", ##
    "https://www.instagram.com/api/v1/users/check_username/" ###
]


@app.get("/")
async def root():
    return {"message": "API is running 🚀"}

@app.get("/check/")
def check_username(username: str):
    """
    param: username -> يجي من اليوزر
    """
    payload = {
        "username": username,
    }
    TARGET_URL = random.choice(f)
    try:
        resp = session.post(TARGET_URL, data=payload)
        return resp.json()  # يرجع JSON مباشر
    except Exception as e:
        return {"error": str(e)}
