const main = () => {
  const data = {
    sausage,
    bottled_water,
    tropical_fruit,
    root_vegetables,
    yogurt,
    soda,
    rolls_buns,
    other_vegetables,
    whole_milk,
  };
  labels = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
    22, 23, 24, 25, 26, 27, 28, 29, 30,
  ];
  const container = document.getElementById('container');
  console.log(data['sausage']['data']);

  let ctx = document.getElementById('myChart').getContext('2d');
  const config = {
    type: 'line',
    data: {
      labels,
      datasets: [
        {
          label: 'sausage',
          borderColor: '#081c15',
          borderWidth: 1,
          radius: 0,
          data: data['sausage']['data'],
          tension: 0.2,
        },
        {
          label: 'bottled_water',
          borderColor: '#081c15',
          borderWidth: 1,
          radius: 0,
          data: data['bottled_water']['data'],
          tension: 0.2,
        },
        {
          label: 'tropical_fruit',
          borderColor: '#081c15',
          borderWidth: 1,
          radius: 0,
          data: data['tropical_fruit']['data'],
          tension: 0.2,
        },
        {
          label: 'root_vegetables',
          borderColor: '#081c15',
          borderWidth: 1,
          radius: 0,
          data: data['root_vegetables']['data'],
          tension: 0.2,
        },
        {
          label: 'yogurt',
          borderColor: '#081c15',
          borderWidth: 1,
          radius: 0,
          data: data['yogurt']['data'],
          tension: 0.2,
        },
        {
          label: 'soda',
          borderColor: '#081c15',
          borderWidth: 1,
          radius: 0,
          data: data['soda']['data'],
          tension: 0.2,
        },
        {
          label: 'rolls_buns',
          borderColor: '#081c15',
          borderWidth: 1,
          radius: 0,
          data: data['rolls_buns']['data'],
          tension: 0.2,
        },
        {
          label: 'other_vegetables',
          borderColor: '#081c15',
          borderWidth: 1,
          radius: 0,
          data: data['other_vegetables']['data'],
          tension: 0.2,
        },
        {
          label: 'whole_milk',
          borderColor: '#081c15',
          borderWidth: 1,
          radius: 0,
          data: data['whole_milk']['data'],
          tension: 0.2,
        },
      ],
    },
    options: {
      interaction: {
        mode: 'index',
        intersect: false,
      },
      plugins: {
        legend: {
          position: 'top',
        },
        title: {
          display: true,
          text: 'Demand Forecast (For the next 30 Days)',
        },
      },
      scales: {
        x: {
          display: true,
          title: {
            display: true,
            text: 'Days',
          },
        },
      },
    },
  };
  let myChart = new Chart(ctx, config);

};

main();
