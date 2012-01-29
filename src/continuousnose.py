import time
import logging
import subprocess
from watchdog.events        import PatternMatchingEventHandler
from watchdog.observers     import Observer

class UniqueTimeHandler(PatternMatchingEventHandler):

    def __init__(self, event_queue, argv, patterns=None, ignore_patterns=None,
                         ignore_directories=False, case_sensitive=False):
        """
        args:
            event_queue : brownie.datastructures.SetQueue
            argv        : list
        """
        self.event_queue = event_queue
        self.argv = argv
        super(UniqueTimeHandler,self).__init__(patterns, ignore_patterns, ignore_directories, case_sensitive)

    def on_any_event(self, event):
        self.event_queue.queue.clear()
        self.is_running = True
        logging.info("[%s] %s" % (event._event_type.upper(), event._src_path))
        cmd = ['./env/bin/nosetests', '-s', '--rednose']
        map(cmd.append, self.argv)
        subprocess.call(cmd)
        print '-' * 10

class ContinuousNose(object):

    def __init__(self, options, patterns=['*.py'], dirs=[]):
        self.target_patterns = patterns
        self.target_dirs = dirs
        self.argv = []
        if len(options) > 0:
            self.argv = options

    def run(self):
        observer = Observer(timeout=3)
        event_handler = UniqueTimeHandler(observer.event_queue, self.argv,
                                            patterns=self.target_patterns)
        for dir in self.target_dirs:
            observer.schedule(event_handler, path=dir, recursive=True)
        observer.schedule(event_handler, path='.', recursive=False)
        observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()
