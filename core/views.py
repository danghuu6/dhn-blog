from django.shortcuts import render, redirect
from django.views import View
from .models import Posts, Categories, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


class HomeView(View):

    def get(self, request):
        search = request.GET.get('search')
        categories = Categories.objects.all()

        if search:
            posts = Posts.objects.filter(title__icontains=search, public=True)
        else:
            posts = Posts.objects.filter(public=True)

        # Paging
        paginator = Paginator(posts, 4)
        page = request.GET.get('page', 1)
        try:
            orders_paged = paginator.page(page)
        except PageNotAnInteger:
            orders_paged = paginator.page(1)
        except EmptyPage:
            orders_paged = paginator.page(paginator.num_pages)

        posts_new = Posts.objects.filter(public=True).order_by('-time')
        short_text = []
        for i in posts_new:
            short_text.append(i.content.split('\r\n')[0])
            y = i.time.strftime('%Y')
            m = i.time.strftime('%m')
            d = i.time.strftime('%d')
            i.time = d+'/'+m+'/'+y

        for j in orders_paged:
            y = j.time.strftime('%Y')
            m = j.time.strftime('%m')
            d = j.time.strftime('%d')
            j.time = d + '/' + m + '/' + y

        context = {
            'view': 'home',
            'search': search,
            'posts_new': posts_new[0],
            'short_text_new': short_text[0],
            'posts': orders_paged,
            'cate_list': categories,
        }

        return render(request, 'index.html', context)


class DetailView(View):

    def get(self, request, posts_id):
        p = Posts.objects.get(pk=posts_id)
        categories = Categories.objects.all()

        comment_list = Comment.objects.filter(posts_id=posts_id).order_by('-time')

        y = p.time.strftime('%Y')
        m = p.time.strftime('%m')
        d = p.time.strftime('%d')
        p.time = d+'/'+m+'/'+y

        for i in comment_list:
            y = i.time.strftime('%Y')
            m = i.time.strftime('%m')
            d = i.time.strftime('%d')
            i.time = d+'/'+m+'/'+y

        context = {
            'comment': comment_list,
            'post': p,
            'cate_list': categories,
        }

        return render(request, 'post.html', context)

    def post(self, request, posts_id):
        redirect_to = request.POST.get('next')
        p = Posts.objects.get(pk=posts_id)

        comment_text = request.POST.get('comment-text')
        comment_name = request.POST.get('comment-name')
        comment_email = request.POST.get('comment-email')

        comment = Comment(posts_id=p, comment_content=comment_text, comment_user=comment_name, comment_email=comment_email)

        if comment:
            comment.save()
            return redirect(redirect_to)


class CateView(View):
    def get(self, request, categories_id):
        p = Posts.objects.filter(categories=categories_id)
        cate = Categories.objects.get(pk=categories_id)
        cate_list = Categories.objects.all()

        # Paging
        paginator = Paginator(p, 6)
        page = request.GET.get('page', 1)
        try:
            orders_paged = paginator.page(page)
        except PageNotAnInteger:
            orders_paged = paginator.page(1)
        except EmptyPage:
            orders_paged = paginator.page(paginator.num_pages)

        context = {
            'posts': orders_paged,
            'cate_list': cate_list,
            'view': 'cate',
            'cate': cate,
        }
        return render(request, 'index.html', context)
