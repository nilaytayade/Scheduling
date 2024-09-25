def npPriority(ids, bursts, arrivals, priorities):
    n = len(ids)
    wt = [0] * n   # Waiting time for each process
    ct = [0] * n   # Completion time for each process
    tat = [0] * n  # Turnaround time for each process
    isCompleted = [False] * n  # Track completed processes
    currentTime = 0
    completedTasks = 0

    while completedTasks < n:
        # Find the highest priority task that is ready to run
        HPT = -1  # High Priority Task index
        for j in range(n):
            if (arrivals[j] <= currentTime and not isCompleted[j]):
                if HPT == -1 or priorities[j] < priorities[HPT]:
                    HPT = j

        if HPT == -1:  # If no task is ready, increment the current time
            currentTime += 1
            continue

        # Process the selected high priority task
        currentTime += bursts[HPT]
        ct[HPT] = currentTime
        tat[HPT] = ct[HPT] - arrivals[HPT]
        wt[HPT] = tat[HPT] - bursts[HPT]
        isCompleted[HPT] = True
        completedTasks += 1
    
    return wt, ct, tat

def priority_main():
    ids = [1, 2, 3, 4, 5]
    bursts = [11, 28, 2, 10, 16]
    arrivals = [0, 5, 12, 2, 9]
    priorities = [2, 0, 3, 1, 4]

    wt, ct, tat = npPriority(ids, bursts, arrivals, priorities)

    print(f"{'ID':>5} {'AT':>5} {'BT':>5} {'CT':>5} {'TAT':>5} {'WT':>5}")
    for i in range(len(ids)):
        print(f"{ids[i]:>5} {arrivals[i]:>5} {bursts[i]:>5} {ct[i]:>5} {tat[i]:>5} {wt[i]:>5}")

priority_main()
