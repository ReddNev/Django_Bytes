from django.shortcuts import render


posts = [
    {
        'author': 'Admin',
        'title': 'First post',
        'content': 'Content first post',
        'date_posted': '12 agust, 2022'
    },

    {
        'author': 'User',
        'title': 'Second post',
        'content': 'Details of the second post',
        'data_posted': '13 agust, 2022'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/abot.html', {'title': 'About the club Python bytes'})