import threading
import time

def print_numbers():
    for i in range(1, 6):
        print(i)
        time.sleep(1)

def main():
    thread1 = threading.Thread(target=print_numbers)
    thread2 = threading.Thread(target=print_numbers)
    thread3 = threading.Thread(target=print_numbers)

    thread1.start()
    thread1.join()

    thread2.start()
    thread2.join()
    
    thread3.start()    
    thread3.join()

if __name__ == "__main__":
    main()
