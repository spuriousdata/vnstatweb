import logging
from flask import Flask
from vnstatweb import settings

app = Flask(__name__)
app.debug = settings.debug
app.logger.setLevel(logging.DEBUG)

app.register_error_handler(500, lambda e: 'bad request!')
