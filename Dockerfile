# set base image (host OS)
FROM python:3.8

# set the working directory in the container
WORKDIR /

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies / make sure time zone is correct
RUN ln -sf /usr/share/zoneinfo/America/New_York /etc/timezone && \
    ln -sf /usr/share/zoneinfo/America/New_York /etc/localtime && \
    pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY src/ .

# command to run on container start
CMD [ "python", "main.py" ]
