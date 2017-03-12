# Get speaker alert when Internet starts working
wget google.co.in
( speaker-test -t sine -f 1000 )& pid=$! ; sleep 0.5s ; kill -9 $pid
( speaker-test -t sine -f 1000 )& pid=$! ; sleep 0.5s ; kill -9 $pid
( speaker-test -t sine -f 1000 )& pid=$! ; sleep 0.5s ; kill -9 $pid
