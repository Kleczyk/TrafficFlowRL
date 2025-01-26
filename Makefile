doker_gui:
	docker run -it --network=host --ipc=host \
	  -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
	  -v $HOME/.Xauthority:/root/.Xauthority:ro \
	  --env=DISPLAY=$DISPLAY \
	  sumo_test