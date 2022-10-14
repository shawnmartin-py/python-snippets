class ThreadingMixIn:
    def process_request(self):
        ...

class BaseServer:
    def process_request(self):
        ...

class MyService(ThreadingMixIn, BaseServer):
    ...