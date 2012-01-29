import subprocess
import time
from watchdog.events        import PatternMatchingEventHandler
from watchdog.observers     import Observer
from watchdog.observers.api import ObservedWatch, \
                                   BaseObserver, \
                                   EventEmitter, \
                                   EventDispatcher, \
                                   EventQueue

argv = []

def run_test():
    global argv
    cmd = ['./env/bin/nosetests', '-s', '--rednose']
    map(cmd.append, argv)
    subprocess.call(cmd)
    print '-' * 10

class MyHandler(PatternMatchingEventHandler):

    def __init__(self, patterns=None, ignore_patterns=None,
                         ignore_directories=False, case_sensitive=False):
        self.is_running = False
        super(MyHandler,self).__init__(self, patterns, ignore_patterns, ignore_directories, case_sensitive)
        
    def on_any_event(self, event):
        if self.is_running == True:
            return
        self.is_running = True
        print "[%s] %s" % (event._event_type.upper(), event._src_path)
        run_test()
        time.sleep(1)
        self.is_running = False

class MyEmitter(EventEmitter):
   def queue_event(self, event):
        super(MyEmitter,self).queue_event(event)

class NoseContinuous(object):

    def __init__(self, options, patterns=['*.py'], dirs=['test','lib']):
        self.target_patterns = patterns
        self.target_dirs = dirs
        self.argv = []
        if len(options)>0:
            self.argv = options

        self.event_queue = EventQueue()
        self.watch = ObservedWatch('.', True)
        self.emitter = MyEmitter(self.event_queue, self.watch, timeout=1)
        self.observer = BaseObserver(self.emitter)

    def run(self):
        event_handler = MyHandler(patterns=self.target_patterns)


        observer = Observer()
        for dir in self.target_dirs:
            observer.schedule(event_handler, path=dir, recursive=True)
        observer.schedule(event_handler, path='.', recursive=False)

        observer.start()
        try:
            while True:
                time.sleep(0.5)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()

