import os

# Render sets PORT environment variable, default to 10000 for Render
port = os.getenv('PORT', '10000')
bind = f"0.0.0.0:{port}"
workers = 1
worker_class = "sync"   # FIXED: no gevent → email works
timeout = 30
keepalive = 5
loglevel = "info"  # Changed from debug to info for production
accesslog = "-"
errorlog = "-"
