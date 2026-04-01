from django.urls import path
from . import views

#task6:
#urlpatterns = [
#    path('', views.index), 
#    path('index2/<int:val1>/', views.index2),
#    path('<int:bookId>', views.viewbook),#task7
#]

#task4-lab4
#urlpatterns = [
#path('', views.index, name= "books.index"),
#path('list_books/', views.list_books, name= "books.list_books"),
#path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
#path('aboutus/', views.aboutus, name="books.aboutus"),
#]

#lab5
urlpatterns = [
    path('html5/links', views.links_view),
    path('html5/text/formatting', views.text_formatting_view),
    path('html5/listing', views.listing_view),
    path('html5/tables', views.tables_view),
#lab6
    path('search', views.search_view),
]
