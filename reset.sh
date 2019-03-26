#!/bin/bash
rm -rf Data/migrations/*
touch Data/migrations/__init__.py
rm db.sqlite3
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser

