#!/bin/bash

YEAR=$1
DAY=$2
MODE=$3

TARGET = "src/${YEAR}/day_${DAY}/day${DAY}.py"

if [! -f "$TARGET"]; then
  PYTHONPATH=. python3 "$TARGET" "$MODE"

else
  echo "Could not find file at $TARGET"
fi
