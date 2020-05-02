from django.shortcuts import render
from rest_framework import viewsets

from subjects.models import Subject, Topic
from subjects.serializers import SubjectSerializer, TopicSerializer


class SubjectViewSet(viewsets.ModelViewSet):
    query = Subject.objects.all()
    serializer_class = SubjectSerializer


class TopicViewSet(viewsets.ModelViewSet):
    query = Topic.objects.all()
    serializer_class = TopicSerializer
