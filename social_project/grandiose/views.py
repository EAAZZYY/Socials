from django.shortcuts import render,redirect, get_object_or_404
from .forms import PostForm
from .models import Posts, Comment
from user_accounts.models import Profile
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def home(request):
    logged_user = request.user
    if request.method == "POST":
        comment = request.POST.get("comment")
        comment_by = logged_user
        post_id = request.POST.get("post_id")
        post = get_object_or_404(Posts, id = post_id)
        new_comment = Comment(post = post, comment=comment,comment_by=comment_by)
        new_comment.save()
        all_post = Posts.objects.all()
        return redirect("/")
    else:    
        all_post = Posts.objects.all()

    return render(request, "grandiose/home.html",{"all_post":all_post,"logged_user":logged_user})

@login_required
def post(request):
    if request.method == "POST":
        post = PostForm(data = request.POST, files = request.FILES)
        post.instance.posted_by = request.user
        if post.is_valid():
            post.save()
            return redirect("grandiose:home")
        
    else:
        post = PostForm()
        
    return render(request, "grandiose/post.html",{"post":post})

def post_liked(request):
    post_id = request.POST.get('post_id')
    post = get_object_or_404(Posts, id = post_id)
    if post.liked_by.filter(id=request.user.id).exists():
        post.liked_by.remove(request.user)
    
    else:
        post.liked_by.add(request.user)
    return redirect("/")