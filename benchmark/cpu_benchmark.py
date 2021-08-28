#!/usr/bin/python3

# -----------------------------------------------------------
# Benchmark CPU
# 2021 Leimer Castellano --- Barcelona, Spain
# Released under GNU Public License (GPL)
# email leimercastellano@gmx.com
# command to look at the processor
#FreeBsd -->  sysctl -a | egrep -i 'hw.machine|hw.model|hw.ncpu'
#FreeBsd --> sysctl hw.model hw.machine hw.ncpu
# -----------------------------------------------------------


import time
import platform

def run_benchmark():
    if "Linux" == platform.system():
        with open('/proc/cpuinfo') as f:
            for line in f:
                # Ignore the blank line separating the information between
                # details about two processing units
                if line.strip():
                    if line.rstrip('\n').startswith('model name'):
                        model_name = line.rstrip('\n').split(':')[1]
                        print('Os: Linux -- Processor:' + model_name)
                        break
    else:
        print('Your CPU is only shown automatic on Linux system.')

    # laeufe -- How many tries per iteration?
    laeufe = 1000
    # wiederholungen -- How many iterations (repetitions)? )
    wiederholungen = 10

    schnitt = 0
    for a in range(0, wiederholungen):

        start = time.time()

        for i in range(0, laeufe):
            for x in range(1, 1000):
                3.141592 * 2 ** x
            for x in range(1, 10000):
                float(x) / 3.141592
            for x in range(1, 10000):
                float(3.141592) / x

        ende = time.time()
        dauer = (ende - start)
        dauer = round(dauer, 3)
        schnitt += dauer
        print('Time: ' + str(dauer) + 's')

    schnitt = round(schnitt / wiederholungen, 3)
    print('Avarage: ' + str(schnitt) + 's')
