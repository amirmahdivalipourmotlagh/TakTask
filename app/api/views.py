from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import IsAuthenticated , IsAdminUser ,AllowAny
from rest_framework.response import Response
from .serializers import *
from user.models import *
from Task.models import * 
import datetime


@api_view(['GET'])
@permission_classes([AllowAny])
def getRoutes(request):
    routes=[
        {'POST':'/api/users/login/'},
        {'POST':'/api/users/login/refresh/'},
    ]
    return Response(routes)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def AllTasks1(request):
    user  = request.user
    user_des = User_describtion.objects.get(user=user)
    livetasks = task.objects.filter(user=user_des)
    serialized_live_task = taskserializer(livetasks,many=True)
    # res = {
        
    # }
    return Response(serialized_live_task.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def AllTasks(request,team_id,user_id=None):
    this_user = request.user
    this_user_des = User_describtion.objects.get(user = this_user)
    if user_id == None:
        user = this_user_des
    else:
        user  = User_describtion.objects.get(id = user_id)
    teami  = Team.objects.get(id = team_id)
    if this_user_des == user :
        chosen_tasks = task.objects.filter(user=this_user_des).filter(team__id=team_id)
        serialized_live_task = taskserializer(chosen_tasks,many=True)
        res = {
            'data':serialized_live_task.data,
            'msg':'Done'
        }
    if teami in this_user_des.teams.all():
        # user_des = User_describtion.objects.get(user=user)
        chosen_tasks = task.objects.filter(user=user).filter(team__id=team_id)
        serialized_live_task = taskserializer(chosen_tasks,many=True)
        res = {
            'data':serialized_live_task.data,
            'msg':'Done'
        }
    else:
        res = {
            'msg':'you dont have access to that.'
        }
    return Response(res)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def liveTasks(request,team):
    user  = request.user
    user_des = User_describtion.objects.get(user=user)
    livetasks = task.objects.filter(user=user_des).filter(team = team).filter(If_Done=False)
    serialized_live_task = taskserializer(livetasks,many=True)
    # res = {
        
    # }
    return Response(serialized_live_task.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def DoneTasks(request,team):
    user  = request.user
    user_des = User_describtion.objects.get(user=user)
    livetasks = task.objects.filter(user=user_des).filter(team = team).filter(If_Done=True)
    serialized_live_task = taskserializer(livetasks,many=True)
    res = {
     'data':   serialized_live_task.data,
     'msg':'Done',
    }
    return Response(res)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def UpdateTask(request,tasks):
    user  = request.user
    user_des = User_describtion.objects.get(user=user)
    this_task = task.objects.get(id = tasks)
    if user_des == this_task.user:
        this_task_qryset = task.objects.filter(id = tasks)
        # this_task_qryset.title = request.data['title']
        # if request.data['DueDate'] != '' or request.data['DueDate'] != None:
            # date_time_obj = datetime.datetime.strptime(request.data['DueDate'],'%Y-%m-%d')
        # this_task_qryset.DueDate = request.data['DueDate']
        # this_task_qryset.estimate_time = request.data['estimate_time']
        # this_task_qryset.If_Done = request.data['If_Done']
        # this_task_qryset.save()
        print(request.data['If_Done'] , type(request.data['If_Done']))
        if request.data['If_Done'] == 'False':
            this_task_qryset.update(title = request.data['title'],duedate = request.data['DueDate'],
                                estimate_time = request.data['estimate_time'],If_Done=request.data['If_Done'])
        else:
            done_date = datetime.datetime.today().strftime('%Y-%m-%d')
            this_task_qryset.update(title = request.data['title'],duedate = request.data['DueDate'],
                                estimate_time = request.data['estimate_time'],If_Done=request.data['If_Done'],Done_time=done_date)
        livetasks= task.objects.filter(user=user_des).filter(team = this_task.team)
        serialized_live_task = taskserializer(livetasks,many=True)
        res = {
            'Data':serialized_live_task.data,
            'msg':'Status ok'
        }
    else:
        res={
            'msg':'this task dose not belong to U.',
        }

    return Response(res)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def DeleteTask(request,tasks):
    try:
        user  = request.user
        user_des = User_describtion.objects.get(user=user)
        this_task = task.objects.get(id = tasks)
        if user_des == this_task.user:
            this_team = this_task.team
            this_task.delete()
            livetasks= task.objects.filter(user=user_des).filter(team = this_team)
            serialized_live_task = taskserializer(livetasks,many=True)
            res = {
                'Data':serialized_live_task.data,
                'msg':'Done'
            }
        else:
            res={
                'msg':'this task dose not belong to U.',
            }
    except:
        res={
                'msg':'there is a problem',
            }
    return Response(res)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def CreateTask(request,team):
    # try:
    user  = request.user
    user_des = User_describtion.objects.get(user=user)
    this_team = Team.objects.get(id = team)
    if request.data['DueDate'] == 'null' or request.data['DueDate'] == '' :
        do_d= None
    else:
        do_d = request.data['DueDate']
        
    if request.data['estimate_time'] == 'null' or request.data['estimate_time'] == '' :
        es_t= None
    else:
        es_t = request.data['estimate_time']
    task.objects.create(title=request.data['title'],user=user_des,team=this_team,duedate=do_d,estimate_time=es_t)
    # this_task = task.objects.get(id = tasks)
    livetasks= task.objects.filter(user=user_des).filter(team = this_team)
    serialized_live_task = taskserializer(livetasks,many=True)
    res = {
        'Data':serialized_live_task.data,
        'msg':'Done'
    }
    # except:
    #     res={
    #         'msg':'there is a problem with creation',
    #     }
    return Response(res)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def CreateSpendTime(request,taski):
    try:
        user  = request.user
        user_des = User_describtion.objects.get(user=user)
        this_task = task.objects.get(id=taski)
        this_team = this_task.team
        if this_task.user == user_des:
            do_d = request.data['start_date']
            es_t = request.data['spended']
            this_spent_time = SpentTime.objects.create(start_date=do_d,spended=es_t,related_task=this_task,related_user=user_des,related_team=this_team)
            this_task.time_spented_up.add(this_spent_time)
            serialized_this_task = taskserializer(this_task,many=False)
            res = {
                'Data':serialized_this_task.data,
                'msg':'Done'
            }
        else:
            res={
                'msg':'you dont have access to this task',
            }
    except:
        res={
            'msg':'there is a problem with creation please check your inputs.',
        }
    return Response(res)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def UpdateSpendTime(request,spend_id):
    # try:
    user  = request.user
    user_des = User_describtion.objects.get(user=user)
    this_st = SpentTime.objects.filter(id=spend_id)
    this_st_get = SpentTime.objects.get(id=spend_id)
    rel_task = this_st_get.related_task
    owner = this_st_get.related_task.user
    if owner == user_des:
        do_d = request.data['start_date']
        es_t = request.data['spended']
        this_st.update(start_date=do_d,spended=es_t,related_task=rel_task)
        # this_task.time_spented_up.add(this_spent_time)
        serialized_this_task = spendserializer(this_st,many=False)
        res = {
            # 'Data':serialized_this_task.data,
            'msg':'Done'
        }
    else:
        res = {
            'msg':'this object dosen\'t belong to you.'
        }
    # except:
    #     res={
    #         'msg':'there is a problem with update please check your inputs.',
    #     }
    return Response(res)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def DeleteSpendTime(request,spend_id):
    try:
        user  = request.user
        user_des = User_describtion.objects.get(user=user)
        this_st = SpentTime.objects.get(id=spend_id)
        owner = this_st.related_task.user
        if owner == user_des:
            this_st.delete()
            # this_task.time_spented_up.add(this_spent_time)
            # serialized_this_task = spendserializer(this_st,many=False)
            res = {
                # 'Data':serialized_this_task.data,
                'msg':'Done'
            }
        else:
            res = {
                'msg':'this object dosen\'t belong to you.'
            }
    except:
        res={
            'msg':'there is a problem with creation please check your inputs.',
        }
    return Response(res)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def GetTeam(request):
    try:
        user  = request.user
        user_des = User_describtion.objects.get(user=user)
        teams = user_des.teams
        ser_teams = teamserializer(teams,many=True)
        res = {
            'Data':ser_teams.data,
            'msg':'Done'
        }
    except:
        res = {
            'msg':'There is a problem with loading your teams.'
        }
    return Response(res)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def GetChartData(request,useri,teami):
    user = request.user
    user_prof = User_describtion.objects.get(user=user)
    user_target = User_describtion.objects.get(id=useri)
    team_target = Team.objects.get(id = teami)
    IsAllowed = False
    if user_target in team_target.users.all() and user_target in team_target.users.all():
        IsAllowed = True
    if IsAllowed == False:
        res = {
            'msg':'you are not allowed'
        }
        return Response(res)
    current_date = datetime.datetime.strptime(request.data['nowdate'],'%Y-%m-%d')   
    daily_time = []
    temp_day = current_date
    while True:
        if temp_day.weekday() == 4:
            break
        daily_time.append(0)
        temp_day = temp_day + datetime.timedelta(days=1)
        mounth_range = mounth_range - 1
    for single_date in (current_date - datetime.timedelta(n) for n in range(mounth_range)):
        this_st = SpentTime.objects.filter(start_date=single_date).filter(related_user= user_target).filter(related_team=team_target)
        temp_day_time = 0
        for st in this_st:
            temp_day_time = temp_day_time + st.spended
        daily_time.append(temp_day_time)
        # ser_ST = spendserializer(this_st,many=True) 
    res = {
            'Data':{
                'weaks':daily_time,
            },
            'msg':'Done'
        }
    return Response(res)
    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def GetChartDataOwn(request,teami):
    user = request.user
    user_target = User_describtion.objects.get(user=user)
    team_target = Team.objects.get(id = teami)
    current_date = datetime.datetime.strptime(request.data['nowdate'],'%Y-%m-%d')   
    daily_time = []
    mounth_range = 28
    temp_day = current_date
    while True:
        if temp_day.weekday() == 4:
            break
        daily_time.append(0)
        temp_day = temp_day + datetime.timedelta(days=1)
        mounth_range = mounth_range - 1
    for single_date in (current_date - datetime.timedelta(n) for n in range(mounth_range)):
        this_st = SpentTime.objects.filter(start_date=single_date).filter(related_team= team_target)
        temp_day_time = 0
        for st in this_st:
            temp_day_time = temp_day_time + st.spended
        daily_time.append(temp_day_time)
        # ser_ST = spendserializer(this_st,many=True) 
    res = {
            'Data':{
                'weaks':daily_time,
            },
            'msg':'Done'
        }
    return Response(res)
    


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def ReportUsers(request,team_id):
    user = request.user
    user_des = User_describtion.objects.get(user=user)
    this_team = Team.objects.get(id = team_id)
    if this_team in user_des.teams.all():
        current_date = datetime.datetime.strptime(request.data['nowdate'],'%Y-%m-%d').date()
        team_members = this_team.users.all()
        res = dict()
        for temp_user in team_members:
            res['{}'.format(temp_user.username)] = {
                    'Alltasks':0,
                    'DoneTasks':0,
                    'SpentTime':0,
                    'TimePerDay':0,
                    'user_id':temp_user.id,

            } 
        days_before = current_date
        z = 0
        while(True):
            for temp_user in team_members:
                live_now_tasks = task.objects.filter(user=temp_user)
                live_count_now_task = len(live_now_tasks)
                res['{}'.format(temp_user.username)]['Alltasks'] =  live_count_now_task
                now_tasks = task.objects.filter(user=temp_user).filter(If_Done=True).filter(Done_time=days_before)
                count_now_task = len(now_tasks)
                res['{}'.format(temp_user.username)]['DoneTasks'] =  res['{}'.format(temp_user.username)]['DoneTasks'] + count_now_task
                for temp_task in now_tasks:
                    now_sts = SpentTime.objects.filter(related_user = temp_user).filter(related_team=this_team).filter(start_date=days_before)
                    for st_temp in now_sts:
                        print(st_temp.spended)
                        res['{}'.format(temp_user.username)]['SpentTime'] =  res['{}'.format(temp_user.username)]['SpentTime'] + st_temp.spended
            if days_before.weekday() == 6:
                break
            days_before = (days_before-datetime.timedelta(days=1))
            z = z + 1
        for temp_user in team_members:
            res['{}'.format(temp_user.username)]['TimePerDay'] = res['{}'.format(temp_user.username)]['SpentTime'] / z
        res['range'] = '{} <to> {}'.format(days_before,current_date)
        res['msg'] = 'Done'
    else:
        res = {
                'msg':'you dont have access to this team'
            }
    return Response(res)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def FullReportUsers(request,team_id):
    user = request.user
    user_des = User_describtion.objects.get(user=user)
    this_team = Team.objects.get(id = team_id)
    if this_team in user_des.teams.all():
        # current_date = datetime.datetime.strptime(request.data['nowdate'],'%Y-%m-%d').date()
        team_members = this_team.users.all()
        res = dict()
        for temp_user in team_members:
            res['{}'.format(temp_user.username)] = {
                    'DoneTasks':0,
                    'LiveTasks':0,
                    'SpentTime':0,
                    'user_id':temp_user.id,
            } 
        # days_before = current_date
        for temp_user in team_members:
            now_done_tasks = task.objects.filter(user=temp_user).filter(If_Done=True).count()
            now_live_tasks = task.objects.filter(user=temp_user).filter(If_Done=False).count()
            res['{}'.format(temp_user.username)]['DoneTasks'] =  res['{}'.format(temp_user.username)]['DoneTasks'] + now_done_tasks
            res['{}'.format(temp_user.username)]['LiveTasks'] =  res['{}'.format(temp_user.username)]['LiveTasks'] + now_live_tasks
            # for temp_task in now_tasks:
            now_sts = SpentTime.objects.filter(related_user = temp_user).filter(related_team=this_team)
            for st_temp in now_sts:
                res['{}'.format(temp_user.username)]['SpentTime'] =  res['{}'.format(temp_user.username)]['SpentTime'] + st_temp.spended
        res['range'] = 'ALL'
        res['msg'] = 'Done'
    else:
        res = {
                'msg':'you dont have access to this team'
            }
    return Response(res)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def FixTasks(request):
    doneTasks = task.objects.filter(If_Done = True)
    done_date = datetime.datetime.today().strftime('%Y-%m-%d')
    for dt in doneTasks:
        temp_dt = task.objects.get(id = dt.id)
        temp_dt.Done_time = done_date
        temp_dt.save()
        res = {
                'msg':'Done'
            }
    return Response(res)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def FixSp(request):
    AllSp = SpentTime.objects.all()
    for sp in AllSp:
        r_task = sp.related_task
        r_user = r_task.user
        r_team = r_task.team
        temp_sp = SpentTime.objects.get(id = sp.id)
        temp_sp.related_user = r_user
        temp_sp.related_team = r_team
        temp_sp.save()
        res = {
                'msg':'Done'
            }
    return Response(res)