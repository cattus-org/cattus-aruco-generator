FROM public.ecr.aws/lambda/python:3.10

RUN yum -y install libGL libSM libXrender

WORKDIR /var/task

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

CMD ["lambda_function.handler"]
