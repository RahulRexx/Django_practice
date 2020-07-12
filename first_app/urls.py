from django.conf.urls import url
from first_app import views

app_name = 'first_app'

# urlpatterns = [
#     url('',views.index,name="index")
# ]

urlpatterns = [
    url('first/',views.first,name="first"),
    url('formpage/',views.form_name_view,name='form_name'),
    url('users/',views.users,name="users"),
]