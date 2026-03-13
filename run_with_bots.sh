docker run --rm -it \
  --name bf2 \
  -p 16567:16567/udp \
  -p 29900:29900/udp \
  -p 55124:55124/udp \
  -p 55125:55125/udp \
  -p 4711:4711/tcp \
  -v "./bf2_settings/bots/maplist.con:/bf2/mods/bf2/settings/maplist.con" \
  -v "./bf2_settings/bots/serversettings.con:/bf2/mods/bf2/settings/serversettings.con" \
  evgeniyfimushkin/bf2:1.0 \
  /bin/bash -c "cd bf2 && ./start_bf2hub.sh +modPath mods/xpack"
