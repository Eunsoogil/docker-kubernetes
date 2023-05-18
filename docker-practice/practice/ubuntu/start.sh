# ssh start and tail -f for detach mode
# /sbin/init &&
service ssh start
tail -f /dev/null
