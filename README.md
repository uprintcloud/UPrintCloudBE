# UPrintCloud

Cloud Printer

# Requirements

```python
Python ≥ 3.6
asyncio
pika
```

# Master

```python
/admin
/upload -> [/api/upload] -> /upload
/api/request?job_id=&client_id= -> rabbitmq -> client
```

# RabbitMQ

master
admin

# Client

```python
query
print
```

# Server

```python
/admin
/upload  # File upload
/request/download/<file_name>
/request/submit  # User request for print job
```

# Printer

