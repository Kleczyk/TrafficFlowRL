#!/bin/bash

xhost +SI:localuser:root
export DISPLAY=localhost:10.0

docker run -it --network=host --ipc=host \
  -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
  -v $HOME/.Xauthority:/root/.Xauthority:ro \
  --env=DISPLAY=$DISPLAY \
  sumo_test

xhost -
