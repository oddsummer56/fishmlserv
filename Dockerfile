FROM datamario24/isdomi:0.8.3

WORKDIR /code

COPY src/fishmlserv/main.py /code/

RUN pip install --no-cache-dir --upgrade git+https://github.com/oddsummer56/fishmlserv.git@1.0.0/k

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
