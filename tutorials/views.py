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
from rest_framework import mixins,generics


class TutorialsList(generics.ListCreateAPIView):
    queryset = Tutorial.objects.all()
    serializer_class = TutorialSerializer

    '''
    自定义get和post方法,可以去掉
    '''
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TutorialsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tutorial.objects.all()
    serializer_class = TutorialSerializer
    '''
    自定义get和post方法,可以去掉
    '''
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


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
            request.POST._mutable = True   #修改requset.POST 的值需要
            print(request.data["info"])
            info = request.data["info"]
        except:
            return Response("no avgs")
        return Response(info)