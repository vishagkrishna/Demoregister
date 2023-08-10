from . import views
from django.urls import path

urlpatterns = [
  path('',views.index,name='index'),
  path('adds',views.adds,name='adds'),
  path('login',views.loginn,name="login"),
  path('formss/',views.formss,name='formss'),
  path('logout',views.loginn,name='logout'),
  path('get-branches/', views.get_branches,name='get_branches'),
  path('submit-form/', views.submit_form, name='submit_form'),
  path('final/',views.final,name='final'),
  path('home',views.home,name='home'),
  path('page',views.page,name='page')

]