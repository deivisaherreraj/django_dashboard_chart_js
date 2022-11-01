
def infrastructureRoadType(data):
    return {
        'title': 'Infraestructura vial',
        'description': 'La infraestrucutura vial de Cartagena no crece desde el año 2012',
        'chart': {
            'type': 'pie',
            'data': {
                'labels': data['labels'],
                'datasets': [{
                    'label': 'Cantidad de vivienda construida',
                    'data': data['data'],
                    'backgroundColor': [
                        'rgba(255, 205, 86, 0.2)',
                        'rgba(75, 192, 192, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(153, 102, 255, 0.2)',
                    ],
                    'borderColor': [
                        'rgb(255, 205, 86)',
                        'rgb(75, 192, 192)',
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
                          'text': 'Cantidad de infraestructura vial por tipo',
                          'fontSize': 20
                          },
            }
        }
    }


def infrastructureRoadState(data):
    return {
        'title': 'Infraestructura vial',
        'description': 'La infraestrucutura vial de Cartagena no crece desde el año 2012',
        'chart': {
            'type': 'pie',
            'data': {
                'labels': data['labels'],
                'datasets': [{
                    'label': 'Cantidad de vivienda construida',
                    'data': data['data'],
                    'backgroundColor': [
                        'rgba(255, 159, 64, 0.2)',
                        'rgba(255, 205, 86, 0.2)',
                        'rgba(75, 192, 192, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                    ],
                    'borderColor': [
                        'rgb(255, 159, 64)',
                        'rgb(255, 205, 86)',
                        'rgb(75, 192, 192)',
                        'rgb(54, 162, 235)',
                    ],
                    'borderWidth': 1
                }],
                'hoverOffset': 4
            },
            'options': {
                'responsive': True,
                'title': {'display': True,
                          'text': 'Cantidad de infraestrutura por tipo de estado',
                          'fontSize': 20
                          },
            }
        }
    }
