def count_passengers(passenger_times, T):
    count=0
    for entry_time, exit_time in passenger_times:
        if entry_time <= T <= exit_time:
            count += 1
    return count

if __name__ == "__main__":
    N = int(input(""))
    passenger_times = []
    for _ in range(N):
        A, B = map(int, input().split())
        passenger_times.append((A, B))
    T = int(input(""))
    result = count_passengers(passenger_times, T)
    print(result)