FROM python:3.11-slim

# Install security updates
RUN apt-get update && apt-get upgrade -y && apt-get clean

WORKDIR /app

RUN pip install Flask
RUN pip install gunicorn

COPY . .

EXPOSE 3000

CMD ["gunicorn", "-w", "1", "-b", "0.0.0.0:3000", "--access-logfile", "-", "--error-logfile", "-", "app:app"]