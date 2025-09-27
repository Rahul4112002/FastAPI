import time
from timeit import default_timer as timer

def run_task(name, seconds):
    print(f'{name} started at {timer()}')
    time.sleep(seconds)
    print(f'{name} completed at {timer()}')
    
start =  timer()

run_task('Task 1', 2)
run_task('Task 2', 1)
run_task('Task 3', 3)

print(f'\n Total time taken: {timer() - start:.2f} s')