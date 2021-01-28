from django.urls import path

from . import views

app_name = 'grocery_list'
urlpatterns = [
    path('complete_todo/<int:item_id>', views.complete_todo, name='complete_todo'),
    path('delete_item/<int:item_id>', views.delete_item, name='delete_item'),
    path('add_more', views.add_more, name='add_more'),
    path('', views.index, name='index')
]
