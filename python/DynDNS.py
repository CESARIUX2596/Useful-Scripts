#!/usr/bin/python3
import requests
from urllib.request import urlopen
from requests import get
import time
import logging

# Credentials
username = 'username goes here'
password = 'password goes here'
hostname = 'sub.example.com'
timer = 30
ip = ''

logging.basicConfig(filename="DynDNS.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

while True:
    try:
        current_ip = urlopen('https://api.ipify.org/').read().decode('utf-8')
    except:

        logger.error('SOMETHING WENT WRONG!!!')
        time.sleep(timer)
    else:
        if ip != current_ip:
            # Use this line for IPv4
            url = 'https://{}:{}@domains.google.com/nic/update?hostname={}&myip={}'.format(
                username, password, hostname, current_ip)
            resp = requests.post(url)
            out = resp.content.decode('utf-8')
            if ('good' in out or 'nochg' in out):
                ip = current_ip
            logger.info('****{} UPDATE****'.format(hostname))
            logger.info('DynDNS Response {}'.format(out))
            # Use this line for IPv6
            # url = 'https://{}:{}@domains.google.com/nic/update?hostname={}'.format(username,password,hostname)
        time.sleep(timer)
