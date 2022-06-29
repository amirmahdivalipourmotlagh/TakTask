from django import views
from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView , TokenRefreshView

urlpatterns=[
    path('',views.getRoutes),
    path('users/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('tasks/all/<str:team_id>/<str:user_id>', views.AllTasks, name='AllTasks'),
    path('tasks/all/<str:team_id>/', views.AllTasks, name='AllTasks'),
    path('tasks/all1/', views.AllTasks1, name='AllTasks1'),
    path('tasks/live/<str:team>', views.liveTasks, name='liveTasks'),
    path('tasks/Done/<str:team>', views.DoneTasks, name='DoneTasks'),
    path('tasks/update/<str:tasks>', views.UpdateTask, name='UpdateTask'),
    path('tasks/delete/<str:tasks>', views.DeleteTask, name='DeleteTask'),
    path('tasks/create/<str:team>', views.CreateTask, name='CreateTask'),
    path('ST/create/<str:taski>', views.CreateSpendTime, name='CreateST'),
    path('ST/update/<str:spend_id>', views.UpdateSpendTime, name='UpdateST'),
    path('ST/delete/<str:spend_id>', views.DeleteSpendTime, name='DeleteST'),
    path('teams', views.GetTeam, name='GetTeams'),
    path('chartdata/<str:teami>', views.GetChartDataOwn, name='GetChartDataOwn'),
    path('chartdata/<str:useri>/<str:teami>', views.GetChartData, name='GetChartData'),
    path('report/<str:team_id>', views.ReportUsers, name='ReportUsers'),
    path('fullreport/<str:team_id>', views.FullReportUsers, name='FullReportUsers'),
]