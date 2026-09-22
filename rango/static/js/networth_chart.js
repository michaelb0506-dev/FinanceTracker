const ctx = document.getElementById('networthChart');

if (ctx) {
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: networthLabels,
            datasets: [{
                label: 'Net Worth',
                data: networthValues,
                borderColor: '#6699cc',
                backgroundColor: 'rgba(102, 153, 204, 0.2)',
                fill: true,
                tension: 0.2
            }]
        },
        options: {
            responsive: true
        }
    });
}