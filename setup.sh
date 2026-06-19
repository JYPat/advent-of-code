#!/bin/bash

YEAR=$1
DAY=$2

DIR="src/${YEAR}/${DAY}"

mkdir -p "$DIR"

touch "${DIR}/demo_day${DAY}.txt"
touch "${DIR}/input_day${DAY}.txt"
PYTHON="${DIR}/day${DAY}.py"

if [ ! -f "$PYTHON" ]; then
  echo "from util.util import get_path" >"$PYTHON"
  echo "" >>"$PYTHON"
  echo "with open(get_path(), 'r', encoding='utf-8') as f:" >>"$PYTHON"
  echo "  block = f.read().splitlines()" >>"$PYTHON"

else
  echo "python file already exists"
fi
