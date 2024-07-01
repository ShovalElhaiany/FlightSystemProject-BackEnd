FROM python:3.11

# Set the working directory inside the container
ENV ProjectDir=/app
RUN mkdir -p $ProjectDir
WORKDIR $ProjectDir

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY . $ProjectDir

RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "python", "app.py" ]