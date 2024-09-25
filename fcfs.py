def FCFS(ids, bursts, arrivals):
    n = len(ids)
    wt = [0] * n
    ct = [0] * n
    tat = [0] * n
    wait = 0
    
    for i in range(n):
        wt[i] = wait - arrivals[i]
        ct[i] = wait + bursts[i]
        tat[i] = ct[i] - arrivals[i]
        wait += bursts[i]
    
    return wt, ct, tat

def fcfs_main():
    ids = [1, 2, 3, 4, 5]
    bursts = [6, 2, 8, 3, 4]
    arrivals = [2, 5, 1, 0, 4]
    
    wt, ct, tat = FCFS(ids, bursts, arrivals)

    print(f"{'ID':>5} {'AT':>5} {'BT':>5} {'CT':>5} {'TAT':>5} {'WT':>5}")
    for i in range(len(ids)):
        print(f"{ids[i]:>5} {arrivals[i]:>5} {bursts[i]:>5} {ct[i]:>5} {tat[i]:>5} {wt[i]:>5}")

fcfs_main()
