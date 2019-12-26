#!/bin/bash

docker=podman

image=clinicaldataserviceimage
container=clinicaldataservicecontainer
port=5000

${docker} container rm -f ${container}
${docker} rmi ${image}

${docker} build -t ${image} -f Dockerfiles/Dockerfile.service . 
${docker} run -d -p ${port}:8000 --name ${container} ${image}
