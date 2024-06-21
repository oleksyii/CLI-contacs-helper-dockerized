FROM python:3.10

# Встановимо змінну середовища
ENV APP_HOME /app

# Встановимо робочу директорію всередині контейнера
WORKDIR $APP_HOME

COPY . .

RUN pip3 install poetry

RUN poetry install

CMD ["poetry", "run", "python3", "main.py"]