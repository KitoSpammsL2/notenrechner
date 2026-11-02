FROM python:3.13-slim

LABEL org.opencontainers.image.source="https://github.com/KitoSpammsL2/notenrechner"

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN useradd --create-home app && chown -R app /app
USER app

EXPOSE 8000

CMD ["gunicorn", "--bind=0.0.0.0:8000", "main:app"]
