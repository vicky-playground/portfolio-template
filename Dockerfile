FROM tiangolo/uwsgi-nginx-flask:python3.10

RUN groupadd -r myuser && useradd -r -g myuser myuser

USER root 

COPY requirements.txt portfolio-template/requirements.txt
RUN pip install -r portfolio-template/requirements.txt

WORKDIR /portfolio-template
COPY . /1_🏠_Home

EXPOSE 8501

ENTRYPOINT ["streamlit", "run"]

CMD ["1_🏠_Home.py"]

USER myuser
