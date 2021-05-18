#!/bin/bash

set -o errexit
set -o nounset


eval $FAUST_RUN

exec "$@"