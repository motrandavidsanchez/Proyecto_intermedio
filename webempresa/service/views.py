from django.shortcuts import render

from service.models import Service


def service(request):
    services = Service.objects.all()
    return render(request, 'service/service.html', {'services': services})
