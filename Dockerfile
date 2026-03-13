FROM debian:bullseye

# install base packets
RUN apt-get update
RUN apt-get -y install lib32stdc++6 lib32gcc-s1 wget curl vim nginx procps git unrar-free file unzip libncurses5

RUN mkdir /bf2
COPY bf2 /bf2
COPY bf2hub /bf2

CMD cd bf2 && exec ./start_bf2hub.sh +modPath mods/xpack