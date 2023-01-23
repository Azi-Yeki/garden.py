FROM python:3.10
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN python -m spacy download en_core_web_sm
WORKDIR /app
COPY . /app
CMD python garden.py