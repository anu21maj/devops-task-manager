FROM python:3.14-slim
#Start building my image from this existing image
#starting with a lightweight Linux environment that already has Python 3.14 installed.

WORKDIR /app
#Inside the container, make /app the working directory for our application.

COPY app/requirements.txt .
#Copy the requirements.txt file from the host machine to the working directory in the container.

RUN pip install --no-cache-dir -r requirements.txt
#Install the dependencies listed in requirements.txt using pip, without caching the downloaded packages to reduce image size.

COPY app/ .
#Copy the contents of the app directory from the host machine to the working directory in the container.

EXPOSE 5000
#Tell Docker that the container will listen on port 5000 at runtime.

CMD ["python", "app.py"]
#Set the default command to run when the container starts, which is to execute the app.py file using Python.



