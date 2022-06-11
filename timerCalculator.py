from threading import Thread
import time


def TempoDeExecucaoDeUmaThread(thr: Thread, arquivo):
    t1 = time.time()
    thr.start()
    t2 = time.time()
    thr.join()
    arquivo.write(f"{t2 - t1}\n")