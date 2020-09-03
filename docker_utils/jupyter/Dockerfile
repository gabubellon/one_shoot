FROM conda/miniconda3

WORKDIR /code

COPY requirements.txt requirements.txt
RUN apt-get update && \
    apt-get install -y build-essential git libicu-dev && \
    pip --no-cache install -r requirements.txt && \
    apt-get purge -y build-essential git && \
    rm -rf /var/lib/apt/lists/*

CMD ["jupyter", "notebook", "--no-browser", "--ip", "0.0.0.0", "--allow-root"]