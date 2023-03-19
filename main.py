# python3

def parallel_processing(n, m, data):
    output = []
    thread = [0] * n

    for i in range(m):
        threadnxt = 0
        for j in range(1, n):
            if thread[j] < thread[threadnxt]:
                threadnxt = j
        x = thread[threadnxt]
        y = x + data[i]
        thread[threadnxt] = y
        output.append((threadnxt, x))
    return output

def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    result = parallel_processing(n, m, data)

    for i in range(m):
        print(result[i][0], result[i][1])
