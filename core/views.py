from core.model_chart.infrastructure_road import infrastructureRoadState, infrastructureRoadType
from core.model_chart.domestic_violence import violenceGender2020, violenceGender2021
from django.shortcuts import render
from django.db.models import Count
import json
from core.model_chart.living import livingBuider, livingStratum
from core.model_chart.vehicle import vehicleType, vehicleYear

from core.models import DomesticViolence, InfrastructureRoad, LivingPlace, Vehicle, ViolentDeaths
from core.model_chart.deaths_violent import numberDeathsType, numberDeathsYear
# Create your views here.


def home(request):
    return render(request, 'home.html')


def deathsViolent(request):
    lstChart = []

    query1 = {
        'labels': [],
        'data': []
    }

    query2 = {
        'labels': [],
        'data': []
    }

    queryset = ViolentDeaths.objects.values('type__name').annotate(
        count=Count('type_id')).order_by('-count')
    queryset2 = ViolentDeaths.objects.values('year').annotate(
        count=Count('year')).order_by('-count')

    for entry in queryset:
        query1['labels'].append(entry['type__name'])
        query1['data'].append(entry['count'])

    for entry in queryset2:
        query2['labels'].append(entry['year'])
        query2['data'].append(entry['count'])

    lstChart.append(numberDeathsType(query1))
    lstChart.append(numberDeathsYear(query2))

    return render(request, 'graphics.html', {'lstChart': json.dumps(lstChart)})


def domesticViolence(request):
    lstChart = []

    query2020 = {
        'labels': [],
        'data': []
    }

    query2021 = {
        'labels': [],
        'data': []
    }

    queryset2020 = DomesticViolence.objects.filter(year=2020).values('gender__name').annotate(
        count=Count('gender_id')).order_by('-count')

    queryset2021 = DomesticViolence.objects.filter(year=2021).values('gender__name').annotate(
        count=Count('gender_id')).order_by('-count')

    totalCont2020 = total(queryset2020)
    for entry in queryset2020:
        query2020['labels'].append(entry['gender__name'])
        query2020['data'].append(calc(entry['count'], totalCont2020))

    totalCont2021 = total(queryset2021)
    for entry in queryset2021:
        query2021['labels'].append(entry['gender__name'])
        query2021['data'].append(calc(entry['count'], totalCont2021))

    lstChart.append(violenceGender2020(query2020))
    lstChart.append(violenceGender2021(query2021))

    return render(request, 'graphics.html', {'lstChart': json.dumps(lstChart)})


def living(request):
    lstChart = []

    query1 = {
        'labels': [],
        'data': []
    }

    query2 = {
        'labels': [],
        'data': []
    }

    # Grafica circular para mostrar cuantas casas han construido por cada tipo de constructor
    queryset = LivingPlace.objects.values('builtby__name').annotate(
        count=Count('builtby_id')).order_by('-count')

    # Grafica de barra para mostrar las viviendas contruidas por estrato
    queryset2 = LivingPlace.objects.values('stratum').annotate(
        count=Count('stratum')).order_by('-count')

    totalCont = total(queryset)
    for entry in queryset:
        query1['labels'].append(entry['builtby__name'])
        query1['data'].append(calc(entry['count'], totalCont))

    for entry in queryset2:
        query2['labels'].append('Estrato '+str(entry['stratum']))
        query2['data'].append(entry['count'])

    lstChart.append(livingBuider(query1))
    lstChart.append(livingStratum(query2))

    return render(request, 'graphics.html', {'lstChart': json.dumps(lstChart)})


def infrastructureR(request):
    lstChart = []

    query = {
        'labels': [],
        'data': []
    }

    query1 = {
        'labels': [],
        'data': []
    }

    # Grafica circular por tipo de vehiculo
    queryset = InfrastructureRoad.objects.values('type__name').annotate(
        count=Count('type_id')).order_by('-count')

    # Grafica circular por estado
    queryset1 = InfrastructureRoad.objects.values('state__name').annotate(
        count=Count('state_id')).order_by('-count')

    totalCont = total(queryset)
    for entry in queryset:
        query['labels'].append(entry['type__name'])
        query['data'].append(calc(entry['count'], totalCont))

    totalCont1 = total(queryset1)
    for entry in queryset1:
        query1['labels'].append(entry['state__name'])
        query1['data'].append(calc(entry['count'], totalCont1))

    lstChart.append(infrastructureRoadType(query))
    lstChart.append(infrastructureRoadState(query1))

    return render(request, 'graphics.html', {'lstChart': json.dumps(lstChart)})


def vehicle(request):
    lstChart = []

    query = {
        'labels': [],
        'data': []
    }

    query1 = {
        'labels': [],
        'data': []
    }

    # Grafica de barra por tipo
    queryset = Vehicle.objects.values('type__name').annotate(
        count=Count('type_id')).order_by('-count')

    # Grafica de barra por año
    queryset1 = Vehicle.objects.values('year').annotate(
        count=Count('year')).order_by('-count')

    for entry in queryset:
        query['labels'].append(entry['type__name'])
        query['data'].append(entry['count'])

    for entry in queryset1:
        query1['labels'].append(entry['year'])
        query1['data'].append(entry['count'])

    lstChart.append(vehicleType(query))
    lstChart.append(vehicleYear(query1))

    return render(request, 'graphics.html', {'lstChart': json.dumps(lstChart)})


def total(data):
    total = 0
    for entry in data:
        total += entry['count']
    return total


def calc(cant, total):
    return round(cant*100/total)
