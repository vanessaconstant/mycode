// Grab the macronutrient values

const fvCarb = Number(document.getElementById("fv-carb").innerText);
const fvPro = Number(document.getElementById("fv-pro").innerText);
const fvFat = Number(document.getElementById("fv-fat").innerText);
const total = fvCarb + fvPro + fvFat;

// Calculate the percentage of each macro
const perCarb = Math.round(100 * (fvCarb / total));
const perPro = Math.round(100 * (fvPro / total));
const perFat = Math.round(100 * (fvFat / total));

// Food View Pie Chart
var ctxP = document.getElementById("foodViewChart").getContext("2d");
var myPieChart2 = new Chart(ctxP, {
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
