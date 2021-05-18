stream:
	docker-compose up --build -d stream

scale-steam:
	docker-compose up -d --scale stream=5
	
api:
	docker-compose up --build -d api

locust:
	docker-compose up -d locust_worker

logs-api:
	docker-compose logs -f api

logs-stream:
	docker-compose logs -f api

down:
	docker-compose down -v

kafkacat:
	kafkacat -b localhost:9092 -C -e -o beginning -t pen_test | jq .