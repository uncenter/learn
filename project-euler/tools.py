import time
from funcenter import cprint

# https://stackoverflow.com/a/25061573/17378715 #
from contextlib import contextmanager
import sys, os

@contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:  
            yield
        finally:
            sys.stdout = old_stdout
# --------------------------------------------- #

def run(file):
    st = time.process_time()
    exec(open(f'{file}/main.py').read())
    result = time.process_time() - st
    return result

def average(file):
    cprint('blue', f"Timing <{file}/main.py>...")
    with suppress_stdout():
        first_runtime =  run(str(file))*1000
        if first_runtime < 1:
            runs = 10000
        elif first_runtime > 25:
            runs = 100
        else:
            runs = 1000
        st = time.process_time()
        avg_runtime = [run(str(file)) for i in range(runs)]
        test_runtime = time.process_time() - st
    average = sum(avg_runtime) / len(avg_runtime)
    cprint('green', f"Ran {runs} tests in {round(test_runtime, 2)} seconds.")
    print(f"{round(average, 10)}s\n{round(average, 10) * 1000}ms")
    cprint('blue', f"Timing <{file}/main.py> concluded.")

average(3)