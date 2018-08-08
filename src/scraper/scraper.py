import logging
import time
import requests
import re


########### establish logging ############
logging.basicConfig(filename="sys.log", level=logging.DEBUG, filemode='w')
handler = logging.StreamHandler()
handler.setLevel("INFO")
logging.getLogger().addHandler(handler)
logging.getLogger("urllib3").setLevel(logging.CRITICAL) # suppress requets/urllib3 debug information

########### http request parameters ##############
HEADER = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) \
    AppleWebKit/537.36 (KHTML, like Gecko) \
        Chrome/35.0.1916.114 Safari/537.36'
    }
CONNECTION_TIMEOUT = 9
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

    # add scheme if scheme is missing in uri
    uri = validateURL(uri)

    while True:
            try:
                r = requests.get(uri, headers=HEADER)
                break
            except requests.ConnectionError:
                if time.time() > start_time + CONNECTION_TIMEOUT:
                    logging.info(ERROR_CONNECTION_TIMEOUT % (uri, CONNECTION_TIMEOUT))
                    return None
                else:
                    time.sleep(RECONNECTION_TIME)
            except Exception as e:
                logging.info("Exception: " + e)
                return None

    # valid response, analyze return status
    if r.status_code == 200:
        return r
    else:
        logging.info("HTTP status error:")
        logging.info(ERROR_STATUS_CODE % (uri, r.status_code))
        logging.info("   - request involked by %s", func_name)
        return None


def validateURL(uri):
    """
        I am only going to check for scheme omission. This is NOT a strict url validator.
    """
    reg = re.compile(r'^(?:http|ftp)s?://'
            , re.IGNORECASE)
    return uri if re.match(reg, uri) else ("http://" + uri)
