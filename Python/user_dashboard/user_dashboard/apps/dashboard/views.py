from django.shortcuts import render, redirect, HttpResponse


def dashboard_admin(request):
    response = "placeholder for dashboard_admin"
    return render(request, 'dashboard/dashboard_admin.html')
def dashboard(request):
    response = "placeholder for dashboard"
    return render(request, 'dashboard/dashboard.html')