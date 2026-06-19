import sys
from pathlib import Path
import time

script_dir = Path(sys.argv[0]).resolve().parent


def get_path() -> str:
    if len(sys.argv) < 2:
        print("USAGE: python script.py INPUT/DEMO")
        sys.exit(1)

    file, field = Path(sys.argv[0]).stem, sys.argv[1].upper()

    if field == "INPUT":
        path = script_dir / f"input_{file}.txt"
    elif field == "DEMO":
        path = script_dir / f"./demo_{file}.txt"
    else:
        print("Usage: python script.py INPUT/DEMO")
        sys.exit(1)

    return str(path)


def clock(func):
    def clocked(*argv):
        t0 = time.perf_counter()
        result = func(*argv)
        elapsed = time.perf_counter() - t0
        print(f"Time elapsed: {elapsed:.8f}s")
        return result

    return clocked
