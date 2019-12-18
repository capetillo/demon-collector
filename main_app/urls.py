from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('demons/', views.demons_index, name='index'),
    path('demons/<int:demon_id>/', views.demons_detail, name='detail'),
    path('demons/create/', views.DemonCreate.as_view(), name='demons_create'),
    path('demons/<int:pk>/update/', views.DemonUpdate.as_view(), name='demons_update'),
    path('demons/<int:pk>/delete', views.DemonDelete.as_view(), name='demons_delete'),
    path('demons/<int:demon_id>/add_soul/', views.add_soul, name='add_soul'),
    path('demons/<int:demon_id>/add_photo/', views.add_photo, name='add_photo'),
    path('demons/<int:demon_id>/assoc_sin/<int:sin_id>/', views.assoc_sin, name='assoc_sin'),
    path('demons/<int:demon_id>/unassoc_sin/<int:sin_id>/', views.unassoc_sin, name='unassoc_sin'),
    path('sins/', views.SinList.as_view(), name='sins_index'),
    path('sins/<int:pk>/', views.SinDetail.as_view(), name='sins_detail'),
    path('sins/create/', views.SinCreate.as_view(), name='sins_create'),
    path('sins/<int:pk>/update/', views.SinUpdate.as_view(), name='sins_update'),
    path('sins/<int:pk>/delete/', views.SinDelete.as_view(), name='sins_delete'),
]