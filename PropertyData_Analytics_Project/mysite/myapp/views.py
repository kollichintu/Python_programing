from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import json
from myapp.models import Data

# Create your views here.

def hello(request):
   if (request.method == 'POST'):
       previous_records = Data.objects.all()
       previous_records.delete()
       print('This is POST method')
       file = request.FILES['file']
       df = pd.read_csv(file)
       json_records = df.reset_index().to_json(orient='records')
       data = []
       data = json.loads(json_records)
       for d in data:
           name = d['property_name']
           price = d['property_price']
           rent = d['property_rent']
           emi = d['emi']
           tax = d['tax']
           exp = d['other_exp']
           expenses = emi+tax+exp
           income = rent-expenses
           dt = Data(name=name, price=price, rent=rent,
                     emi=emi, tax=tax, exp=exp, monthly_expenses=expenses,actual_income=income )
           dt.save()
       data_objects = Data.objects.all()
       context = {'data_objects':data_objects}
       return render(request,'myapp/index.html',context)
   else:
       print('This is get method')
   return render(request,'myapp/index.html')

    
    
