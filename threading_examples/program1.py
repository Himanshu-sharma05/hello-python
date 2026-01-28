import threading
import time

def serve_toast(order_no:int):
    print(f"Preparing toast {order_no}")
    time.sleep(3)
    print(f"Toast {order_no} Ready")

first_thread = threading.Thread(target=serve_toast,args=(1,))
second_thread = threading.Thread(target=serve_toast,args=(2,))

first_thread.start()
second_thread.start()

first_thread.join()
second_thread.join()

print("Both threads finished executing")