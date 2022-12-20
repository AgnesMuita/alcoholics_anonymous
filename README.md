# Alcoholics Anonymous

Alcoholics Anonymous is a chat application built for recovering addicts to join a community and talk about their experiences. Built with FastAPI, React and PostgreSQL

Project includes:

-   `fastapi`
-   `react`

##


## Backend 

Setup env variables in `app/core/.env`

#### Install and run

```bash
docker-compose up -d web

# you can track logs with:
docker-compose logs -f --tail=100 web
```

Go to: http://localhost:8000/api/docs/


#### Tests

Run tests

```bash
docker-compose exec web pytest .
```


## Environment Variables

To run this project, you will need to add the following environment variables to your app/core/.env file

`BASE_URL` - default: http://localhost:8000

`RELOAD` - default: false

`DB_HOST` - default: localhost

`DB_PORT` - default: 5432

`DB_USER` - default: postgres

`DB_PASS` - default: postgres

`DB_BASE` - default: db

`DB_ECHO` - default: false
