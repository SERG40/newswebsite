FROM python:3.10
RUN mkdir /newswebsite
COPY . /newswebsite
WORKDIR /newswebsite
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8000
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
