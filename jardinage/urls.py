from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^jardin/$', JardinList.as_view(), name='jardin'),
    url(r'^jardin/add', JardinCreate.as_view(), name='add_jardin'),
    url(r'^jardin/update/(?P<pk>\d+)/$', JardinUpdate.as_view(), name='update_jardin'),
    url(r'^jardin/delete/(?P<pk>\d+)/$', JardinDelete.as_view(), name='delete_jardin'),

    #-----------------------------plante------------------------------------------------------

    url(r'^plante/$', PlanteList.as_view(), name='plante'),
    url(r'^plante/add', PlanteCreate.as_view(), name='add_plante'),
    url(r'^plante/update/(?P<pk>\d+)/$', PlanteUpdate.as_view(), name='update_plante'),
    url(r'^plante/delete/(?P<pk>\d+)/$', PlanteDelete.as_view(), name='delete_plante'),

    #-----------------------------variete------------------------------------------------------

    url(r'^variete/$', VarieteList.as_view(), name='variete'),
    url(r'^variete/add', VarieteCreate.as_view(), name='add_variete'),
    url(r'^variete/update/(?P<pk>\d+)/$', VarieteUpdate.as_view(), name='update_variete'),
    url(r'^variete/delete/(?P<pk>\d+)/$', VarieteDelete.as_view(), name='delete_variete'),

]
