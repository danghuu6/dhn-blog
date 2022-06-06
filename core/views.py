from django.shortcuts import render
from django.views import View
from .models import Posts
# Create your views here.


class HomeView(View):
    def get(self, request):
        posts = Posts.objects.filter(public=True).order_by('-time')

        short_text = []
        for i in posts:
            short_text.append(i.content.split('\r\n')[0])

        context = {
            'posts_new': posts[0],
            'posts': posts[1:],
            'short_text_new': short_text[0],
            'short_text': short_text[1:],
        }

        return render(request, 'index.html', context)


class DetailView(View):
    def get(self, request, posts_id):
        p = Posts.objects.get(pk=posts_id)

        context = {
            'post': p,
        }

        return render(request, 'post.html', context)


