# scalable-stream-processing
distributed stream processing using faust and celery

## Installation

```bash
make pg-kafka
make api
make stream
make queue
docker-compose scale queue=10
```

## Locust Load Test

```bash
make locust
```
for locust test go to “http://localhost:8090/"

## [Medium](https://sdamoosavi.medium.com/scalable-stream-processing-using-queue-bf39f6c1f490)
