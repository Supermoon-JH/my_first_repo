from circularDoublyLinkedList import *


def do_sim(cache_slots):

    cache_hit = 0
    tot_cnt = 0

    data_file = open(
        "C:\\Users\\dknl1\\Desktop\\2학년 1학기\\자료구조\\6주차\\소스코드\\linkbench_short.trc")

    list = CircularDoublyLinkedList()

    for line in data_file.readlines():
        lpn = line.split()[0]
        if lpn not in list:
            if len(list) <= cache_slots:
                list.append(lpn)
                tot_cnt += 1
            else:
                list.pop(0)
                list.append(lpn)
                tot_cnt += 1
        else:
            list.pop(list.index(lpn))
            list.append(lpn)
            cache_hit += 1
            tot_cnt += 1

    print("cache_slot = ", cache_slots, "cache_hit = ",
          cache_hit, "hit ratio = ", cache_hit / tot_cnt)


if __name__ == "__main__":

    for cache_slots in range(100, 1001, 100):
        do_sim(cache_slots)
