from collections import deque

def RoundRobin(ids, bursts, arrivals, ts):
    n = len(ids)
    wt = [0] * n  # Waiting time for each process
    ct = [0] * n  # Completion time for each process
    tat = [0] * n  # Turnaround time for each process
    remainingTime = bursts[:]  # Remaining burst time for each process
    RQ = deque()  # Ready Queue to hold process indices
    currentTime = 0
    completedTasks = 0

    # Add all processes that have arrived at time 0 to the Ready Queue
    for i in range(n):
        if arrivals[i] <= currentTime:
            RQ.append(i)

    while completedTasks < n:
        if not RQ:
            currentTime += 1
            for i in range(n):
                if arrivals[i] == currentTime:
                    RQ.append(i)
            continue

        curr = RQ.popleft()  # Get the process index from the front of the Ready Queue

        # Determine the time slice to execute
        timeSlice = min(ts, remainingTime[curr])
        currentTime += timeSlice
        remainingTime[curr] -= timeSlice

        # Add newly arrived processes to the Ready Queue
        for i in range(n):
            if arrivals[i] > currentTime - timeSlice and arrivals[i] <= currentTime and i not in RQ:
                RQ.append(i)

        # If the current process is not yet complete, put it back in the queue
        if remainingTime[curr] > 0:
            RQ.append(curr)
        else:
            # If the process is complete
            ct[curr] = currentTime
            tat[curr] = ct[curr] - arrivals[curr]
            wt[curr] = tat[curr] - bursts[curr]
            completedTasks += 1
    
    return wt, ct, tat

def rr_main():
    ids = [1, 2, 3, 4, 5]
    bursts = [8, 2, 7, 3, 5]
    arrivals = [0, 5, 1, 6, 8]
    ts = 3

    wt, ct, tat = RoundRobin(ids, bursts, arrivals, ts)

    print(f"{'ID':>5} {'AT':>5} {'BT':>5} {'CT':>5} {'TAT':>5} {'WT':>5}")
    for i in range(len(ids)):
        print(f"{ids[i]:>5} {arrivals[i]:>5} {bursts[i]:>5} {ct[i]:>5} {tat[i]:>5} {wt[i]:>5}")

rr_main()
