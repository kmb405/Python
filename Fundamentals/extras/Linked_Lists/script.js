// Select DOM elements
const chartTypeSelect = document.getElementById("chart-type");
const datasetInput = document.getElementById("dataset");
const labelsInput = document.getElementById("labels");
const colorInput = document.getElementById("color-scheme");
const generateButton = document.getElementById("generate-button");
const chartCanvas = document.getElementById("myChart");

// generateButton.addEventListener("click", () => {
//   const chartType = chartTypeSelect.value;
//   const dataset = parseDataset(datasetInput.value); // Function to parse comma-separated values
//   const labels = parseLabels(labelsInput.value);
//   const color = colorInput.value;

//   // Clear any previous chart
//   if (window.myChart) {
//     window.myChart.destroy();
//   }

//   // Generate Chart.js chart
//   if (chartType === "line" || chartType === "bar" || chartType === "pie") {
//     createChartJsChart(chartCanvas, chartType, dataset, labels, color);
//   } else {
//     // Handle D3.js or other libraries as needed
//     createD3Chart(chartCanvas, chartType, dataset, labels, color);
//   }
// });

// // Example Chart.js creation function (replace with D3 or other library as needed)
// function createChartJsChart(canvas, type, data, labels, color) {
//   window.myChart = new Chart(canvas, {
//     type: type,
//     data: {
//       labels: labels,
//       datasets: [
//         {
//           data: data,
//           backgroundColor: color, // Or an array of colors for multi-color charts
//           // ... other Chart.js options
//         },
//       ],
//     },
//     // ... other Chart.js options
//   });
// }

// function parseDataset(str) {
//   return str.split(",").map(Number);
// }

// function parseLabels(str) {
//   return str.split(",").map(String.trim);
// }

// ... (DOM element selections)

generateButton.addEventListener("click", () => {
  const chartType = chartTypeSelect.value;
  const dataset = parseDataset(datasetInput.value);
  const labels = parseLabels(labelsInput.value);
  const color = colorInput.value;

  createChartJsChart(chartCanvas, chartType, dataset, labels, color);
});

function createChartJsChart(canvas, type, data, labels, color) {
  window.myChart = new Chart(canvas, {
    type: type,
    data: {
      labels: labels,
      datasets: [
        {
          data: data,
          backgroundColor: color, // Or an array of colors for multi-color charts
          borderColor: color, // Add border color for visual clarity
          // ... other Chart.js options
        },
      ],
    },
    // ... other Chart.js options
  });
}

// Helper functions
function parseDataset(str) {
  return str.split(",");
}

function parseLabels(str) {
  return str.split(",");
}
