#!/bin/bash

cd portfolio

git fetch && git reset origin/main --hard

docker compose -f docker-compose.prod.yml down
docker compose -f docker-compose.prod.yml up -d --build

python -m venv python3-virtualenv
source python3-virtualenv/bin/activate
pip install -r requirements.txt

systemctl restart myportfolio