import time
import os

from dotenv import load_dotenv
load_dotenv()

def test():
    st = time.process_time()
    exec(open('test.py').read(), globals())
    result = time.process_time() - st
    return result

def run(file):
    st = time.process_time()
    exec(open(f'{os.getenv("file_path")}{file}/main.py').read())
    result = time.process_time() - st
    return result

def average(file):
    results = [run(file) for i in range(1000)]
    average = sum(results) / len(results)
    print(f"{round(average, 10) * 1000}ms")

print(test())
# average(2)