from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from tutorials.models import Tutorial
from tutorials.serializers import TutorialSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404


class TutorialsList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        snippets = Tutorial.objects.all()
        serializer = TutorialSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):

        serializer = TutorialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TutorialsDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Tutorial.objects.get(pk=pk)
        except Tutorial.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = TutorialSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        if request.data["title"] == "test":
            request.data["title"] = "hahaa"
        serializer = TutorialSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
def get_test(request,format=None):
    if request.method == 'GET':
        date = {'status':'Success'}
        return Response(date,status=200)
    else:
        data = {'status':'error','method':request.method}
        return Response(data,status=404)


class Get_info(APIView):
    """
    自定义的API方法,没有数据库
    """
    def get(self, request, format=None):
        info = request.GET["info"]
        return Response(info)
    def post(self, request, format=None):
        try:
            print(request.data["info"])
            info = request.data["info"]
        except:
            return Response("no avgs")
        return Response(info)