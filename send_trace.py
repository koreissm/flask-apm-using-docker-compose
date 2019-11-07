from ddtrace import patch_all
from flask import Flask

from ddtrace import tracer

tracer.configure(hostname='datadog-agent', port=8126)

patch_all()

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello world'

if __name__ == '__main__':
    app.run(host= '0.0.0.0', port=80)
