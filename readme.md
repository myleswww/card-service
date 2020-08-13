# BCR card scan service

## requirements

```
sudo apt update && sudo apt install beanstalkd
sudo systemctl enable beanstalkd
```

## project setup

```
git clone https://github.butler.edu/mbwright/card-scan-service.git
cd card-scan-service
python3 -m venv venv
source ./venv/bin/activate
python3 -m pip install -r requirements.txt
FLASK_APP=app python -m flask run
```

Also, separately run:
- app/main.py
- app/monitor_service.py

