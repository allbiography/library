from django.urls import path


from . import views


urlpatterns = [
    path('programming_book', views.index_programming_book, name="programming_book"),
    path('text_book', views.index_text_book, name="text_book"),
    path('user_history', views.history, name="user-history"),
    path('search', views.search, name="search"),
    path('description', views.description, name="description"),
    path('book_order', views.book_order, name="book-order"),
    path('profile', views.user_profile, name="user-profile"),
    path('change_password', views.user_change_pass, name="change-pass"),
]
