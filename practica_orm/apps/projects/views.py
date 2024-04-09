from django.shortcuts import render
#other modules
from rest_framework.views import APIView
from rest_framework.response import Response
#self modules
from .models import *
#utils
from datetime import datetime

# Create your views here.
class ProjectAPIView(APIView):
    
    def get(self, request):
        projects = Project.objects.all()
        
        data = [
            {
                "id" : project.id,
                "name" : project.name                
            }
            for project in projects
        ]
        return Response(data)
        
    def post(self, request):
        print (request.data)
        
        project = Project()
        project.name = request.data.get('name', "")
        project.init_date = datetime.now()
        
        end_date = request.data.get('end_date', "")
        project.end_date = datetime.strptime(end_date, '%d-%m-%YT%H:%M:%S')
        project.save()
        return Response({})
    
    def delete(self, request):
        id = request.data.get("id")
        project = Project.objects.get(id=id)
        project.delete()
        
        return Response({})
    
    def patch(self, request):
        id = request.data.get("id")
        project = Project.objects.get(id=id)
        
        project.name = request.data.get("name", project.name)
        project.save()
        
        return Response({
            "id" : project.id,
            "name": project.name
        })
        
class TaskAPIView(APIView):    
    def get(self, request, *args, **kwargs):
        # Accedemos al número capturado en la URL para obtener el ID del proyecto
        project_id = kwargs.get('numero')
        
        try:
            # Buscamos el proyecto con el ID proporcionado en la URL
            project = Project.objects.get(id=project_id)
            
            # Recuperamos todas las tareas que corresponden al proyecto
            tasks = Task.objects.filter(project=project)
            
            # Serializamos las tareas y las preparamos para la respuesta
            data = [
                {
                    "id": task.id,
                    "description" : task.description,
                    "project" : task.project.name,  #Nombre del proyecto al que se relaciona la tarea
                    "priority": task.priority,
                    "end_date" : task.end_date,
                }
                for task in tasks
            ]
            
            return Response(data)
        
        except Project.DoesNotExist:
            return Response({"error": "El proyecto no existe"}, status=404)
     
    def post(self, request, *args, **kwargs):
        print(request.data)
        
        # Accedemos al número capturado en la URL para obtener el ID del proyecto
        project_id = kwargs.get('numero')
        
        try:
            # Buscamos el proyecto con el ID proporcionado en la URL
            project = Project.objects.get(id=project_id)
            
            task = Task()
            task.project = project
            task.description = request.data.get('description', "")
            task.priority = request.data.get('priority', "")
            
            end_date = request.data.get('end_date', "")
            task.end_date = datetime.strptime(end_date, '%d-%m-%YT%H:%M:%S')
            task.save()
            
            return Response({})
        
        except Project.DoesNotExist:
            return Response({"error": "El proyecto no existe"}, status=404)
    
    def delete(self, request, *args, **kwargs):
        # Accedemos al número capturado en la URL para obtener el ID del proyecto
        project_id = kwargs.get('numero')
        
        try:
            # Buscamos el proyecto con el ID proporcionado en la URL
            project = Project.objects.get(id=project_id)
            
            task_id = request.data.get("id")
            task = Task.objects.get(id=task_id, project=project)
            
            task.delete()
            
            return Response({})
        
        except (Project.DoesNotExist, Task.DoesNotExist):
            return Response({"error": "El proyecto o la tarea no existe"}, status=404)
    
    def patch(self, request, *args, **kwargs):
        # Accedemos al número capturado en la URL para obtener el ID del proyecto
        project_id = kwargs.get('numero')
        
        try:
            # Buscamos el proyecto con el ID proporcionado en la URL
            project = Project.objects.get(id=project_id)
            
            task_id = request.data.get("id")
            task = Task.objects.get(id=task_id, project=project)
            
            task.description = request.data.get("description", task.description)
            task.priority = request.data.get("priority", task.priority)
            
            end_date = request.data.get('end_date', "")
            if end_date:
                task.end_date = datetime.strptime(end_date, '%d-%m-%YT%H:%M:%S')
                
            task.save()
            
            return Response({
                "id": task.id,
                "description": task.description,
                "priority": task.priority,
                "end_date": task.end_date
            })
        
        except (Project.DoesNotExist, Task.DoesNotExist):
            return Response({"error": "El proyecto o la tarea no existe"}, status=404)
        
        