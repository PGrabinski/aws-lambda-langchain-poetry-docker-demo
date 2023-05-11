FROM public.ecr.aws/lambda/python:3.8

WORKDIR /var/task

COPY pyproject.toml poetry.lock ./
RUN pip install poetry && poetry install --no-root --only main

COPY src/ ./

CMD ["lambda_function.handler"]