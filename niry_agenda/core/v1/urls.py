from django.urls import path

from .views import ScheduleList
from .views import SchedulingList, SchedulingDetail

urlpatterns_schedulings=[
    path('v1/scheduling/', SchedulingList.as_view()),
    path('v1/scheduling/<str:id>/',SchedulingDetail.as_view()),
]

urlpatterns_schedules=[
    path('v1/schedule/',ScheduleList.as_view())
]