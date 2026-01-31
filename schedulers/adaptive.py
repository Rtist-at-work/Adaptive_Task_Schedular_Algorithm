from schedulers.fcfs import fcfs_schedule
from schedulers.priority import priority_schedule

def adaptive_schedule(tasks, vms):
    total_tasks = len(tasks)
    high_priority_tasks = len([t for t in tasks if t.priority == "HIGH"])

    high_priority_ratio = high_priority_tasks / total_tasks

    if high_priority_ratio >= 0.4:
        selected_algorithm = "PRIORITY"
        scheduled_tasks = priority_schedule(tasks, vms)
    else:
        selected_algorithm = "FCFS"
        scheduled_tasks = fcfs_schedule(tasks, vms)

    return selected_algorithm, scheduled_tasks
