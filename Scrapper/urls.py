from django.contrib import admin
from django.urls import path
from scrapperapp import views
urlpatterns = [
    path('admin/', admin.site.urls), 
    path('',views.scrape, name="scrape"),
    path('delete',views.clear,name="clear" ), 
]