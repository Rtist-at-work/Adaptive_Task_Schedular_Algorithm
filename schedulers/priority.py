def priority_schedule(tasks, vms):
    # Priority order mapping
    priority_order = {"HIGH": 1, "MEDIUM": 2, "LOW": 3}

    # Sort tasks by priority, then arrival time
    sorted_tasks = sorted(
        tasks,
        key=lambda t: (priority_order[t.priority], t.arrival_time)
    )

    for task in sorted_tasks:
        # Pick earliest available VM
        vm = min(vms, key=lambda v: v.available_at)

        start_time = max(task.arrival_time, vm.available_at)
        completion_time = start_time + task.execution_time

        # Update task metrics
        task.start_time = start_time
        task.completion_time = completion_time
        task.waiting_time = start_time - task.arrival_time
        task.response_time = task.waiting_time
        task.deadline_met = completion_time <= task.deadline

        # Update VM
        vm.available_at = completion_time

    return sorted_tasks
