from django.urls import path
from first_app import views

urlpatterns=[
    path('<int:num_redirct>',views.num_page_redirect),
    path('<str:topic>',views.sample_view,), #add this "<topic>" keyword in path to get a dynamic urls 
    path('<int:num1>/<int:num2>',views.add_num,)  #add this'<int:num1>/<int:num2>' keyword in path to get a dynamic urls 
]