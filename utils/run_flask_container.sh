#!/bin/bash

get_project_dir() { # Gets the root directory of the repository
    cd "${BASH_SOURCE[0]%*/*}" && pwd
}

if [[ $CONTAINERISED != "true" ]] ; then
    PROJECT_DIR=$(get_project_dir)
else
    PROJECT_DIR="/app"
fi

export PYTHONPATH=$PROJECT_DIR/lib

$PROJECT_DIR/utils/start_app_container.sh Y
