# Gunakan image Python resmi
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Salin file aplikasi ke dalam container
COPY app.py /app
COPY model.pkl /app

# Install dependensi yang dibutuhkan
RUN pip install --no-cache-dir Flask joblib scikit-learn

# Tentukan port yang digunakan
EXPOSE 8080

# Jalankan aplikasi Flask
CMD ["python", "app.py"]
