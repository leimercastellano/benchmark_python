from cpu_benchmark import run_benchmark
import threading

class thread_benchmark(threading.Thread):

    def __init__(self, x):
        self.__x = x
        threading.Thread.__init__(self)

    def run(self):
        run_benchmark()



