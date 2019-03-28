import threading
import httplib

class SlowServerClient:
    def __init__(self):
        self._counter_around_io = 0
        self._counter_protected_by_gil = 0

    def request(self):
        num_requests = self._counter_around_io
        conn = httplib.HTTPConnection("localhost:8000")
        conn.request("GET", "/")
        response = conn.getresponse()
        print(response.status, response.read())
        self._counter_around_io = num_requests + 1
        self._counter_protected_by_gil += 1

    def get_counter_around_io(self):
        return self._counter_around_io

    def get_counter_protected_by_gil(self):
        return self._counter_protected_by_gil



client = SlowServerClient()

class RequestThread(threading.Thread):
    def run(self):
        for _ in range(10):
            client.request()


def main():
    thread1 = RequestThread()
    thread2 = RequestThread()

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("Counter around IO: {}".format(client.get_counter_around_io()))
    print("Counter protected by GIL: {}".format(client.get_counter_protected_by_gil()))


if __name__ == '__main__':
    main()
