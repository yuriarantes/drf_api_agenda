from django.urls import path

from .views import scheduling_detail, scheduling_list, schedule_list
from .views import SchedulingList

urlpatterns_schedulings=[
    path('v1/scheduling/', SchedulingList.as_view()),
    path('v1/scheduling/<int:id>/',scheduling_detail),
]

urlpatterns_schedules=[
    path('v1/schedule/',schedule_list)
]