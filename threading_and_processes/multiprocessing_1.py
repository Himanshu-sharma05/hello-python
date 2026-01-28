from multiprocessing import Process
import time 

def toast_bread(name):
    print(f"Preparing ingredients for  {name} ")
    time.sleep(3)
    print(f"Toast {name} is prepared ")


if __name__ == "__main__":
    breads = [Process(target=toast_bread,args=(f"Order No: {i}",)) for i in range(3)]
    for p in breads:
        p.start()

    for p in breads:
        p.join()

    print("All orders done.")