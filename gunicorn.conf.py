import os

bind = f"0.0.0.0:{os.getenv('PORT', 8000)}"
workers = 1
worker_class = "sync"   # FIXED: no gevent → email works
timeout = 30
keepalive = 5
loglevel = "debug"
accesslog = "-"
errorlog = "-"
