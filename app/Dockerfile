FROM python:3.11-slim

RUN useradd -m appuser
WORKDIR /home/appuser/app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN chown -R appuser:appuser /home/appuser
USER appuser

EXPOSE 5000
CMD ["python", "main.py"]