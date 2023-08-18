from django.urls import path

from .views import schedule_list
from .views import SchedulingList, SchedulingDetail

urlpatterns_schedulings=[
    path('v1/scheduling/', SchedulingList.as_view()),
    path('v1/scheduling/<int:id>/',SchedulingDetail.as_view()),
]

urlpatterns_schedules=[
    path('v1/schedule/',schedule_list)
]