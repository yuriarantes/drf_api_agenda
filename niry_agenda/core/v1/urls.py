from django.urls import path

from .views import scheduling_detail, scheduling_list

urlpatterns_schedulings=[
    path('v1/scheduling/', scheduling_list),
    path('v1/scheduling/<int:id>/',scheduling_detail),
]