from django.shortcuts import render
from django.http import HttpResponse


# def home(request):
#     return render(request, 'home.html')
    
def about(request):
    return render(request,"about.html")

def services(request):
    return render(request,"services.html")

def pricing(request):
    return render(request,"pricing.html")

def blog(request):
    return render(request,"blog.html")

def contact(request):
    return render(request,"contact.html")


from django.shortcuts import render

def home(request):
    context = {
        'title': 'Aura Harks Technology | IT Services & Solutions',
        'meta_description': 'Aura Harks Technology delivers cutting-edge IT services and solutions. From product development and web development to data analysis and AI & ML design, we empower your business with expert solutions.',
        'canonical_url': 'https://www.example.com/',
        'og_title': 'Aura Harks Technology | IT Services & Solutions',
        'og_description': 'Aura Harks Technology provides advanced IT services and solutions including product development, web development, data analysis, and AI & ML design.',
        'og_url': 'https://www.example.com/',
        'twitter_title': 'Aura Harks Technology | IT Services & Solutions',
        'twitter_description': 'Aura Harks Technology provides advanced IT services and solutions including product development, web development, data analysis, and AI & ML design.',
        'linkedin_title': 'Aura Harks Technology | IT Services & Solutions',
        'linkedin_description': 'Aura Harks Technology provides advanced IT services and solutions including product development, web development, data analysis, and AI & ML design.',
    }
    return render(request, 'home.html', context)







