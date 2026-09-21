const ctx = document.getElementById('categoryChart');

new Chart(ctx, {
    type: 'pie',
    data: {
        labels: categoryLabels,
        datasets: [{
            label: 'Spending by Category',
            data: categoryValues,
            backgroundColor: [
                '#6699cc',
                '#88bb88',
                '#cc8866',
                '#aa77bb',
                '#cccc66',
                '#66cccc'
            ]
        }]
    },
    options: {
        responsive: true
    }
});