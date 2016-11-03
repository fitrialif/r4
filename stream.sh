#! /bin/sh

# -n : Stop video from preview
raspivid -o - -t 0 -n -fps 30 | cvlc -vvv stream:///dev/stdin --sout '#rtp{sdp=rtsp://:8888/}' :demux=h264
