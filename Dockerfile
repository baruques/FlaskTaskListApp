FROM python:3.11-slim-bookworm

# Install security updates and remove unnecessary files
RUN apt-get update && \
	apt-get upgrade -y && \
	apt-get dist-upgrade -y && \
	apt-get install --only-upgrade -y libexpat1 libssl3 && \
	apt-get autoremove -y && \
	apt-get clean && \
	rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN pip install Flask
RUN pip install gunicorn

COPY . .

EXPOSE 3000

CMD ["gunicorn", "-w", "1", "-b", "0.0.0.0:3000", "--access-logfile", "-", "--error-logfile", "-", "app:app"]