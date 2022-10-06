const dashCarb = Number(document.getElementById("dash-carb").innerText);
const dashPro = Number(document.getElementById("dash-pro").innerText);
const dashFat = Number(document.getElementById("dash-fat").innerText);
const total = dashCarb + dashPro + dashFat;

// Calculate the percentage of each macro
const perCarb = Math.round(100 * (dashCarb / total));
const perPro = Math.round(100 * (dashPro / total));
const perFat = Math.round(100 * (dashFat / total));

// Dashboard Pie Chart

var ctx = document.getElementById("pieChart").getContext("2d");
var myPieChart = new Chart(ctx, {
  type: "pie",
  data: {
    labels: [`Carbs: ${perCarb}% `, `Proteins: ${perPro}%`, `Fat: ${perFat}%`],
    datasets: [
      {
        data: [perCarb, perPro, perFat],
        backgroundColor: ["#F7464A", "#46BFBD", "#FDB45C"],
        hoverBackgroundColor: ["#FF5A5E", "#5AD3D1", "#FFC870"],
      },
    ],
  },
  options: {
    responsive: true,
  },
});
