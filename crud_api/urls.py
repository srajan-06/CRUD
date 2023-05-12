from . import views
from django.urls import path

app_name = 'crud_api'

urlpatterns = [
    path('crud_ajax_create/',views.CreateCrudUser.as_view(),name="crud_ajax_create"),
    path('crud_ajax_update/',views.UpdateCrudUser.as_view(),name="crud_ajax_update"),
    path('crud_ajax_delete/',views.DeleteCrudUser.as_view(),name="crud_ajax_delete"),
]