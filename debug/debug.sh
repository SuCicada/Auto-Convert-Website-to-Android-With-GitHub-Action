#!/bin/bash

docker_proxy=http://192.168.65.2:10809

current=$(realpath $(dirname $0))
echo $current

act-su issues \
  -e $current/issue.json \
  -s github.actor=SuCicada \
  -s GITHUB_TOKEN=$GITHUB_TOKEN \
  -s github.repository=SuCicada/test-github-action \
  --env https_proxy=$docker_proxy \
  --env http_proxy=$docker_proxy \
  --env all_proxy=$docker_proxy \
  --env DEBUG=true \
  --git-proxy http://127.0.0.1:10809 \
  $@
