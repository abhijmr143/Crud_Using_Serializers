from django.shortcuts import render
from django.views.generic import View
import io
from rest_framework.parsers import JSONParser
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
class EmployeeCRUDCBV(View):

    def get(self, requests, *args, **kwargs):
        json_data = requests.body 
        stream = io.BytesIO(json_data)
        pdata = JSONParser().parse(stream)
        id = pdata.get('id', None)
        if id is not None:
            emp = Employee.objects.get(id=id)
            ser = EmployeeSerializer(emp)
            json_data = JSONRenderer().render(ser.data)
            return HttpResponse(json_data, content_type='application/json')

        qs = Employee.objects.all()
        ser = EmployeeSerializer(qs, many=True)
        json_data = JSONRenderer().render(ser.data)
        return HttpResponse(json_data, content_type='application/json')



    def post(self, requests, *args, **kwargs):
        json_data = requests.body
        stream = io.BytesIO(json_data)
        pdata = JSONParser().parse(stream)

        # Now convert thses python data into data base supported form
        ser = EmployeeSerializer(data=pdata)
        if ser.is_valid():
            ser.save()  # internally it will call create() function inside serializer.py
            msg={'msg':'Resource created successfully'}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data, content_type='applicaion/json')
        json_data = JSONRenderer().render(ser.errors)
        return HttpResponse(json_data, content_type='application/json', status=400)



    def put(self,requests, *args, **kwargs):
        json_data = requests.body
        stream = io.BytesIO(json_data)
        pdata = JSONParser().parse(stream)
        id = pdata.get('id')
        emp = Employee.objects.get(id=id)
        ser = EmployeeSerializer(emp, data=pdata, partial=True)
        if ser.is_valid():
            ser.save()
            msg = {'msg':'Resource updated successfully'}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(ser.errors)
        return HttpResponse(json_data, content_type='application/json', status=400)



    def delete(self,requests, *args, **kwargs):
        json_data = requests.body
        stream = io.BytesIO(json_data)
        pdata = JSONParser().parse(stream)
        id = pdata.get('id')
        emp = Employee.objects.get(id=id)
        emp.delete()
        msg = {'msg':'Resource deleted successfully'}
        json_data = JSONRenderer().render(msg)
        return HttpResponse(json_data, content_type='application/json')
        





            

