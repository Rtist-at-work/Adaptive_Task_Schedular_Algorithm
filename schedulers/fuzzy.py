def fuzzy_schedule(tasks, vms):

    time = 0
    remaining = tasks[:]
    completed = []

    def priority_val(p):
        return {"HIGH":1.0,"MEDIUM":0.6,"LOW":0.3}[p]

    while remaining:

        # ready tasks at current time
        ready = [t for t in remaining if t.arrival_time <= time]

        if not ready:
            time += 1
            continue

        for task in ready:

            slack = task.deadline - (time + task.execution_time)

            urgency = 1/(slack+1) if slack>=0 else 1.5
            length = 1/task.execution_time

            task.fuzzy_score = (
                0.4*urgency +
                0.35*priority_val(task.priority) +
                0.25*length
            )

        best = max(ready,key=lambda t:t.fuzzy_score)

        vm = min(vms,key=lambda v:v.available_at)

        start = max(time,vm.available_at,best.arrival_time)
        finish = start + best.execution_time

        best.start_time = start
        best.completion_time = finish
        best.waiting_time = start - best.arrival_time
        best.response_time = best.waiting_time
        best.deadline_met = finish <= best.deadline

        vm.available_at = finish
        time = start

        completed.append(best)
        remaining.remove(best)

    return completed
