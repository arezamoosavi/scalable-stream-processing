api:
	docker-compose up --build -d api

stream:
	docker-compose up --build -d stream

scale-stream:
	docker-compose scale stream=5

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

kafka:
	docker-compose up -d zookeeper kafka

pg:
	docker-compose up -d postgres

kafkacat:
	kafkacat -b localhost:9092 -C -e -o beginning -t pen_test | jq .

zookeeper:
	docker-compose exec zookeeper bash

consumer:
	docker-compose exec zookeeper \
	kafka-consumer-groups --bootstrap-server kafka:29092 \
	--group pen_test_v1001 --describe --verbose

create-topic1:
	docker-compose exec zookeeper kafka-topics --create --zookeeper localhost:2181 \
	--replication-factor 1 --partitions 10 --topic pen_test

create-topic2:
	docker-compose exec zookeeper kafka-topics --create --zookeeper localhost:2181 \
	--replication-factor 1 --partitions 1 --topic pen_test2

alter-topic2:
	docker-compose exec zookeeper kafka-topics --alter --zookeeper localhost:2181 \
	--topic pen_test2 --partitions 10

describe-topic1:
	docker-compose exec zookeeper kafka-topics --describe --zookeeper localhost:2181 \
	--topic pen_test

describe-topic2:
	docker-compose exec zookeeper kafka-topics --describe --zookeeper localhost:2181 \
	--topic pen_test2