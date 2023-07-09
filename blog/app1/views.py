from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .forms import PostForm

from .models import Post


# Create your views here.


def post_list(request):
    p=Post.objects.all()
    return render(request,'app1/post_list.html',{'p':p})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'app1/post_detail.html', {'post': post})


def post_new(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'app1/post_edit.html', {'form': form})


def test(request):
    #p=Post.objects.all()
    return render(request,'app1/test.html')


