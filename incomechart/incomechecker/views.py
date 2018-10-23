from rest_framework import viewsets
from .models import MonthlyPay
from .serializers import MonthlyPaySerializer
from django.shortcuts import render
from django.http import HttpResponse

# Include the `fusioncharts.py` file that contains functions to embed the charts.
from .fusioncharts import FusionCharts


class MonthlyPayViewSet(viewsets.ModelViewSet):
    serializer_class = MonthlyPaySerializer
    queryset = MonthlyPay.objects.all()


# The `chart` function is defined to generate Column 2D chart from database.
def chart(request):
    # Chart data is passed to the `dataSource` parameter, as dict, in the form of key-value pairs.
    dataSource = {}
    dataSource['chart'] = { 
        "caption": "Door Dash Favor delivery Monthly Average",
            "subCaption": "Deliverys",
            "xAxisName": "Month",
            "yAxisName": "Income (In USD)",
            "numberPrefix": "$",
            "theme": "zune",
           
        }

    # The data for the chart should be in an array where each element of the array is a JSON object
    # having the `label` and `value` as key value pair.

    dataSource['data'] = []
    # Iterate through the data in `Revenue` model and insert in to the `dataSource['data']` list.
    for key in MonthlyPay.objects.all():
      data = {}
      data['label'] = key.month
      data['value'] = key.month_earning
      
      dataSource['data'].append(data)

    # Create an object for the Column 2D chart using the FusionCharts class constructor                      
    column2D = FusionCharts("column2D", "ex1" , "600", "350", "chart-1", "json", dataSource)
    return render(request, 'incomechecker/index.html', {'output': column2D.render()}) 