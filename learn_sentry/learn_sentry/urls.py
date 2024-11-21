from django.urls import path

def trigger_error(request):
    '+'+1

urlpatterns = [
    path('sentry-debug/', trigger_error),
    
]