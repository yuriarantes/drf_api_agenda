from django.urls import path

from .views import scheduling_detail, scheduling_list, schedule_list

urlpatterns_schedulings=[
    path('v1/scheduling/', scheduling_list),
    path('v1/scheduling/<int:id>/',scheduling_detail),
]

urlpatterns_schedules=[
    path('v1/schedule/',schedule_list)
]