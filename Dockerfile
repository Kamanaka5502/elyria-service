# ---- Base image ----
FROM python:3.13-slim

# ---- Working directory ----
WORKDIR /app

# ---- Copy files ----
COPY . .

# ---- Install dependencies ----
RUN pip install --no-cache-dir -r requirements.txt

# ---- Expose port and launch ----
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
