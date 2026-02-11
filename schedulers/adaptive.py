from schedulers.fcfs import fcfs_schedule
from schedulers.priority import priority_schedule
from schedulers.fuzzy import fuzzy_schedule

def adaptive_schedule(tasks, vms):

    total = len(tasks)

    high_priority = len([t for t in tasks if t.priority == "HIGH"])

    urgent_tasks = len([
        t for t in tasks
        if (t.deadline - (t.arrival_time + t.execution_time)) <= 3
    ])

    avg_exec = sum(t.execution_time for t in tasks) / total

    high_ratio = high_priority / total
    urgent_ratio = urgent_tasks / total

    print("\nSystem Check:")
    print(f"- {high_priority} high priority tasks")
    print(f"- {urgent_tasks} urgent tasks")
    print(f"- Avg job time: {avg_exec:.1f}")

    if urgent_ratio > 0.35:
        print("\nReason: Many tight deadlines")
        print("Choosing Fuzzy\n")
        return "FUZZY", fuzzy_schedule(tasks, vms)

    elif high_ratio > 0.45:
        print("\nReason: Many high priority tasks")
        print("Choosing Priority\n")
        return "PRIORITY", priority_schedule(tasks, vms)

    elif avg_exec <= 5:
        print("\nReason: Jobs are short")
        print("Choosing FCFS\n")
        return "FCFS", fcfs_schedule(tasks, vms)

    else:
        print("\nReason: Mixed workload")
        print("Choosing Priority\n")
        return "PRIORITY", priority_schedule(tasks, vms)
