pid=`ps -ef | grep iptraf | grep -v grep | awk '{print $2}'`
kill -USR2 $pid