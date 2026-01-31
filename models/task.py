class Task:
    def __init__(self, task_id, arrival_time, execution_time, deadline, priority):
        self.task_id = task_id
        self.arrival_time = arrival_time
        self.execution_time = execution_time
        self.deadline = deadline
        self.priority = priority

        # these will be set during scheduling
        self.start_time = None
        self.completion_time = None
        self.waiting_time = None
        self.response_time = None
        self.deadline_time = None

    # returns string format for the receiving object 
    def __repr__(self):
        return (
            f"Task(id={self.task_id})"
            f"priority(id={self.priority})"
            f"execution_time(id={self.execution_time})"
            f"arrival_time(id={self.arrival_time})"
            f"deadline(id={self.deadline})"
        )        