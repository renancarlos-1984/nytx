from django.shortcuts import render

from .models import RevisionHistory

def AboutPage(request):
    template_name = 'pages/about.html'
    context = {}
    context['revision_history'] = RevisionHistory.about_objects.all()
    return render(request, template_name, context)