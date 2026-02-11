def priority_schedule(tasks, vms):

    tasks = sorted(tasks, key=lambda t: t.arrival_time)

    time = 0
    completed = []
    pending = tasks[:]

    while pending:

        # tasks that have arrived
        available = [t for t in pending if t.arrival_time <= time]

        if not available:
            time = pending[0].arrival_time
            continue

        # pick highest priority among available
        priority_order = {"HIGH": 3, "MEDIUM": 2, "LOW": 1}

        task = max(
            available,
            key=lambda t: priority_order[t.priority]
        )

        vm = min(vms, key=lambda v: v.available_at)

        start = max(task.arrival_time, vm.available_at)
        finish = start + task.execution_time

        task.start_time = start
        task.completion_time = finish
        task.waiting_time = start - task.arrival_time
        task.response_time = task.waiting_time
        task.deadline_met = finish <= task.deadline

        vm.available_at = finish

        time = start
        pending.remove(task)
        completed.append(task)

    return completed
