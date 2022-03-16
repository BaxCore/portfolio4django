from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'index.html'

class WorksPageView(TemplateView):
    template_name = 'works.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class ContactPageView(TemplateView):
    template_name = 'contact.html'

class WorkPageView(TemplateView):
    template_name = 'work.html'