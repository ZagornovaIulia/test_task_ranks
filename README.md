## Start project with `docker-compose`

```
$ cp .env.example .env.local
$ docker-compose up -d --build
```



Exec commands for docker containers:

```bash
# load database dump from staging
$ make dcreatedb
$ make dloaddump
# dump database from docker container
$ make dcreatedump
# delete database from docker container
$ make ddeletedb

# make migrations && migrate
$ make dmigr
```
