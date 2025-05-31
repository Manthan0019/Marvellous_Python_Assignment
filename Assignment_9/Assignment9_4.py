import threading
import multiprocessing
import time

def Addition(No):
    sum = 0
    for i in range(1,No + 1):
        sum = sum + i
    print("Sum is : ",sum)


def main():
    Data = 1000000

    start_time = time.time()
    Addition(Data)
    end_time = time.time()
    print("Total time for NORMAL execution : ",end_time - start_time)

    start_time1 = time.time()
    T1 = threading.Thread(target=Addition,args=(Data,))
    T1.start()
    T1.join()
    end_time1 = time.time()
    print("Total time for THREADED execution : ",end_time1 - start_time1)

    start_time2 = time.time()
    P1 = multiprocessing.Process(target=Addition,args=(Data,))
    P1.start()
    P1.join()
    end_time2 = time.time()
    print("Total time for MULTIPROCESSING execution : ",end_time2 - start_time2)

    
if __name__ == "__main__":
    main()