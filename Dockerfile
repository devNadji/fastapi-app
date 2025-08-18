# نبدأ من صورة Python خفيفة
FROM python:3.10-slim

# نحدد مجلد العمل داخل الحاوية
WORKDIR /app

# ننسخ ملف المتطلبات أولاً ونثبت المكتبات
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ننسخ باقي ملفات المشروع
COPY . .

# نفتح البورت 8000 (اللي FastAPI يشتغل عليه)
EXPOSE 8000

# نشغّل التطبيق بـ Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
