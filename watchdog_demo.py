#! /usr/bin/env python
"""
Code adapted from watchdog demo https://github.com/gorakhargosh/watchdog

Usage:
    python watchdog_demo.py [-r] <dir>
    where -r will watch recursively, <dir> is the directory to watch
    
"""

import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

if __name__ == "__main__":
    args = len(sys.argv)
    if args == 3:
        if sys.argv[1] == '-r':
            recurse = True
        path = sys.argv[2]
    if args == 2:
        recurse = False
        path = sys.argv[1]
    if args == 1:
        print """Usage:\n\t
            python watchdog_demo.py [-r] <dir>  
            where -r will watch recursively, <dir> is the directory to watch"""
        exit()
        
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=recurse)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
