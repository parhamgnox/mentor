from rest_framework import serializers
from ...models import Course


# class CourseApiSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=200)
#     price = serializers.IntegerField()


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ["id", "title", "price", "content", "category", "teacher" , "image"]




class CourseDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ["title", "price", "content", "teacher", "category", "status" , "image"]


    image = serializers.CharField()