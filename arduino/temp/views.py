from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,  login as auth_login

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from .models import SensorData
import json


from .models import *

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, email=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('temp')  # Redirect to the home page after successful login
        else:
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        name = request.POST.get('name', '')

        if UserData.objects.filter(email=email).exists():
            return render(request, 'register.html', {'error_message': 'Email is already in use'})

        user_data = UserData(email=email, password=password, name=name)
        user_data.save()

        # You can perform additional actions here if needed

        return redirect('get_data')  # Redirect to the home page after successful registration
    else:
        return render(request, 'register.html')
    
def temp(request):
    if request.method=="GET":
        return render(request, 'temp.html')

def ultra(request):
    return render(request, 'ultra.html')

@csrf_protect
def get_data(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            temperature = data.get('temperature')
            humidity = data.get('humidity')
            
            if temperature is None or humidity is None:
                return JsonResponse({'error': 'Missing required fields'}, status=400)
            
            sensor_instance = SensorData(temperature=temperature, humidity=humidity)
            sensor_instance.save()
            
            response = JsonResponse({'message': 'Data saved successfully'}, status=201)
            response["Cross-Origin-Opener-Policy"] = "same-origin"
            return response
        
        except (ValueError, TypeError):
            return JsonResponse({'error': 'Invalid request body'}, status=400)
    
    sensor_data = SensorData.objects.all()
    
    if not sensor_data:
        response = JsonResponse({'message': 'No sensor data available'})
    else:
        data = [{'id': item.id, 'temperature': item.temperature, 'humidity': item.humidity} for item in sensor_data]
        response = JsonResponse(data, safe=False)
    
    response["Cross-Origin-Opener-Policy"] = "same-origin"
    return response