from django.urls import path
from .views.view1 import view1
from .views.view2 import view2
from .views.view3 import view3

urlpatterns = [
    path('view1/', view1, name='view1'),
    path('view2/', view2, name='view2'),
    path('view3/', view3, name='view3'),
]
