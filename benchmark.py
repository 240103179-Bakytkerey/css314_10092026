import time
import multiprocessing

def compute_task(chunk_size):
    result = 0
    for i in range(int(chunk_size)):
        result += (i * i) ** 0.5
    return result

def run_benchmark(N, total_work=20000000):
    chunk = total_work / N
    start_time = time.time()
    
    with multiprocessing.Pool(processes=N) as pool:
        pool.map(compute_task, [chunk] * N)
        
    return time.time() - start_time

if __name__ == '__main__':
    total_work = 20000000 
    thread_counts = [1, 2, 4, 8, 16, 32]
    
    print("Benchmark starts...")
    
    baseline_time = None
    
    for n in thread_counts:
        times = []
        for run in range(3):
            t = run_benchmark(n, total_work)
            times.append(t)
            
        avg_time = sum(times) / 3
        
        if n == 1:
            baseline_time = avg_time
            
        speedup = baseline_time / avg_time
        efficiency = (speedup / n) * 100
        
        print(f"N={n:2} | Run 1: {times[0]:.3f}s | Run 2: {times[1]:.3f}s | Run 3: {times[2]:.3f}s | Avg: {avg_time:.3f}s | Speedup: {speedup:.2f}x | Efficiency: {efficiency:.1f}%")
