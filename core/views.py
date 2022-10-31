from core.model_chart.domestic_violence import violenceGender2020, violenceGender2021
from django.shortcuts import render
from django.db.models import Count
import json

from core.models import DomesticViolence, ViolentDeaths
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

    print("2020")
    for entry in queryset2020:
        print(entry)
        query2020['labels'].append(entry['gender__name'])
        query2020['data'].append(entry['count'])

    print("2021")
    for entry in queryset2021:
        print(entry)
        query2021['labels'].append(entry['gender__name'])
        query2021['data'].append(entry['count'])

    lstChart.append(violenceGender2020(query2020))
    lstChart.append(violenceGender2021(query2021))

    return render(request, 'graphics.html', {'lstChart': json.dumps(lstChart)})
