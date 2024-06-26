from django.shortcuts import render

# Importing a django rest framework api view
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer


@api_view(["GET"])
def index(request):
    return Response({"Success": "The setup was successful"})


@api_view(["GET"])
def GetAllPosts(request):
    get_posts = Post.objects.all()
    serializer = PostSerializer(get_posts, many=True)
    return Response(serializer.data)


@api_view(["GET", "POST"])
def CreatePost(request):
    if request.method == "GET":
        get_posts = Post.objects.all()
        serializer = PostSerializer(get_posts, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)


@api_view(["DELETE"])
def DeletePost(request):
    post_id = request.data.get("post_id")
    try:
        post = Post.objects.get(id=post_id)
        post.delete()
        return Response({"success": "Post was deleted"}, status=200)
    except Post.DoesNotExist:
        return Response({"error": "Post does not exist"}, status=404)


@api_view(["GET"])
def GetPost(request):
    post_id = request.data.get("post_id")
    try:
        post = Post.objects.get(id=post_id)
        serialize = PostSerializer(post)
        return Response(serialize.data)
    except Post.DoesNotExist:
        return Response({"Error": "The post does not exist"}, status=404)


@api_view(["PUT"])
def UpdatePost(request):
    post_id = request.data.get("post_id")
    get_new_title = request.data.get("new_title")
    get_new_content = request.data.get("new_content")
    try:
        post = Post.objects.get(id=post_id)

        if get_new_title:
            post.title = get_new_title

        if get_new_content:
            post.content = get_new_content

        post.save()
        return Response({"success": "Post was updated"}, status=200)

    except Post.DoesNotExist:
        return Response({"Error": "The post does not exist"}, status=404)
