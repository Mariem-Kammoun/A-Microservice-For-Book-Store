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

## Testing:
I used Postman to test my API.
![GET_Books](/images/Testing/1.PNG)

![POST_CreationBooks](/images/Testing/2_post_creation-book.PNG)

![GET_Add_Book](/images/Testing/3_Get_Add-book-done.PNG)

![PUT_update_book](/images/Testing/4_PUT_update_book.PNG)

![PUT_update_book2](/images/Testing/5_Update_done.PNG)

![Delete_book](/images/Testing/6_Delete_book.PNG)

![Delete_done](/images/Testing/7_delete_done.PNG)

## Documenting:
I used Swagger to document my REST-API. So, I created swagger_books files.
![Documentation](/images/Documenting/swaggerEditor.PNG)

## Screenshots:
![Metrics](/images/Screenshots/metrics with docker_compose.PNG)

![Grafana1](/images/Screenshots/grafana_first_dashboard.PNG)

![Grafana2](/images/Screenshots/grafana_my_second_dashboard_with_2_panels.PNG)

![Grafana3](/images/Screenshots/grafana_panel_1.PNG)

![Grafana4](/images/Screenshots/grafana_panel_1_prom_query.PNG)

![Grafana5](/images/Screenshots/grafana_2_panel.PNG)

![Grafana6](/images/Screenshots/grafana_panel_2_editor.PNG)
