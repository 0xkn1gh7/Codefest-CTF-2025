#! /bin/sh
service=http://172.17.0.1:9512
flag=$(curl -s $service/flag\?chal_id\=$CHALLENGE_ID\&team_id\=$TEAM_ID)
echo $flag > /flag.txt
chmod 444 /flag.txt
exec "$@"
