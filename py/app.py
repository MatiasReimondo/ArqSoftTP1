import time

from flask import Flask

TIMEOUT = 5
LOOP = 0.5
app = Flask(__name__)

@app.route("/")
def ping():
  return "python - ping"

@app.route("/timeout")
def timeout():
  time.sleep(TIMEOUT)
  return "python - timeout"

@app.route("/heavy")
def heavy():
  t_end = time.time() + LOOP
  while time.time() < t_end:
    pass
  return "python - heavy"

if (__name__ == "__main__"):
  app.run()