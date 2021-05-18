api:
	docker-compose up --build -d api

stream:
	docker-compose up --build -d stream

queue:
	docker-compose up --build -d queue

scale-queue:
	docker-compose scale queue=3

locust:
	locust -f src/locust/pen_test_locust.py -P 8090

logs-api:
	docker-compose logs -f api

logs-queue:
	docker-compose logs -f queue

logs-stream:
	docker-compose logs -f stream

down:
	docker-compose down -v

pg-kafka:
	docker-compose up -d zookeeper kafka postgres

kafkacat:
	kafkacat -b localhost:9092 -C -e -o beginning -t pen_test | jq .