# UPrintCloudBE

A open source version of Do La, but more efficient maybe.

# Requirements

```
Python ≥ 3.6
django
pika
filetype
```

# API

| url | Function |
| --- | --- |
| /admin | administration |
| /upload | file uploading temporary frontend |
| /login | user sign in |
| /join | user sign up |
| /api/upload | **username, file**, only *.pdf will be accepted |
| /api/request?**job_id=&client_id=** | send a print job to client |
| /api/login | **email or username, password** |
| /api/join | **email, nickname, password** |

# Testing Deployment

```bash
bash reset.sh
```

Then access `127.0.0.1:8000/init` in browser is required

## Web root

[127.0.0.1:8000](http://127.0.0.1:8000)
