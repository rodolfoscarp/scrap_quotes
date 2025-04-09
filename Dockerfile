FROM python:3.12-slim-bookworm

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    wget \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


RUN wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    xdg-utils \
    libx11-6 \
    libxcb1 \
    libxcomposite1 \
    libxcursor1 \
    libxdamage1 \
    libxext6 \
    libxfixes3 \
    libxi6 \
    libxrandr2 \
    libxrender1 \
    libxss1 \
    libxtst6 \
    ca-certificates \
    fonts-liberation \
    libappindicator1 \
    libnspr4 \
    libnss3 \
    lsb-release \
    xdg-utils 

RUN apt-get install -y ./google-chrome-stable_current_amd64.deb \ 
    ||apt-get install -y -f \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY requirements.txt .
COPY src/ ./src/
COPY .env .
COPY main.py .

RUN ls -lR /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]