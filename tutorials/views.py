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
from rest_framework import viewsets

class TutorialsViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Tutorial.objects.all()
    serializer_class = TutorialSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        print("list")
        page = self.paginate_queryset(queryset)
        if page is not None:
            print("lis3333")
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


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


class GetViewSet(viewsets.ModelViewSet):
    '''
    必须有序列化的动作,否则会报错
    '''
    queryset = Tutorial.objects.all()
    serializer_class = TutorialSerializer


    def list(self, request, *args, **kwargs):
        info = request.GET["info"]
        return Response(info)