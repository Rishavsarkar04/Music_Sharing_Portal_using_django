from django.urls import path
from django.contrib.auth import views as auth_views
from app import views
from app.forms import LoginForm
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('signup', views.signup,name='signup'),
    path('', views.home,name='home'),
    path('upload/', views.upload,name='upload'),
    path('delete/<int:id>/', views.delete,name='delete'),
    path('login/', auth_views.LoginView.as_view(template_name = 'app/login.html',authentication_form=LoginForm,next_page='home') , name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login') , name='logout'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
