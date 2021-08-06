from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from tutorials.models import Tutorial
from tutorials.serializers import TutorialSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

@csrf_exempt
@api_view(['GET', 'POST'])
def tutorials_list(request,format=None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':

        snippets = Tutorial.objects.all()
        print(snippets)
        serializer = TutorialSerializer(snippets,many=True) #没有many=True页面显示空
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TutorialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def tutorials_detail(request, pk,format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Tutorial.objects.get(pk=pk)
    except Tutorial.DoesNotExist:
        return Response()

    if request.method == 'GET':
        print(snippet.title)
        snippet.title = "haa1121"   #修改展示的数据
        serializer = TutorialSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TutorialSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response()

@api_view(['GET','POST'])
def get_test(request,format=None):
    if request.method == 'GET':
        date = {'status':'Success'}
        return Response(date,status=200)
    else:
        data = {'status':'error','method':request.method}
        return Response(data,status=404)
