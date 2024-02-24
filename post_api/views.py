from rest_framework.response import Response
from rest_framework import status, generics
from post_api.models import PostModel
from post_api.serializers import PostSerializer
import math
from datetime import datetime


class Posts(generics.GenericAPIView):
    serializer_class = PostSerializer
    queryset = PostModel.objects.all()

    def get(self, request):
        page_num = int(request.GET.get("page", 1))
        limit_num = int(request.GET.get("limit", 10))
        start_num = (page_num - 1) * limit_num
        end_num = limit_num * page_num
        search_param = request.GET.get("search")
        posts = PostModel.objects.all()
        total_posts = posts.count()
        if search_param:
            posts = posts.filter(title__icontains=search_param)
        serializer = self.serializer_class(posts[start_num:end_num], many=True)
        return Response({
            "status": "success",
            "total": total_posts,
            "page": page_num,
            "last_page": math.ceil(total_posts / limit_num),
            "posts": serializer.data
        })

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": {"post": serializer.data}}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class PostDetail(generics.GenericAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer

    def get_post(self, pk):
        try:
            return PostModel.objects.get(pk=pk)
        except:
            return None

    def get(self, request, pk):
        post = self.get_post(pk=pk)
        if post == None:
            return Response({"status": "fail", "message": f"Post with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(post)
        return Response({"status": "success", "data": {"post": serializer.data}})

    def patch(self, request, pk):
        post = self.get_post(pk)
        if post is None:
            return Response({"status": "fail", "message": f"Post with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        allowed_fields = {'title', 'content'}
        data = {k: v for k, v in request.data.items() if k in allowed_fields}

        data['updatedAt'] = datetime.now()

        serializer = self.serializer_class(
            post, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": {"post": serializer.data}})
        return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        post = self.get_post(pk)
        if post == None:
            return Response({"status": "fail", "message": f"Post with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

