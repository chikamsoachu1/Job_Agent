#!/bin/bash





find /home/appuser/chrome_data -name "Singleton*" -delete


find /app/data/chrome_data -name "Singleton*" -deletex

















# Start supervisord in the foreground to properly manage child processes
exec /usr/bin/supervisord -n -c /etc/supervisor/conf.d/supervisord.conf
