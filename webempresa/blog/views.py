from django.shortcuts import render, get_object_or_404

from blog.models import Post, Category


def blog(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog.html', {'posts': posts})


def category(request, category_id):
    categorie = get_object_or_404(Category, id=category_id)
    return render(request, 'blog/categorie.html', {'categorie': categorie})
