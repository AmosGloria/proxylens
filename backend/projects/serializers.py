from rest_framework import serializers
from .models import Project, TargetURL

class TargetURLSerializer(serializers.ModelSerializer):
    project_name = serializers.CharField(source="project.name", read_only=True)
    
    class Meta:
        model = TargetURL
        fields = [
            "id",
            "project",
            "project_name",
            "url",
            "label",
            "is_active",
            "last_checked_at",
            "next_check_at",
            "created_at",
        ]
        read_only_fields = [
            "id",
            "project_name",
            "last_checked_at",
            "next_check_at",
            "created_at",
        ]
        
class ProjectSerializer(serializers.ModelSerializer):
    owner_username = serializers.CharField(source="owner.username", read_only=True)
    target_urls_count = serializers.SerializerMethodField()
    
    class Meta :
        model = Project
        fields = [
            "id",
            "owner",
            "owner_username",
            "name",
            "domain",
            "description",
            "is_active",
            "target_urls_count",
            "created_at",
            "updated_at",
        ]   
        read_only_fields = [
            "id",
            "owner",
            "owner_username",
            "target_urls_count",
            "created_at",
            "updated_at",
        ] 
    def get_target_urls_count(self, obj):
        return obj.target_urls.count() 