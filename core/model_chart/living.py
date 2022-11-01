def livingBuider(data):
    return {
        'title': 'Viviendas',
        'description': 'Viviendas contruidos por sectores publicos y privados en un determinado estrato',
        'chart': {
            'type': 'pie',
            'data': {
                'labels': data['labels'],
                'datasets': [{
                    'label': 'Cantidad de vivienda construida',
                    'data': data['data'],
                    'backgroundColor': [
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(153, 102, 255, 0.2)',
                    ],
                    'borderColor': [
                        'rgb(54, 162, 235)',
                        'rgb(153, 102, 255)',
                    ],
                    'borderWidth': 1
                }],
                'hoverOffset': 4
            },
            'options': {
                'responsive': True,
                'title': {'display': True,
                          'text': 'Cantidad de construcciones por constructora',
                          'fontSize': 20
                          },
            }
        }
    }


def livingStratum(data):
    return {
        'title': '',
        'description': '',
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
                        'rgba(255, 99, 132, 0.2)',
                        'rgba(255, 159, 64, 0.2)',
                        'rgba(255, 205, 86, 0.2)',
                    ],
                    'borderColor': [
                        'rgb(75, 192, 192)',
                        'rgb(54, 162, 235)',
                        'rgb(153, 102, 255)',
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
                          'text': 'Cantida de viviendas por estrato',
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
