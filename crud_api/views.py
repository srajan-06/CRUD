from django.shortcuts import render
from django.views.generic import ListView, View
from django.http import JsonResponse
from .models import CrudUser

#Creating a logical view for user
class CrudView(ListView):
    model = CrudUser
    template_name = 'crud_api/crud.html'
    context_object_name = 'users'

#Creating a view to user to create a user
class CreateCrudUser(View):
    def get(self, request):
        name1 = request.GET.get('name', None)
        email1 = request.GET.get('email', None)
        phone1 = request.GET.get('phone', None)
        age1 = request.GET.get('age', None)
        location1 = request.GET.get('location', None)
    
        obj = CrudUser.objects.create( 
            name = name1,
            email = email1,
            phone = phone1,
            age = age1,
            location = location1

        )

        user = {'id':obj.id,'name':obj.name, 
                'email':obj.email,'phone':obj.phone,
                'age':obj.age,'location':obj.location}
    
        data = {
            'user' : user
        }

        return JsonResponse(data)

#Creating a view for user to update user
class UpdateCrudUser(View):
    def get(self, request):
        id1 = request.GET.get('id', None)
        name1 = request.GET.get('name', None)
        email1 = request.GET.get('email', None)
        phone1 = request.GET.get('phone', None)
        age1 = request.GET.get('age', None)
        location1 = request.GET.get('location', None)
    
        obj = CrudUser.objects.get(id=id1) 
        obj.name = name1
        obj.email = email1
        obj.phone = phone1
        obj.age = age1
        obj.location = location1

        user = {'id':obj.id,'name':obj.name, 
                'email':obj.email,'phone':obj.phone,
                'age':obj.age,'location':obj.location}
    
        data = {
            'user' : user
        }

        return JsonResponse(data)
    
class DeleteCrudUser(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        CrudUser.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)