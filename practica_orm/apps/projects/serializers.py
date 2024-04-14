from rest_framework import serializers
from .models import Project, Task, Comment
from datetime import datetime

class projectSerializerModel(serializers.ModelSerializer):        
    def validate_name(self, value):
        if "andres" in value:
            raise serializers.ValidationError("Dont use the name andres in project")
        return value
    
    class Meta:
        model = Project
        fields = "__all__"

            
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
        
class CommentSerializer(serializers.ModelSerializer):
    def validate_content(self, value):
        invalidWords = ["sexo", "anal", "orgia", "puta"]
        if any(word in value for word in invalidWords):
            raise serializers.ValidationError("Don't use obscene words")
        return value

    class Meta:
        model = Comment
        fields = "__all__"

class ProjectSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=60)
    init_date = serializers.DateTimeField(required=False)
    end_date = serializers.DateTimeField()
    
    def validate_name(self, value):
        if "andres" in value:
            raise serializers.ValidationError("Dont use the name andres in project")
        return value
   
    def create(self, validated_data):
        print (validated_data)  
        Project(**validated_data).save()
        
        return self.data