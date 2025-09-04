FROM python:3.10-slim AS builder

RUN apt-get update && \
    apt-get install -y libgl1 libsm6 libxrender1 && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

FROM python:3.10-slim

WORKDIR /var/task

RUN pip install --no-cache-dir awslambdaric

COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /app /var/task

CMD ["python3", "-m", "awslambdaric", "lambda_function.handler"]
