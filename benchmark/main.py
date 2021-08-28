from thread_benchmark import thread_benchmark as b


# -----------------------------------------------------------
# Benchmark CPU
# 2021 Leimer Castellano --- Barcelona, Spain
# Released under GNU Public License (GPL)
# email leimercastellano@gmx.com
# -----------------------------------------------------------


def run_benchmark():
    n_threads = input("number of threads to create: \n")
    try:
        n_threads = int(n_threads)

    except Exception:
        return print("Error")

    for i in range(n_threads):
        b(i).start()

if __name__ == '__main__':
    run_benchmark()
