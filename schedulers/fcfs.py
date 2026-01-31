def fcfs_schedule(tasks, vms):
    current_time = 0

    for task in tasks:
        # Find the earliest available VM
        vm = min(vms, key=lambda v: v.available_at)

        start_time = max(task.arrival_time, vm.available_at)
        completion_time = start_time + task.execution_time

        # Update task metrics
        task.start_time = start_time
        task.completion_time = completion_time
        task.waiting_time = start_time - task.arrival_time
        task.response_time = task.waiting_time
        task.deadline_met = completion_time <= task.deadline

        # Update VM availability
        vm.available_at = completion_time

    return tasks
