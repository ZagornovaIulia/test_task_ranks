
## Start project with **docker-compos**e

```
cp .env.example .env.local

docker-compose up -d --build

make dmigr

make dloaddump
```

# dump database from docker container

```
make dcreatedump
```

# delete database from docker container

```
$ make dloaddump
```
