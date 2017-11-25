from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/opportunities/$', views.OpportunityList.as_view()),
    url(r'^api/surveys/$', views.SurveyList.as_view()),
    url(r'^api/submit/$', views.SubmitVolunteerInterestForm.as_view())
]