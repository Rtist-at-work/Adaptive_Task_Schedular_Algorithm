import copy
import matplotlib.pyplot as plt

from utils.task_generator import generate_tasks
from models.vm import VM

from schedulers.fcfs import fcfs_schedule
from schedulers.priority import priority_schedule
from schedulers.adaptive import adaptive_schedule
from schedulers.fuzzy import fuzzy_schedule   # <-- NEW

from utils.metrics import calculate_metrics


# large workload
tasks = generate_tasks(1000)

# create identical copies for fair comparison
tasks_fcfs = copy.deepcopy(tasks)
tasks_priority = copy.deepcopy(tasks)
tasks_adaptive = copy.deepcopy(tasks)
tasks_fuzzy = copy.deepcopy(tasks)   # <-- NEW

# VMs for each run
vms_fcfs = [VM(1,1), VM(2,1)]
vms_priority = [VM(1,1), VM(2,1)]
vms_adaptive = [VM(1,1), VM(2,1)]
vms_fuzzy = [VM(1,1), VM(2,1)]   # <-- NEW


# 1. Static FCFS
fcfs_scheduled = fcfs_schedule(tasks_fcfs, vms_fcfs)
fcfs_metrics = calculate_metrics(fcfs_scheduled, len(vms_fcfs))

# 2. Static Priority
priority_scheduled = priority_schedule(tasks_priority, vms_priority)
priority_metrics = calculate_metrics(priority_scheduled, len(vms_priority))

# 3. Adaptive
algo_used, adaptive_scheduled = adaptive_schedule(tasks_adaptive, vms_adaptive)
adaptive_metrics = calculate_metrics(adaptive_scheduled, len(vms_adaptive))

# 4. Fuzzy Scheduling  <-- NEW
fuzzy_scheduled = fuzzy_schedule(tasks_fuzzy, vms_fuzzy)
fuzzy_metrics = calculate_metrics(fuzzy_scheduled, len(vms_fuzzy))


print("Total tasks processed:", len(tasks))

print("\nStatic FCFS:")
print(f"Average Response Time: {fcfs_metrics['avg_response_time']:.2f} ms")
print(f"Deadline Miss Rate: {fcfs_metrics['deadline_miss_rate']:.2f}%")
print(f"CPU Utilization: {fcfs_metrics['cpu_utilization']:.2f}%")

print("\nStatic Priority:")
print(f"Average Response Time: {priority_metrics['avg_response_time']:.2f} ms")
print(f"Deadline Miss Rate: {priority_metrics['deadline_miss_rate']:.2f}%")
print(f"CPU Utilization: {priority_metrics['cpu_utilization']:.2f}%")

print("\nAdaptive Scheduling:")
print(f"Algorithm Chosen: {algo_used}")
print(f"Average Response Time: {adaptive_metrics['avg_response_time']:.2f} ms")
print(f"Deadline Miss Rate: {adaptive_metrics['deadline_miss_rate']:.2f}%")
print(f"CPU Utilization: {adaptive_metrics['cpu_utilization']:.2f}%")

print("\nFuzzy Scheduling:")   # <-- NEW
print(f"Average Response Time: {fuzzy_metrics['avg_response_time']:.2f} ms")
print(f"Deadline Miss Rate: {fuzzy_metrics['deadline_miss_rate']:.2f}%")
print(f"CPU Utilization: {fuzzy_metrics['cpu_utilization']:.2f}%")


# -------- Visualization --------

labels = ["FCFS","Priority","Adaptive","Fuzzy"]

response_times = [
    fcfs_metrics["avg_response_time"],
    priority_metrics["avg_response_time"],
    adaptive_metrics["avg_response_time"],
    fuzzy_metrics["avg_response_time"]   # <-- NEW
]

deadline_miss_rates = [
    fcfs_metrics["deadline_miss_rate"],
    priority_metrics["deadline_miss_rate"],
    adaptive_metrics["deadline_miss_rate"],
    fuzzy_metrics["deadline_miss_rate"]  # <-- NEW
]

# Plot 1
plt.figure()
plt.bar(labels, response_times)
plt.title("Average Response Time Comparison")
plt.xlabel("Scheduling Algorithm")
plt.ylabel("Response Time (ms)")
plt.show()

# Plot 2
plt.figure()
plt.bar(labels, deadline_miss_rates)
plt.title("Deadline Miss Rate Comparison")
plt.xlabel("Scheduling Algorithm")
plt.ylabel("Miss Rate (%)")
plt.show()
