let chart; // global for chart reuse

function run() {
  fetch("/run")
    .then((res) => res.json())
    .then((data) => {
      // ===== SYSTEM INFO =====
      document.getElementById("algo").innerText = data.chosen;
      document.getElementById("avgJob").innerText = data.avg_job;

      document.getElementById("load").innerText = "SYSTEM LOAD: " + data.load;

      document.getElementById("check").innerHTML =
        `High priority tasks: ${data.high}<br>
             Urgent tasks: ${data.urgent}<br>
             Avg job time: ${data.avg_job}`;

      document.getElementById("decision").innerHTML =
        `Reason: ${data.reason}<br>
             Chosen Algorithm: ${data.chosen}`;

      // ===== METRICS =====
      document.getElementById("m1").innerHTML = `<h4>FCFS</h4>
             Avg RT: ${data.fcfs.avg_response_time} ms<br>
             Miss Rate: ${data.fcfs.deadline_miss_rate}%<br>
             CPU: ${data.fcfs.cpu_utilization}%`;

      document.getElementById("m2").innerHTML = `<h4>Priority</h4>
             Avg RT: ${data.priority.avg_response_time} ms<br>
             Miss Rate: ${data.priority.deadline_miss_rate}%<br>
             CPU: ${data.priority.cpu_utilization}%`;

      document.getElementById("m3").innerHTML = `<h4>Adaptive</h4>
             Avg RT: ${data.adaptive.avg_response_time} ms<br>
             Miss Rate: ${data.adaptive.deadline_miss_rate}%<br>
             CPU: ${data.adaptive.cpu_utilization}%`;

      // ===== CHART =====
      const ctx = document.getElementById("chart");

      if (chart) chart.destroy();

      chart = new Chart(ctx, {
        type: "bar",
        data: {
          labels: ["FCFS", "Priority", "Adaptive", "Fuzzy"],
          datasets: [
            {
              label: "Avg Response Time",
              data: [
                data.fcfs.avg_response_time,
                data.priority.avg_response_time,
                data.adaptive.avg_response_time,
                data.fuzzy.avg_response_time,
              ],
            },
          ],
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
        },
      });
    });
}
