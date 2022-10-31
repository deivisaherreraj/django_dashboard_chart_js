def violenceGender2020(data):
    return {
        'title': 'Volencia Domestica',
        'description': 'La violencia intrafamiliar va en aumento y según los resultados, las mujeres son las más afectadas.',
        'chart': {
            'type': 'pie',
            'data': {
                'labels': data['labels'],
                'datasets': [{
                    'label': 'Cantidad por genero',
                    'data': data['data'],
                    'backgroundColor': [
                        'rgba(255, 205, 86, 0.2)',
                        'rgba(75, 192, 192, 0.2)',
                    ],
                    'borderColor': [
                        'rgb(255, 205, 86)',
                        'rgb(75, 192, 192)',
                    ],
                    'borderWidth': 1
                }],
                'hoverOffset': 4
            },
            'options': {
                'responsive': True,
                'title': {'display': True,
                          'text': 'Violencia infrafamiliar por genero para el año 2020',
                          'fontSize': 20
                          },
            }
        }
    }


def violenceGender2021(data):
    return {
        'title': 'Volencia Domestica',
        'description': 'La violencia intrafamiliar va en aumento y según los resultados, las mujeres son las más afectadas.',
        'chart': {
            'type': 'pie',
            'data': {
                'labels': data['labels'],
                'datasets': [{
                    'label': 'Cantidad por genero',
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
                          'text': 'Violencia infrafamiliar por genero para el año 2021',
                          'fontSize': 20
                          },
            }
        }
    }
