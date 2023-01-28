from django.shortcuts import render
from django.http import JsonResponse
from .models import Post


def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        if title:
            Post.objects.create(title=title, description=description)
            message = f'Post {title} created successfully'
            return JsonResponse({"response": message})
    return render(request, 'blog/create_post.html')
