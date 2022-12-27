import os
import urllib.request
from time import sleep
import logging
from datetime import datetime

# current date and time
now = str(datetime.now())

# logfile path
logpath = '/home/<PATH_TO_USER>/rps/'

# IP address of the Orbi router
orbi_ip = '192.168.2.200'

# IP address of the remote power switch
rps_ip = '192.168.2.252'

# password of the remote power switch admin user
rps_pass = 'PASSWORD'

# Email address
email = 'noname@noname.com'

logging.basicConfig(filename=logpath + "events.log", level=logging.DEBUG)
logging.debug(now + "  Starting Orbi online checker.")


def internet_on():
    try:
        urllib.request.urlopen(orbi_ip, timeout=2)
        return True
    except:
        return False


while True:
    state = internet_on()
    now = str(datetime.now())
    if not state:
        logging.error(now + "  Orbi router not available anymore")
        logging.info(now + "  Now powering off and on the power socket")
        os.system("sudo curl http://" + rps_ip + "/set.cmd?user=admin+pass=" + rps_pass + "+cmd=setpower+p61=0+p61n=1+t61=5")
        logging.info(now + "  Sending an email to inform")
        os.system('echo "Subject: Orbi is down" |  sendmail -v ' + email)
        logging.warning(now + "  Sleeping for 10 minutes")
        sleep(600)
    else:
        logging.debug(now + "  We're alright. Sleeping for 15 seconds.")
        sleep(15)
