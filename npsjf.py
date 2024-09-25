def npSJF(ids, bursts, arrivals):
    n = len(ids)
    wt = [0] * n  # Waiting time for each process
    ct = [0] * n  # Completion time for each process
    tat = [0] * n  # Turnaround time for each process
    remainingTime = bursts[:]  # Remaining burst time for each process
    currentTime = 0
    completedTasks = 0

    while completedTasks < n:
        # Find the shortest job that has arrived and is not yet completed
        shortestTask = -1
        for j in range(n):
            if (arrivals[j] <= currentTime and remainingTime[j] > 0):
                if shortestTask == -1 or bursts[j] < bursts[shortestTask]:
                    shortestTask = j

        if shortestTask == -1:  # If no task is ready, increment the current time
            currentTime += 1
            continue

        # Execute the shortest task
        currentTime += bursts[shortestTask]
        remainingTime[shortestTask] = 0  # Mark the task as completed
        completedTasks += 1
        ct[shortestTask] = currentTime
        tat[shortestTask] = ct[shortestTask] - arrivals[shortestTask]
        wt[shortestTask] = tat[shortestTask] - bursts[shortestTask]

    return wt, ct, tat

def sjf_main():
    ids = [1, 2, 3, 4, 5]
    bursts = [6, 2, 8, 3, 4]
    arrivals = [2, 5, 1, 0, 4]

    wt, ct, tat = npSJF(ids, bursts, arrivals)

    print(f"{'ID':>5} {'AT':>5} {'BT':>5} {'CT':>5} {'TAT':>5} {'WT':>5}")
    for i in range(len(ids)):
        print(f"{ids[i]:>5} {arrivals[i]:>5} {bursts[i]:>5} {ct[i]:>5} {tat[i]:>5} {wt[i]:>5}")

sjf_main()
