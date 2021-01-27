from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from user.views import signup, log_in, user_logout, home
from todo.views import list_todo

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('', list_todo, name='home'),
    path('signup/', signup, name='signup'),
    path('login/', log_in, name='login'),
    path('logout/', user_logout, name='logout'),
] 
urlpatterns += staticfiles_urlpatterns()
