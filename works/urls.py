from django.urls import path
from works.views import WorksView, WorkDetailView

urlpatterns = [
    path('', WorksView.as_view(), name='works'),
    path('work/<int:id>/', WorkDetailView.as_view(), name='work-detail'),
]
