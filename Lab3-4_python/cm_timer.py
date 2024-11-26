import time
from contextlib import contextmanager
from time import sleep

class cm_timer_1:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        end_time = time.time()
        print(f"time: {end_time - self.start_time}")

@contextmanager
def cm_timer_2():
    start_time = time.time()
    yield
    end_time = time.time()
    print(f"time: {end_time - start_time}")


with cm_timer_1():
    sleep(5.5)

with cm_timer_2():
    sleep(3)