all: run

build:
	docker build -t telegram-bot-template .

run: build
	docker run -d --name telegram-bot telegram-bot-template

delete: stop rm-image

stop:
	docker stop telegram-bot

rm:
	docker rm telegram-bot

rm-image: rm
	docker rmi telegram-bot-template

start: stop
	docker start telegram-bot
