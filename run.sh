docker run --rm -it \
  --name bf2 \
  -p 16567:16567/udp \
  -p 29900:29900/udp \
  evgeniyfimushkin/bf2:1.0 \
  /bin/bash -c "cd bf2 && ./start_bf2hub.sh"
