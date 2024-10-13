from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from maths.views import add, sub, mul, div, math

urlpatterns = [
   path('admin/', admin.site.urls),
   path('maths/', math),
   path('maths/add/<int:a>/<int:b>', add),
   path('maths/sub/<int:a>/<int:b>', sub),
   path('maths/mul/<int:a>/<int:b>', mul),
   path('maths/div/<int:a>/<int:b>', div),
]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('greetings/', include('greetings.urls')),
]