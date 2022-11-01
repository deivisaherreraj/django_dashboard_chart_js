def vehicleYear(data):
    return {
        'title': 'Muertes violentas',
        'description': 'Cantida de muertes violentas por año.',
        'chart': {
            'type': 'bar',
            'data': {
                'labels': data['labels'],
                'datasets': [{
                    'label': 'Cantidad por año',
                    'data': data['data'],
                    'backgroundColor': [
                        'rgba(255, 99, 132, 0.2)',
                        'rgba(255, 159, 64, 0.2)',
                        'rgba(255, 205, 86, 0.2)',
                        'rgba(75, 192, 192, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(153, 102, 255, 0.2)',
                        'rgba(201, 203, 207, 0.2)'
                    ],
                    'borderColor': [
                        'rgb(255, 99, 132)',
                        'rgb(255, 159, 64)',
                        'rgb(255, 205, 86)',
                        'rgb(75, 192, 192)',
                        'rgb(54, 162, 235)',
                        'rgb(153, 102, 255)',
                        'rgb(201, 203, 207)'
                    ],
                    'borderWidth': 1
                }]
            },
            'options': {
                'responsive': True,
                'title': {'display': True,
                          'text': 'Vehiculos matriculados por año',
                          'fontSize': 20
                          },
                'scales': {
                    'yAxes': [{
                        'ticks': {
                            'beginAtZero': True
                        }
                    }]
                }
            }
        }
    }


def vehicleType(data):
    return {
        'title': 'Movilidad',
        'description': 'La matricula de vehiculo venia de baja desde el 2019 y la pandemia la complico.',
        'chart': {
            'type': 'bar',
            'data': {
                'labels': data['labels'],
                'datasets': [{
                    'label': 'Cantidad por tipo',
                    'data': data['data'],
                    'backgroundColor': [
                        'rgba(75, 192, 192, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(153, 102, 255, 0.2)',
                        'rgba(201, 203, 207, 0.2)'
                        'rgba(255, 99, 132, 0.2)',
                        'rgba(255, 159, 64, 0.2)',
                        'rgba(255, 205, 86, 0.2)',
                    ],
                    'borderColor': [
                        'rgb(75, 192, 192)',
                        'rgb(54, 162, 235)',
                        'rgb(153, 102, 255)',
                        'rgb(201, 203, 207)'
                        'rgb(255, 99, 132)',
                        'rgb(255, 159, 64)',
                        'rgb(255, 205, 86)',
                    ],
                    'borderWidth': 1
                }]
            },
            'options': {
                'responsive': True,
                'title': {'display': True,
                          'text': 'Vehiculos matriculados por tipo',
                          'fontSize': 20
                          },
                'scales': {
                    'yAxes': [{
                        'ticks': {
                            'beginAtZero': True
                        }
                    }]
                }
            }
        }
    }
