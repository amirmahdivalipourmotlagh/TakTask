# from asyncio.windows_events import NULL
from django.db.models.signals import post_delete,post_save , m2m_changed
from .models import *
from django.contrib.auth.models import User
from django.dispatch import receiver


@receiver(post_save,sender=User)
def create_describtion(sender,instance,created,**kwargs):
    if created:
        user = instance
        user_profile = User_describtion.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            first_name = str(user.first_name),
            last_name = str(user.last_name),
            create_time = user.date_joined,
        )
    if not created:
        user = instance
        user_profile = User_describtion.objects.filter(user = user).update(
            username=user.username,
            email=user.email,
            first_name = str(user.first_name),
            last_name = str(user.last_name),
            create_time = user.date_joined,
        )

@receiver(post_delete,sender=User)
def delete_user(sender,instance,**kwargs):
    user = User_describtion.objects.filter(user = user)
    user.delete()


# @receiver(post_save,sender=User_describtion)
# def updateTeam(sender,instance,created,**kwargs):
#     if created:
#         user = instance
#         site_teams = Team.objects.all()
#         for u in site_teams:
#             u.users.remove(user)
#         teams_all = user.teams.all()
#         teams_all_list = list(teams_all)
#         print ("teams:",teams_all)
#         if len(teams_all_list) != 0 :
#             for team in teams_all:
#                 # print("user : ",user)
#                 # print("team : ",team)
#                 user_Team = Team.objects.get(id = team.id).users.add(user)
#     if not created:
#         user = instance
#         site_teams = Team.objects.all()
#         for u in site_teams:
#             u.users.remove(user)
#         teams_all = user.teams.all()
#         teams_all_list = list(teams_all)
#         print ("teams:",teams_all)
#         if  len(teams_all_list) != 0:
#             for team in teams_all:
#                 # print("user : ",user)
#                 # print("team : ",team)
#                 user_Team = Team.objects.get(id = team.id)
#                 if user in user_Team.users.all():
#                     continue
#                 else:
#                     user_Team.users.add(user)

# @receiver(post_save,sender=Team)
# def updateTeam(sender,instance,created,**kwargs):
#     if created:
#         team = instance
#         site_users = User_describtion.objects.all()
#         for u in site_users:
#             u.teams.remove(team)
#         users_all = team.users.all()
#         users_all_list = list(users_all)
#         print ("users:",users_all)
#         if len(users_all_list) != 0  :
#             for user in users_all:
#                 print("user : ",user.id)
#                 print("team : ",team.id)
#                 team_user = User_describtion.objects.get(id = user.id).teams.add(team)
#     if not created:
#         team = instance
#         users_all = team.users.all()
#         site_users = User_describtion.objects.all()
#         for u in site_users:
#             u.teams.remove(team)
#         users_all_list = list(users_all)
#         print ("users:",users_all)
#         if len(users_all_list) != 0 :
#             print("yes")
#             for user in users_all:
#                 print("user : ",user.id)
#                 print("team : ",team.id)
#                 team_user = User_describtion.objects.get(id = user.id)
#                 if team in team_user.teams.all():
#                     pass
#                 else:
#                     team_user.teams.add(team)
@receiver(m2m_changed,sender=User_describtion.teams.through)
def updateTeam(sender, instance, action, **kwargs):
    print(action)
    if action in ('post_add'):
        user = instance
        users_all = user.teams.all()
        print("allusers = ",users_all)
        site_users = Team.objects.all()
        for u in site_users:
            if u not in users_all:
                u.users.remove(user)
        # if users_all != pre_users_all:
        # user = instance
        print(user.teams.all())
        teams_all = user.teams.all()
        teams_all_list = list(teams_all)
        print ("teams:",teams_all)
        if  len(teams_all_list) != 0:
            for team in teams_all:
                # print("user : ",user)
                # print("team : ",team)
                user_Team = Team.objects.get(id = team.id)
                if user in user_Team.users.all():
                    continue
                else:
                    user_Team.users.add(user)
        # else:
        #     pass

@receiver(m2m_changed,sender=Team.users.through)
def updateTeam(sender, instance, action, **kwargs):
    print(action)
    if action in ('post_add','post_remove'):
        team = instance
        users_all = team.users.all()
        print("allusers = ",users_all)
        # users_all_list = list(users_all)
        print ("users:",users_all)
        user_all_list = list(users_all)
        site_users = User_describtion.objects.all()
        for u in site_users:
            if u not in users_all:
                u.teams.remove(team)
        if len(user_all_list) != 0 :
            print("yes")
            for user in users_all:
                print("user : ",user.id)
                print("team : ",team.id)
                team_user = User_describtion.objects.get(id = user.id)
                if team in team_user.teams.all():
                    pass
                else:
                    team_user.teams.add(team)
        # else:
        #     pass