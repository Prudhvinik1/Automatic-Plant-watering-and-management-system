from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render,redirect
from .models import Weather,Plant,Waterlevel,plantid
from django.utils import timezone
from django.core import serializers

from django.contrib.auth import authenticate,login,logout
from .forms import UserForm
from django.contrib.auth.decorators import login_required

def first_page(request):
    return render(request, "slide.html")

@csrf_exempt
def index(request):
    if request.method == 'POST':
        data1 = request.POST['data'].split(', ')
        if int(data1[2]) > 100:
                data1[2] = 'raining'
        else:
                data1[2] = 'no rain'
        for n  in range(1,len(data1) - 3):
            mois = Plant.objects.create(pid = plantid.objects.get(pid = n),moisture = data1[n+3])
            mois.save()
        temp = Weather.objects.create(temperature = data1[0],humidity = data1[1],pub_date = str(timezone.now()),check = data1[2])
        level = Waterlevel.objects.create(water_level = data1[3])
        temp.save()
        level.save()
        return HttpResponse(timezone.now())
    else:
        return HttpResponse(timezone.now())

def detail(request,pid1):
    if not request.user.is_authenticated():
        return redirect('weather:login')
    else:
        h = (list(filter(lambda x: x['fields'], json.loads(serializers.serialize('json',Plant.objects.filter(pid=pid1)))))[::-1])
        h1 = (list(filter(lambda x: x['fields'], json.loads(serializers.serialize('json',plantid.objects.filter(pid=pid1)))))[::-1])
        weather = Weather.objects.get(pk = Weather.objects.count())
        if len(h) == 0:
            return render(request, "Plants.html",{'moisture':"None",'latitude':h1[0]['fields']['latitude'],'longitude':h1[0]['fields']['longitude'],'name':h1[0]['fields']['plant_name'],'pid':pid1,'weather':weather})
        #return JsonResponse({"loc":html, "values":html1}, safe=False)
        return render(request, "Plants.html",{'moisture':h[0]['fields']['moisture'],'latitude':h1[0]['fields']['latitude'],'longitude':h1[0]['fields']['longitude'],'name':h1[0]['fields']['plant_name'],'name':h1[0]['fields']['plant_name'],'pid':pid1,'weather':weather})

def dashboard(request):
    if not request.user.is_authenticated():
        return redirect('weather:login')
    else:
        if request.method == 'GET':
            weather = Weather.objects.get(pk = Weather.objects.count())
            level = Waterlevel.objects.get(pk = Waterlevel.objects.count())
            json_temp = [Weather.objects.get(pk= Weather.objects.count() - k).temperature for k in range(0,11)][::-1]
            json_humid = [Weather.objects.get(pk= Weather.objects.count() - k).humidity for k in range(0,11)][::-1]
            return render(request, "graph.html", {'weather':weather,'plantid':plantid,'level':level,'json_temp':json_temp,'json_humid':json_humid})

@csrf_exempt
def addplant(request):
    if not request.user.is_authenticated():
        return redirect('weather:login')
    else:
        if request.method == "POST":
            plant_name = request.POST['a1']
            latitude = request.POST['a2']
            longitude = request.POST['a3']
            p = plantid.objects.count()
            plant = plantid.objects.create(pid = p+1,plant_name = plant_name,latitude = latitude,longitude = longitude)
            plant.save()
            return redirect('weather:dashboard')
            #print(plant_name)
        return render(request, 'add_plant.html')

def map(request):
    if not request.user.is_authenticated():
        return redirect('weather:login')
    else:
        if request.method == 'GET':
            weather = Weather.objects.get(pk = Weather.objects.count())
            p = plantid.objects.all()
            mois = []
            plant = []
            for i in p:
                m = list(filter(lambda x: x['fields'], json.loads(serializers.serialize('json',plantid.objects.filter(pid = i.pid)))))[::-1]
                for j in m:
                    plant.append(float(j['fields']['latitude']))
                    plant.append(float(j['fields']['longitude']))
                l = list(filter(lambda x: x['fields'], json.loads(serializers.serialize('json',Plant.objects.filter(pid = i.pid)))))[::-1]
                if len(l) != 0:
                	mois.append(l[0]['fields']['moisture'])
                else:
                    mois.append('None')
            level = Waterlevel.objects.get(pk = Waterlevel.objects.count())
            #print(weather.pub_date)
            #return JsonResponse({'plant':plant,'mois':mois},safe=False)
            return render(request, "map.html", {'weather':weather,'level':level,'mois':mois,'plant':plant})

@csrf_exempt
def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
    	user = form.save(commit=False)
    	username = form.cleaned_data['username']
    	password = form.cleaned_data['password']
    	user.set_password(password)
    	user.save()
    	user = authenticate(username = username, password = password)
    	if user is not None:
    		if user.is_active:
    			login(request,user)
    			return redirect('weather:dashboard')
    return render(request,'register.html')

@csrf_exempt
def UserLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('weather:dashboard')
            else:
                return render(request,'login.html',{'context': 'This user is already logged in.'})
        else:
            return render(request,'login.html',{'context': 'Either Username or Password are wrong.'})
    return render(request,'login.html')
    

def UserLogout(request):
	logout(request)
	return redirect('weather:login')
	

def numplants(request):
    plant = plantid.objects.all()
    arr = []
    for  p in plant:
        arr.append(p.pid)
    return JsonResponse({'pid':arr},safe=False)
