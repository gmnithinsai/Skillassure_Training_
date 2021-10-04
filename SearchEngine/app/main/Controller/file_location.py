import os
import concurrent.futures
from app.main.Exceptions import *

# locates files in drives
def locate_file(search_file,drive):
    try:
        location = []
        for r,d,f in os.walk(drive):
            if drive == 'C:\\':
                if search_file in f:
                    c_res = os.path.join(r,search_file)
                    location.append(c_res)                
                    break
            if search_file in f:
                res = os.path.join(r,search_file)
                location.append(res)
        return location
    except:
        drivesException()

# parallel process of searching file in drives
def multiThreading(filename, drives):
    try:
        results_ = []
        with concurrent.futures.ThreadPoolExecutor() as Executor:
            # submit method returns the file search update
            results = [Executor.submit(locate_file, filename, drive) for drive in drives] 
            for f in concurrent.futures.as_completed(results):
                results_.append(f.result())
        return results_
    except:
        multithreadException()

