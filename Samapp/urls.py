from . import views
from django.urls import path,include

urlpatterns = [

    path('home_page',views.home_page,name='home_page'),
    path('thrissur_page',views.thrissur_page,name='thrissur_page'),
    path('palakkad_page',views.palakkad_page,name='palakkad_page'),
    path('kannur_page',views.kannur_page,name='kannur_page'),
    path('kozhikode_page',views.kozhikode_page,name='kozhikode_page'),
    path('wayanad_page',views.wayanad_page,name='wayanad_page'),

]
