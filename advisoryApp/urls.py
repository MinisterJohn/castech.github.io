from django.urls import path
from .views import home, careerpath, studentperformance, career, performance, login_view, payment, signup

app_name = "core"
urlpatterns = [
    path('home/', home, name='home'),
    path('', signup, name='signup'),  
    path('payment/', payment, name='payment'),
    path('login/',login_view, name='login'),
    path('careerplanning/',career, name='career'),
    path('careerpathresult/', careerpath, name='careerpath'),
    path('performance/', performance, name='performance'),
    path('performanceresult/', studentperformance, name='studentperformance'),
]
