from django.conf.urls import url
from django.contrib import admin
from quiz.views import list_quizzes, show_quiz, check_answer, index
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from user.views import signup, log_in, user_logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('', index),
    path('list/', list_quizzes, name='list_quiz'),
    path('quiz/<int:quiz_id>/', show_quiz, name='show_quiz'),
    path('attempt/<int:question_id>/', check_answer, name='check_answer'),
    path('signup/', signup, name='signup'),
    path('login/', log_in, name='login'),
    path('logout/', user_logout, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
