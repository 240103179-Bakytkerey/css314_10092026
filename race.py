import threading
import time

counter = 0

def increment_without_lock():
    global counter
    for _ in range(1000000):
        counter += 1

def run_unsync():
    global counter
    counter = 0
    threads = []
    start = time.time()
    for _ in range(10):
        t = threading.Thread(target=increment_without_lock)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    end = time.time()
    return counter, (end - start) * 1000

counter_sync = 0
lock = threading.Lock()

def increment_with_lock():
    global counter_sync
    for _ in range(1000000):
        with lock:
            counter_sync += 1

def run_sync():
    global counter_sync
    counter_sync = 0
    threads = []
    start = time.time()
    for _ in range(10):
        t = threading.Thread(target=increment_with_lock)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    end = time.time()
    return counter_sync, (end - start) * 1000

if __name__ == "__main__":
    print("Қорғаныссыз (Unlocked) 10 рет тестілеу:")
    for i in range(1, 11):
        val, _ = run_unsync()
        error = 10000000 - val
        print(f"Run #{i:2} | Measured Output: {val:8} | Error: {error}")
        
    sync_val, sync_time = run_sync()
    _, unsync_time = run_unsync()
    
    print(f"\nUnlocked Time = {unsync_time:.0f} ms")
    print(f"Locked Time = {sync_time:.0f} ms")
