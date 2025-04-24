#!/bin/bash





find /app/data/user1-profile -name "Singleton*" -delete


find /app/data/user2-profile -name "Singleton*" -deletex

















# Start supervisord in the foreground to properly manage child processes
exec /usr/bin/supervisord -n -c /etc/supervisor/conf.d/supervisord.conf
