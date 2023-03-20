#Vasīlijs Dvils-Dmitrijevs 221RDB381

def parallel_processing(n, m, data):
    output = []
    next_available = {i: 0 for i in range(n)}

    for i in range(m):
        thread = min(next_available, key=next_available.get)
        start_time = next_available[thread]
        end_time = start_time + data[i]
        output.append((thread, start_time))
        next_available[thread] = end_time

    return output


def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    result = parallel_processing(n, m, data)

    for i in range(m):
        print(result[i][0], result[i][1])


if __name__ == "__main__":
    main()
