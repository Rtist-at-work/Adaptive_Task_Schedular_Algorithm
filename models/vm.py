class VM:
    def __init__(self,vm_id,cpu_capacity):
        self.vm_id = vm_id
        self.cpu_capacity = cpu_capacity
        self.available_at = 0 # when this VM becomes free

    def __repr__(self):
        return(
            f"VM(id={self.vm_id}, available_at = {self.available_at}, cpu_capacity = {self.cpu_capacity})"
        )