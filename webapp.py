from flask import Flask, render_template, jsonify
import copy

from utils.task_generator import generate_tasks
from models.vm import VM

from schedulers.fcfs import fcfs_schedule
from schedulers.priority import priority_schedule
from schedulers.adaptive import adaptive_schedule
from schedulers.fuzzy import fuzzy_schedule
from utils.metrics import calculate_metrics

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("dashboard.html")

@app.route("/run")
def run():

    tasks = generate_tasks(1000)
    vms = [VM(1,1), VM(2,1), VM(3,1)]

    total = len(tasks)

    high = len([t for t in tasks if t.priority=="HIGH"])
    urgent = len([
        t for t in tasks
        if (t.deadline-(t.arrival_time+t.execution_time))<=5
    ])

    avg_job = sum(t.execution_time for t in tasks)/total

    # load level
    if avg_job > 8:
        load="OVERLOAD"
    elif avg_job > 5:
        load="NORMAL"
    else:
        load="UNDERLOAD"

    # reason logic
    if urgent/total > 0.3:
        reason="Many tasks have tight deadlines."
    elif high/total > 0.4:
        reason="Large number of HIGH priority tasks."
    else:
        reason="Mixed workload."

    fcfs = calculate_metrics(
        fcfs_schedule(copy.deepcopy(tasks),copy.deepcopy(vms)),3)

    priority = calculate_metrics(
        priority_schedule(copy.deepcopy(tasks),copy.deepcopy(vms)),3)

    algo, adaptive_tasks = adaptive_schedule(
        copy.deepcopy(tasks),copy.deepcopy(vms))

    adaptive = calculate_metrics(adaptive_tasks,3)

    fuzzy = calculate_metrics(
        fuzzy_schedule(copy.deepcopy(tasks),copy.deepcopy(vms)),3)

    return jsonify({
        "load":load,
        "high":high,
        "urgent":urgent,
        "avg_job":round(avg_job,1),
        "reason":reason,
        "chosen":algo,
        "fcfs":fcfs,
        "priority":priority,
        "adaptive":adaptive,
        "fuzzy":fuzzy
    })

if __name__=="__main__":
    app.run(debug=True)
