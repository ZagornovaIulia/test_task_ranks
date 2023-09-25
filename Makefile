#!make
include .env

dcollect:
	docker-compose exec web python manage.py collectstatic
dupbuild:
	docker-compose -f "docker-compose.prod.yml" up --build
dup:
	docker-compose -f "docker-compose.prod.yml" up
dbuild:
	docker-compose -f "docker-compose.prod.yml" build
dstop:
	docker-compose -f "docker-compose.prod.yml" stop

dmigr:
	docker-compose exec web python manage.py makemigrations && docker-compose exec web python manage.py migrate
duser:
	docker-compose exec web python manage.py createsuperuser
dshell:
	docker-compose exec web python manage.py shell

dloaddump:
	docker-compose exec web python manage.py loaddata db.json
dcreatedump:
	docker-compose exec web python manage.py dumpdata > core/db.json