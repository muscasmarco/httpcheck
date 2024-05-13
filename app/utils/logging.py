import time
from pathlib import Path
from fastapi import Request
from datetime import datetime

import logging
logging.basicConfig(filename = 'requests.log',
                    filemode = 'a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt = '%H:%M:%S',
                    level = logging.INFO,)


class RequestLogger:

    def __init__(self,):
        self.logger = logging.getLogger('requests_logger')
        self.logger.setLevel(logging.INFO)
        self.file_handle = logging.FileHandler('spam.log')
        self.logger.addHandler(self.file_handle)
        

    def log(self, request: Request, status: str):
        """
            Logs the fastapi Request. This method will usually be called inside a 
            fastapi endpoint function call.

            Args:
                request (fastapi.Request): the received request to be logged to file.
                status  (int): A status code to be logged. For now it's the status of the HTTP req that is going to be returned to the client.
        """

        message = f"Response: {status} - Client {request.client[0]}:{request.client[1]} sent a GET to endpoint {request.url._url}."
        self.logger.info(msg = message)
        return
    

logger = logging.getLogger()

