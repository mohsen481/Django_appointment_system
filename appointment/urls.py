from django.urls import path
from . import views
urlpatterns=[path("",views.myview,name="appointment"),
             path("my_appointments/<int:user_id>/",views.show_user_appointments,name="my_appointments"),
             path("all",views.all_appointments,name="all_times")
             ]