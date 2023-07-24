from django.urls import path

from views import scheduling_detail, scheduling_list

urlpatterns=[
    path('v1/schedulings/', scheduling_list),
    path('v1/scheduling/<int:id>/',scheduling_detail),
]