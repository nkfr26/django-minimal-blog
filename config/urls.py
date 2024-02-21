from django.contrib import admin
from django.urls import path

# views.pyで書いた関数をインポートする
from blog.views import index, detail

urlpatterns = [
    path('admin/', admin.site.urls)
] + [
    path("", index),
    path("<slug:slug>/", detail, name="detail")
]
