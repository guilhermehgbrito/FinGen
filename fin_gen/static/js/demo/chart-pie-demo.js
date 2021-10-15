// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';

let atividadesPie = document.querySelector('input#atividades-pie').value
var ctx = document.getElementById("myPieChart");

if (atividadesPie == 'None') {
  ctx.parentElement.classList.add('text-center')
  ctx.parentElement.innerText = 'Ainda sem atividades. Bora começar?'
} else {
  let atividadeData = atividadesPie.split(';').map((value) => {
    return value.split(',').map((value) => value.replace(/[\(\)<>\']+/g, ''))
  })
  let divLegend = document.querySelector('div#pie-legend')
  atividadeData.forEach((value) => {
    let span = document.createElement('span')
    span.classList.add('mr-2')
    let i = document.createElement('i')
    i.classList.add('fas', 'fa-circle')
    i.style.color = `${value[2].replace(/[\s]+/g, '')}df`
    span.appendChild(i)
    span.innerHTML += ` ${value[0]}`
    divLegend.appendChild(span)
  })
  
  // Pie Chart Example
  var myPieChart = new Chart(ctx, {
    type: 'doughnut',
    data: {
      labels: atividadeData.map((value) => value[0]),
      datasets: [{
        data: atividadeData.map((value) => Number(value[1])),
        backgroundColor: atividadeData.map((value) => `${value[2].replace(/[\'\s]+/g, '')}cf`),
        hoverBackgroundColor: atividadeData.map((value) => `${value[2].replace(/[\'\s]+/g, '')}ff`),
        hoverBorderColor: "rgba(234, 236, 244, 1)",
      }],
    },
    options: {
      maintainAspectRatio: false,
      tooltips: {
        backgroundColor: "rgb(255,255,255)",
        bodyFontColor: "#858796",
        borderColor: '#dddfeb',
        borderWidth: 1,
        xPadding: 15,
        yPadding: 15,
        displayColors: false,
        caretPadding: 10,
      },
      legend: {
        display: false
      },
      cutoutPercentage: 80,
    },
  });
}
