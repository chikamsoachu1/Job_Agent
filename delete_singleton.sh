#!/bin/bash


# Set -e to exit immediately if a command exits with a non-zero status

#set -e


# Delete all files matching "Singleton*" in the specified directory

#find /app/data/user1-profile -name "Singleton*" -delete


#echo "Deleted Singleton* files from /app/data/user1-profile"


#!/bin/bash


# Delete Singleton* files from user1-profile

find /app/data/user1-profile -name "Singleton*" -print0 | xargs -0 rm -f


# Delete Singleton* files from user2-profile

find /app/data/user2-profile -name "Singleton*" -print0 | xargs -0 rm -f


# Start the main application

exec "$@"
