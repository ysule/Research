pid=`ps -ef | grep iptraf | grep -v grep | awk '{print $2}'`
echo $pid
kill -USR2 $pid