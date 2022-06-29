from django.db.models.signals import post_delete,post_save , m2m_changed
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import *




@receiver(post_save,sender=SpentTime)
def add_tracked_time(sender,instance,created,**kwargs):
    st = instance
    tst = st.related_task
    all_task = task.objects.all()
    this_st = SpentTime.objects.filter(id=st.id)
    for temp_task in all_task :
        try:
            temp_task.time_spented_up.remove(st)
        except:
            pass    
    tst.time_spented_up.add(st)
    this_st.update(related_team=tst.team,related_user=tst.user)

@receiver(post_save,sender=task)
def add_tracked_time(sender,instance,created,**kwargs):
    if not created:
        print('not created')
        sti = instance
        st = task.objects.filter(id = sti.id)
        print(sti)
        print(st)
        if sti.If_Done == True and sti.orginal_done == False:
            print(datetime.datetime.now().date())
            st = task.objects.filter(id = sti.id).update(Done_time = datetime.datetime.now().date())
            print('Done')
            sti.orginal_done = True
            sti.Done_time = datetime.datetime.now().date()
            sti.save()