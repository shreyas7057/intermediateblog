from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from .models import BlogCategory,Blog,Comment,Contact
from django.core.paginator import Paginator


def all_blog(request):

    blogs = Blog.objects.all()

    # pagination
    paginator = Paginator(blogs,1)
    page = request.GET.get('pg')
    blogs = paginator.get_page(page)

    context = {
        'blogs':blogs,
        # 'count_comment':comments,
    }
    return render(request,'index.html',context)


def blog_detail(request,id):
    blog = Blog.objects.get(id=id)

    # recent posts it will show lastest 1 post
    blogs = Blog.objects.all().order_by('-created_at')[:1]

    # category list with product filter
    blogcategory = BlogCategory.objects.all()

    # show comments according to post
    comments = Comment.objects.filter(blog=blog)

    # posting comment
    comment_blog = get_object_or_404(Blog,id=id)
    
    if request.method == "POST":
        name = request.POST.get('name')
        message = request.POST.get('message')

        newcomment = Comment(
            blog = comment_blog,
            name=name,
            comment=message
        )
        newcomment.save()

        return redirect('blog_detail',id=id)
        

    context = {
        'blog':blog,
        'comments':comments,
        'blogcategory':blogcategory,
        'blogs':blogs,

    }
    return render(request,'post.html',context)


def post_by_filter(request,id):
    category = get_object_or_404(BlogCategory,id=id)
    posts = Blog.objects.filter(category=category)

    # pagination
    paginator = Paginator(posts,1)
    page = request.GET.get('pg')
    posts = paginator.get_page(page)

    context = {
        'blogs':posts,
    }

    return render(request,'filter.html',context)


def search(request):
    query = request.GET.get('q','')
    if query:
            queryset = (Q(title__icontains=query))
            results = Blog.objects.filter(queryset).distinct()
    else:
       results = []
    return render(request, 'search.html', {'results':results, 'query':query})


def contact(request):
    
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact_message = Contact(
            name=name,
            email = email,
            subject = subject,
            message = message
        )
        contact_message.save()


    return render(request,'contact.html')