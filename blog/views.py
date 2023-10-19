from django.http import HttpResponse
from django.shortcuts import render

blog_post = [
    {
        'title': "প্রথম আলো | বাংলা নিউজ পেপার",
        'content': "ফিলিস্তিনি গোষ্ঠী হামাস বিশ্বজুড়ে একটি আর্থিক নেটওয়ার্ক ব্যবহার করে থাকে",
        'author': "বিষয়টি অবিশ্বাস্য মনে হচ্ছে পিপি আবদুর রশিদের",
        "post": "স্বজনেরা কেউ না আসায় নিরাশ চট্টগ্রাম নগরের বায়েজিদ বোস্তামী থানার",
    },
    {
        'title': "প্রথম আলো | বাংলা নিউজ পেপার",
        'content': "ফিলিস্তিনি গোষ্ঠী হামাস বিশ্বজুড়ে একটি আর্থিক নেটওয়ার্ক ব্যবহার করে থাকে",
        'author': "বিষয়টি অবিশ্বাস্য মনে হচ্ছে পিপি আবদুর রশিদের",
        "post": "স্বজনেরা কেউ না আসায় নিরাশ চট্টগ্রাম নগরের বায়েজিদ বোস্তামী থানার",
    }

]


def home(request):
    return render(request, 'home.html', {'blog_post': blog_post})


def about(request):
    return render(request, 'blog/about.html', {'title': "About Page"})
