# movies-microservices

---

## Description
Microservice is the approach of breaking down large monolith applications into individual applications specializing
in a specific service/functionality. This approach is often known as Service-Oriented Architecture or SOA.

Python is a perfect tool for building micro-services because it comes with a great community, 
an easy learning curve, and tons of libraries. Due to the introduction of asynchronous programming in Python, 
web frameworks with performance on par with GO and Node.js have emerged.

FastAPI is a modern, high-performance, web framework, which comes with tons of cool features like auto-documentation 
based on OpenAPI and built-in serialization and validation library. 
See [here](https://fastapi.tiangolo.com/features/) for the list of all the cool features in FastAPI.

## Goals
 - How to build REST API using FastAPI and PostgreSQL
 - How to build microservice using FastAPI
 - How to run microservices using docker-compose
 - How to manage microservices using Nginx
 - How to test developed code

## Data Management

The current approach is Database Per Service.

Using a database for each service is great to keep the microservices as loosely coupled as possible.
Having a different database per service allows us to scale different services independently.
A transaction involving multiple databases is done through well-defined APIs.
This has a disadvantage because implementing business transactions spanning multiple services is not straightforward.
In addition, the addition of network overhead makes it less efficient to use.


## How to run the project
 - Make sure you have installed `docker` and `docker-compose`
 - Prepare your own `.env` file (check the examples section)
 - Run `docker-compose up -d`
 - Head over to http://localhost:8080/api/v1/movies/docs for movie service docs 
   and http://localhost:8080/api/v1/casts/docs for cast service docs


### Examples

- dot env `.env` file

     ```
     # URL to the database for cast service (postgresql://<username>:<password>@<host>:<db_port>/<cast_db_name>).
     # NOTE: 
     #       In the case of local development, the host should be related to the local address i.e. "localhost"
     #       In the case of docker development it can be a database service name like "cast_db" (docker-compose.yaml file).
     CAST_DATABASE_URL=postgresql://postgres:my-secret-password@cast_db:5432/cast_db_dev
     
     # Name of PostgreSQL database related to cast service.
     CAST_POSTGRES_DB=cast_db_dev
     
     # URL to the database for movie service.
     MOVIE_DATABASE_URL=postgresql://<username>:<password>@<host>:<db_port>/<movie_db_name>
     
     # Name of PostgreSQL database related to movie service.
     MOVIE_POSTGRES_DB=movie_db_dev
     
     # PostgreSQL username.
     POSTGRES_USER=postgres
     
     # PostgreSQL user password.
     POSTGRES_PASSWORD=password123
     ```

### Resources
 - [Microservice in Python using FastAPI](https://dev.to/paurakhsharma/microservice-in-python-using-fastapi-24cc)
 - [Developing and Testing an Asynchronous API with FastAPI and Pytest](https://testdriven.io/blog/fastapi-crud/)