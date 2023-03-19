# python3
import threading

class PriorityQueue:
    def __init__(self, n):
        self.heap = [(0, i) for i in range(n)]
        self.size = n
        self.lock = threading.Lock()

    def push(self, item, priority):
        with self.lock:
            self.heap.append((priority, item))
            self.size += 1
            self._siftup(self.size - 1)

    def pop(self):
        with self.lock:
            lastelt = self.heap.pop()
            self.size -= 1
            if self.heap:
                returnitem = self.heap[0]
                self.heap[0] = lastelt
                self._siftdown(0)
            else:
                returnitem = lastelt
            return returnitem

    def _siftup(self, pos):
        if pos > 0:
            parentpos = (pos - 1) >> 1
            if self.heap[pos][0] < self.heap[parentpos][0]:
                self.heap[pos], self.heap[parentpos] = self.heap[parentpos], self.heap[pos]
                self._siftup(parentpos)

    def _siftdown(self, pos):
        childpos = (pos << 1) + 1
        if childpos < self.size:
            rightpos = childpos + 1
            if rightpos < self.size and not self.heap[childpos][0] < self.heap[rightpos][0]:
                childpos = rightpos
            if not self.heap[pos][0] < self.heap[childpos][0]:
                self.heap[pos], self.heap[childpos] = self.heap[childpos], self.heap[pos]
                self._siftdown(childpos)

def parallel_processing(n, m, data):
    output = []
    pq = PriorityQueue(n)

    def process(i):
        t = 0
        while True:
            item = pq.pop()
            with pq.lock:
                if item[0] > t:
                    pq.push(item[1], item[0])
                    continue
                output.append((i, t))
                t += data[i]
                if i + n < m:
                    pq.push(i + n, t)
                break

    threads = [threading.Thread(target=process, args=(i,)) for i in range(n)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    return output


def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    result = parallel_processing(n, m, data)

    for i in range(m):
        print(result[i][0], result[i][1])


if __name__ == "__main__":
    main()
