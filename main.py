from typing import Optional
from fastapi import FastAPI
import requests

app = FastAPI()

# session global عشان ما نعيد تهيئتها كل مرة
session = requests.Session()
session.headers.update({
    "User-Agent": "Instagram 275.0.0.27.98 Android (29/10; 320dpi; 720x1369; Xiaomi; Redmi 8A; olivelite; qcom; en_US; 458229237)"
})

TARGET_URL = "https://i.instagram.com/api/v1/users/check_username/"

@app.get("/")
async def root():
    return {"message": "API is running 🚀"}

@app.get("/check/")
def check_username(username: str):
    """
    param: username -> يجي من اليوزر
    """
    payload = {
        "signed_body": f'SIGNATURE.{{"is_group_creation":"false","username":"{username}","_uuid":"48041674-e663-4131-8f5b-428c4896cbbe"}}'
    }

    try:
        resp = session.post(TARGET_URL, data=payload)
        return resp.json()  # يرجع JSON مباشر
    except Exception as e:
        return {"error": str(e)}
