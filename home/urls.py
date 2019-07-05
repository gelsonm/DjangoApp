from django.urls import path
from .views import .

urlpatterns={
    path('',views.home_view),
    path('delete-student/<id>',views.deletestudent),
    path('edit-student/<id>',views.editstudent),
    path('create-student/',views.createstudent),
    path('about/',views.about),
    path('contact/',views.contact),
}