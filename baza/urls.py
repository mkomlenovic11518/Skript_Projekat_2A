from django.urls import path,re_path
from . import views


app_name = 'demo_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('proizvodjaci/', views.proizvodjaci, name='proizvodjaci'),
    path('proizvodjaci/<int:id>/', views.proizvodjac, name='proizvodjac'),
    path('proizvodjac/edit/<int:id>/', views.edit, name='edit'),
    path('proizvodjac/new/', views.new, name='new'),
    path('robe/', views.robe, name='robe'),
    path('robe/<int:id>/', views.roba, name='roba'),
    path('robe_p/<int:id>/', views.robe_p, name='robe_p'),
    path('roba/new_roba/', views.new_roba, name='new_roba'),
    path('roba/edit_roba/<int:id>/', views.edit_roba, name='edit_roba'),
    path('registracija/', views.registracija, name='registracija'),
    path('delete_proizvodjac/<int:id>/', views.delete_proizvodjac, name='delete_proizvodjac'),
    path('delete_roba/<int:id>/', views.delete_roba, name='delete_roba')

    #za integer int
    #path('int/<int:br>', views.broj, name='baza_broj'),
    #path('int/', views.broj, name='baza_broj_def'),
    #za string imamo str, text i slug
    #path('rec/<str:r>', views.rec, name='baza_rec'),
    #parametri
    #path('params/', views.params, name='baza_params'),
    #regex
    #re_path(r'^regex/(?:godina-(?P<godina>[0-9]{4}))/(?:mesec-(?P<mesec>[0-9]{2}))', views.regex, name='baza_regex'),
    #prikaz template
    #path('hello/', views.hello, name='baza_hello'),
]