import time
import schedule

def main():
    schedule.every(2).seconds.do(lambda : print("Jay Ganesh..."))
    
    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()