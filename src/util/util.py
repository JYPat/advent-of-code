import sys

if len(sys.argv) < 2:
    print("USAGE: python script.py INPUT/DEMO")
    sys.exit(1)

file, field = sys.argv[0].strip(".py"), sys.argv[1]

if field == "INPUT":
    path = f"./input_{file}.txt"
elif field == "DEMO":
    path = f"./demo_{file}.txt"
else:
    print("Usage: python script.py INPUT/DEMO")
    sys.exit(1)

lines = (line for line in open(path, "r", encoding="utf-8"))
