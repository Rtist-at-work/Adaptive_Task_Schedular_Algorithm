import random
from models.task import Task

def generate_tasks(num_tasks):

    tasks = []
    current_time = 0

    scenario = random.choice([
        "DEADLINE_HEAVY",
        "PRIORITY_HEAVY",
        "SHORT_JOBS",
        "MIXED"
    ])

    print("SCENARIO:", scenario)

    for i in range(num_tasks):

        # arrival pattern
        if scenario == "DEADLINE_HEAVY":
            current_time += random.randint(0,2)

        elif scenario == "PRIORITY_HEAVY":
            current_time += random.randint(1,3)

        elif scenario == "SHORT_JOBS":
            current_time += random.randint(2,5)

        else:  # MIXED
            current_time += random.randint(0,4)

        # execution time
        if scenario == "SHORT_JOBS":
            execution_time = random.randint(1,4)

        elif scenario == "DEADLINE_HEAVY":
            execution_time = random.randint(4,10)

        else:
            execution_time = random.randint(1,12)

        # priority distribution
        if scenario == "PRIORITY_HEAVY":
            priority = random.choices(
                ["HIGH","MEDIUM","LOW"],
                weights=[0.6,0.3,0.1]
            )[0]
        else:
            priority = random.choice(["HIGH","MEDIUM","LOW"])

        # deadline logic
        if scenario == "DEADLINE_HEAVY":
            slack = random.randint(1,3)   # many urgent tasks

        elif priority == "HIGH":
            slack = random.randint(3,8)

        elif priority == "MEDIUM":
            slack = random.randint(6,15)

        else:
            slack = random.randint(10,25)

        deadline = current_time + execution_time + slack

        tasks.append(Task(
            task_id=i+1,
            arrival_time=current_time,
            execution_time=execution_time,
            deadline=deadline,
            priority=priority
        ))

    return tasks
