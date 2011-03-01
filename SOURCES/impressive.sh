#!/bin/bash

. /usr/share/opengl-games-utils/opengl-game-functions.sh

APP=python-impressive

checkDriOK $APP

exec $APP "$@"
