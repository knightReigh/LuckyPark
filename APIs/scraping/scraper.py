import logging
import time
import requsts
import re

from urllib.parse import urlparse


########### establish logging ############

logging.getLogger().addHandler(logging.StreamHandler())
logging.basicConfig(filename="sys.log", level=logging.DEBUG)




########### http request parameters ##############
HEADER = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) \
    AppleWebKit/537.36 (KHTML, like Gecko) \
        Chrome/35.0.1916.114 Safari/537.36'
    }
CONNECTION_TIMEOUT = 90
RECONNECTION_TIME = 1

ERROR_STATUS_CODE = "Invalid status_code from %s: %s"
ERROR_CONNECTION_TIMEOUT = "Unable to connect to %s after %s seconds."
ERROR_CONNECTION_TRIALLIMIT = "Unable to connect to %s after %s trial times"



######### functions #########

def requestHTTP(uri):
    """
        make a HTTP request, return {response object} if successful; return {none} if failed
    """

    logging.info("Starting HTTP request to %s" % uri)
    start_time = time.time()

    while True:
            try:
                r = requests.get(uri, headers=HEADER)
                break
            except requests.ConnectionError:
                if time.time() > start_time + CONNECTION_TIMEOUT:
                    logger.info(ERROR_CONNECTION_TIMEOUT % (uri, CONNECTION_TIMEOUT))
                    return None
                else:
                    time.sleep(RECONNECTION_TIME)

    # valid response, analyze return status
    if r.status_code == 200:
        return r
    else:
        logger.info("HTTP request error:")
        logger.info(ERROR_STATUS_CODE % (uri, r.status_code))
        logger.info("   - request involked by %s", func_name)
        return None

