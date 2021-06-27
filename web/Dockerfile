# Pull python 3 image
FROM python:3.8-slim-buster
# Create a work dir
WORKDIR /usr/src/app
# copy requirements.txt into workdir created above
COPY requirements.txt ./
# Install all requirements
RUN python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt
# Copy entire project into workdir
COPY . .
# Run our app without output
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]