# Dreamteam API

Simple API to execute CRUD operations.

## Requirements
* Python3
* Docker

# Usage
* Running on the host machine:

   After download this repository, install dependencies:
   ```
   $ cd src
   $ pip3 install -r requirements.txt
   ```
   Create the database and execute the api server:
   ```
   $./build_database.py
   $./server.py
   ```

* Running in a docker container:

   Build the docker image and run exposing the port 5000:
   ```
   $ docker build -t="apiserver" .
   $ docker run -p 5000:5000 apiserver
   ```

# Testing

   Go to http://127.0.0.1/api/ui to interact with the RESTful api:

   ![Screenshot](https://github.com/loide/loide.github.io/blob/master/images/dreateam_api.png?raw=true)
