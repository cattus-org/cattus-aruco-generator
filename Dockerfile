FROM public.ecr.aws/lambda/python:3.9

RUN yum -y install libGL libSM libXrender

WORKDIR /var/task

COPY app/requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY app .

CMD ["lambda_function.handler"]
