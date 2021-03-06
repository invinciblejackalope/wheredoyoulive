from django.urls import path

from . import views

app_name = "wheredoyoulive"  # idk if I need this
# first argument is relative URL; second is the view it corresponds to in
# views.py; third is the name of the view (necessary for the reverse() function,
# which is explained in views.py)
urlpatterns = [
    path('', views.index, name='index'),
    path('make_user', views.make, name='make'),
    path('users', views.show_users, name='show_users'),
    path('pois', views.show_pois, name='show_pois'),
    path('<str:username>', views.user_index, name='user_index'),
    path('<str:username>/upd_user', views.update, name='update'),
    path('<str:username>/del_user', views.delete, name='delete'),
    path('<str:username>/poi', views.poi, name='poi'),
    path('<str:username>/add_poi', views.add_poi, name='add_poi'),
    path('<str:username>/upd_poi', views.upd_poi, name='upd_poi'),
    path('<str:username>/rm_poi', views.rm_poi, name='rm_poi'),
]
