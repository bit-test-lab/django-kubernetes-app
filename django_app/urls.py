from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
import socket

def health_check(request):
    return HttpResponse("OK")

def hostname_view(request):
    hostname = socket.gethostname()
    return HttpResponse(f"Hello from pod: {hostname}")

def main_page(request):
    hostname = socket.gethostname()
    return HttpResponse(f"""
    <html>
        <body>
            <h1>Django App on Kubernetes</h1>
            <p>Served from pod: <strong>{hostname}</strong></p>
            <p><a href="/metrics">Metrics</a></p>
        </body>
    </html>
    """)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('health/', health_check),
    path('hostname/', hostname_view),
    path('metrics/', include('django_prometheus.urls')),
    path('', main_page),
]
