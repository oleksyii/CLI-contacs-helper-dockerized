FROM python:3.10-alpine

# Встановимо змінну середовища
ENV APP_HOME /app

# Встановимо робочу директорію всередині контейнера
WORKDIR $APP_HOME

COPY . .

RUN apk update && apk add bash

# To run w/ poetry
# RUN pip3 install poetry

# RUN poetry install

# To run w/ requirements.txt
RUN pip3 install -r requirements.txt

# CMD ["poetry", "run", "python3", "main.py"]
# RUN ["python3", "main.py"]
CMD ["python3", "main.py"]