from django.urls import path
from .views import HomePageView, WorksPageView, ContactPageView, AboutPageView, WorkPageView

urlpatterns = [
     path('', HomePageView.as_view(), name='index'),
     path('works', WorksPageView.as_view(), name='works'),
     path('contact', ContactPageView.as_view(), name='contact'),
     path('about', AboutPageView.as_view(), name='about'),
     path('work', WorkPageView.as_view(), name='work'),
]