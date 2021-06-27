# A-Microservice-For-Book-Store
Creation of a CRUD microservice for a book store

## Overview:
A simple API that respects the REST architecture, implemented in the micro web framewok written in python: Flask. 
It uses also MomgoDB and Docker technologies.  

## Deploy:
1. Clone this repository  : `$ git clone https://github.com/Mariem-Kammoun/A-Microservice-For-Book-Store.git `
2. Change the current working directory : `$ cd A-Microservice-For-Book-Store/ `
3. Create the docker image : app-image   : `$ docker build -t app-image . `
4. Build and start our container `$docker-compose up -d `
5. List all our active running containers to see our four containers running and be able to identify them by the ports
 that they run on `$docker ps `

## Exposed Ports:

|  Service      | Exposed Port  | Internal Port |
| ------------- | ------------- |-------------- |
|  App          |      5000     |    5000       |
|  MongoDB	     |        -      |    27017      |
|  Prometheus   |        -      |    9090       |
|  Grafana      |      3000     |    3000       |

## Architecture:
![Architecture](/images/architecture.png)

## Endpoints:

|  Path         |     Type      |                 Description                          |
| ------------- | ------------- |----------------------------------------------------- |
|  /books       |      GET      |    Return a list of existing books and their details |
|  /books	      |      POST     |    Create a new book                                 |
|  /books/n     |      GET      |    Return if the n id book found or not              |
|  /books/n     |      PUT      |    Update a the n id book                            |
|  /books/n     |      DELETE   |    Delete a the n id book                            | 
|  /metrics     |      GET      |    Return the metrics provided by Prometheus         |
