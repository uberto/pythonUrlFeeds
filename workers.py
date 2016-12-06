from multiprocessing import Process, Queue, Pool

NUM_PROCESSES = 4

def processAll(funs, articles):
    pool = Pool(processes=NUM_PROCESSES)

    inList = articles
    for f in funs:
        outList = pool.map(f, inList)
        inList = outList

    return outList




