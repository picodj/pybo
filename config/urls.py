from django.contrib import admin
# ---------------------------------- [edit] ---------------------------------- #
from django.urls import path, include
from pybo import views
# ---------------------------------------------------------------------------- #

urlpatterns = [
    path('admin/', admin.site.urls),
    # ---------------------------------- [edit] ---------------------------------- #
    path('pybo/', include('pybo.urls')),
    path('common/', include('common.urls')),
    path('', views.index, name='index'),
    # ---------------------------------------------------------------------------- #
]
