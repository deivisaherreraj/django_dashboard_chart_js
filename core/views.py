from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import Sum
from django.db.models import Count

from core.models import ViolentDeaths
from core.model_chart.deaths_violent import numberDeathsType, numberDeathsYear
# Create your views here.


def home(request):
    return render(request, 'home.html')


def population_chart(request):
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

    return JsonResponse({'lstChart': lstChart, })


def pie_chart(request):
    labels = []
    data = []

    queryset = ViolentDeaths.objects.order_by('-year')[:5]
    for death in queryset:
        labels.append(death.type)
        data.append(death.year)

    return render(request, 'pie_chart.html', {
        'labels': labels,
        'data': data,
    })
