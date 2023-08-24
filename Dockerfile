FROM python:3.7
LABEL key="swamy877@gmail.com"
USER root
WORKDIR /app/
COPY * /app/
RUN pwd && ls -lrta
RUN pip3 install --no-cache-dir -r requirements.txt
EXPOSE 8000
CMD ["python","manage.py","runserver","0.0.0.0:8000"]
