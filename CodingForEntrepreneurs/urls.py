"""CodingForEntrepreneurs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from patients.views import contactview,aboutview,RegisterView
from questions.views import SignUp
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from rest_framework import routers
from CodingForEntrepreneurs.api.views import QuestionViewSet, PatientViewSet, ExamViewSet, ResultViewSet, Detailed_ScoreViewSet,PatientloginSet
from . import views

router1 = routers.DefaultRouter()
router1.register(r'questions', QuestionViewSet)

router2 = routers.DefaultRouter()
router2.register(r'patients', PatientViewSet)

router3 = routers.DefaultRouter()
router3.register(r'exams', ExamViewSet)

router4 = routers.DefaultRouter()
router4.register(r'results', ResultViewSet)

router5 = routers.DefaultRouter()
router5.register(r'detailed_score', Detailed_ScoreViewSet)

router6 = routers.DefaultRouter()
router6.register(r'p_login', PatientloginSet, base_name='MyModel')



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
# urlpatterns = [
    
#     #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]

urlpatterns = [
    path(r'admin/', admin.site.urls),
    # path(r'patients/', include('patients.urls', namespace='patients')),
    path(r'question/', include('questions.urls', namespace='question')),
    # path(r'contact/', contactview.as_view(), name='contact'),
    # path(r'about/', aboutview.as_view(), name='about'),
    # # path(r'accounts/login/', auth_views.LoginView.as_view(), name = 'login'),
    # path(r'logout/', auth_views.LogoutView.as_view(), name = 'logout'),
    # path(r'api/p_login', PatientloginSet.as_view(), name = 'p_login'),
    path(r'api/', include(router1.urls)),
    path(r'api/', include(router2.urls)),
    path(r'api/', include(router3.urls)),
    path(r'api/', include(router4.urls)),
    path(r'api/', include(router5.urls)),
    path(r'api/', include(router6.urls)),
    # path(r'api/create/', PatientCreateSet.as_view()),
    path(r'', views.angular_view, name='home'),
    path(r'reg/', views.register_view),
    # path(r'', TemplateView.as_view(template_name='home.html'), name='home'),
    path(r'users/', include('questions.urls')),
    path(r'users/', include('django.contrib.auth.urls')),
    path(r'signup/',SignUp.as_view(), name='signup'),
    
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

