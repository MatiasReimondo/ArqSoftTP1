pidfile = 'app.pid'
worker_tmp_dir = '/dev/shm'
worker_class = 'gthread'
workers = 4
worker_connections = 1000
timeout = 100
keepalive = 2
threads = 4
proc_name = 'app'
bind = '0.0.0.0:8000'
backlog = 2048
accesslog = '-'
errorlog = '-'
user = 'ubuntu'
group = 'ubuntu'