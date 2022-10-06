// Dashboard Pie Chart

var ctx = document.getElementById("pieChart").getContext("2d");
var myPieChart = new Chart(ctx, {
  type: "pie",
  data: {
    labels: ["Carbs", "Proteins", "Fat"],
    datasets: [
      {
        data: [100, 100, 100],
        backgroundColor: ["#F7464A", "#46BFBD", "#FDB45C"],
        hoverBackgroundColor: ["#FF5A5E", "#5AD3D1", "#FFC870"],
      },
    ],
  },
  options: {
    responsive: true,
  },
});
