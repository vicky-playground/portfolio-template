# app/Dockerfile

FROM python:3.8

WORKDIR /portfolio-template

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY . . 

# copy over requirements
COPY requirements.txt ./requirements.txt

RUN python3.8 install -r requirements.txt

EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "1_🏠_Home.py", "--server.port=8501", "--server.address=0.0.0.0"]
