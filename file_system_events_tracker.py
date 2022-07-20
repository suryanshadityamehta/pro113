import time
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/hp/Downloads"

# Event Hanlder Class
class FileEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(event)

# Initialize Event Handler Class
event_handler = FileEventHandler()

# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()