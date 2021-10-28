from django.shortcuts import render

def AboutPage(request):
    template_name = 'about.html'
    context = {}
    return render(request, template_name, context)