def calculate_metrics(tasks, num_vms):
    total_response_time = 0
    total_execution_time = 0
    missed_deadlines = 0
    max_completion_time = 0

    for task in tasks:
        response_time = task.start_time - task.arrival_time
        total_response_time += response_time

        total_execution_time += task.execution_time

        if task.completion_time > task.deadline:
            missed_deadlines += 1

        if task.completion_time > max_completion_time:
            max_completion_time = task.completion_time

    n = len(tasks)

    avg_response_time = total_response_time / n
    deadline_miss_rate = (missed_deadlines / n) * 100

    total_capacity_time = max_completion_time * num_vms
    cpu_utilization = (total_execution_time / total_capacity_time) * 100

    return {
        "avg_response_time": avg_response_time,
        "deadline_miss_rate": deadline_miss_rate,
        "cpu_utilization": cpu_utilization
    }
