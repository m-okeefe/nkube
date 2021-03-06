#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail

BUILD_PATH="$(dirname "${BASH_SOURCE}")"
docker build -t meganokeefe/nkube:latest "${BUILD_PATH}"
