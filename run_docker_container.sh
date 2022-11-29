
docker run -it --rm \
    -p 0.0.0.0:6006:6006 \
    --runtime=nvidia \
    -v ${PWD}:/workspace cfg_ws:latest
