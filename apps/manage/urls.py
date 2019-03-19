from django.urls import path
from apps.manage.views import *

urlpatterns = [
    path('', index),
    path('doc', doc_view),
    path('user_manage', user_manage_view),
    path('role_manage', role_manage_view),
    path('dept_manage', dept_manage_view),
    path('app_token_manage', app_token_manage_view),
    path('workflow_manage', workflow_manage_view),
    path('run_script_manage', run_script_manage_view),
    path('notice_manage', notice_manage_view),
]