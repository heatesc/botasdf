#!/bin/bash

export OPENAI_API_KEY=$(cat /home/alien/Desktop/my-code/SenPaths/apcoach_pk)
export DISCORD_TOKEN=$(cat /home/alien/Desktop/my-code/SenPaths/botasdf_tok)
export DEBUG_MODE="yes"
python3 bot.py