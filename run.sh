mkdir .log 2> /dev/null
DEBUG=0 sudo gunicorn -c gun_conf.py server:app