from django.shortcuts import render

def home(request):
    # context = {
    #     'posts': Post.objects.all()
    # }
    return render(request, 'blog/home.html')


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})