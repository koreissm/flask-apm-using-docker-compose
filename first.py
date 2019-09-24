from ddtrace import tracer
import time
from ddtrace import patch_all
patch_all()

from flask import Flask

tracer.configure(hostname='datadog-agent', port='8126')

with tracer.trace('first-span', service='first-service') as span:
    time.sleep(1)


app = Flask(__name__)


@app.route('/')
def index():
    return 'hello world'


if __name__ == '__main__':
    app.run(port=5000)
