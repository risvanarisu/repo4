from django. urls import path
from. import views
urlpatterns=[
    path('attendance/',views.registermanager,name="attendanc_e")

]