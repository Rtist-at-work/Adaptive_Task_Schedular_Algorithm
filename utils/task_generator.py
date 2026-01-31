import random
from models.task import Task

def generate_tasks(num_tasks):
    tasks = []

    for i in range(num_tasks):
        arrival_time = i 
        execution_time = random.randint(1,10)

        priority = random.choice(["HIGH","MEDIUM","LOW"])

        if priority == "HIGH":
            deadline = arrival_time + execution_time + 5
        elif priority == "MEDIUM":
            deadline = arrival_time + execution_time + 10
        else :
            deadline = arrival_time + execution_time + 15

        task = Task(
                task_id=i + 1,
                arrival_time=arrival_time,
                execution_time=execution_time,
                deadline=deadline,
                priority=priority
            )
        tasks.append(task)



    return tasks
