from django.shortcuts import render
from django.http import HttpResponse
import requests
Base_Id="app6qb9IitNh4rttX"  
Table_Name="property "
Api_Key="API_KEY"
End_Point="https://api.airtable.com/v0/"+Base_Id+"/"+Table_Name
Headers={"Authorization":"Bearer "+Api_Key,"Content-Type":"application/json"}

def get_data():
  a=requests.get(End_Point,headers=Headers)
  b=a.json()
  b=b["records"]
  return b

def delete_data(record_id):
    End_Point="https://api.airtable.com/v0/"+Base_Id+"/"+Table_Name+'/'+record_id
    return requests.delete(End_Point,headers=Headers)

def  add_data(name,desc,size):
  Data={"fields": {"Name": name,"Notes": desc,"Label": size}}
  requests.post(End_Point,json=Data,headers=Headers)

def home(request):
    # return render(request,'index.html')
    try:
        i = request.POST.get("submit")
        data=get_data()
        if i!='get-data':
            print(i)
            delete_data(i)
        return render(request,'index.html',{'data':data,})
    except:
        return render(request,'index.html',{'data':data,})

def addrecord(request):
    try:
        name = request.POST.get('name')
        area = request.POST.get('size')
        desc = request.POST.get('desc')

        if (name!="" and area !="" and desc != ""):
            add_data(name,desc,int(area))
        return render(request,'addrecord.html')
    except:
        return render(request,'addrecord.html')
