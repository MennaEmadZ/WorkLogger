import datetime
from django.forms import DateField
from django.views import View
from log.forms import LogHoursForm
from .models import *
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum

class LogHoursView(LoginRequiredMixin, View):
    template_name = 'home.html'
    
 
    def get(self, request, *args, **kwargs):
        # load form
        session_user= request.user.id
        username = User.objects.get(id=session_user)
        form = LogHoursForm(request.POST)
        form.user_id= get_object_or_404(User, id=session_user) 
        
        

        return  render(request, self.template_name, {'log_form':form, 'user': username})

    def post(self, request):
        session_user= request.user
        form = LogHoursForm(request.POST)
    
        if form.is_valid():
            log = form.save(commit=False)
            
            date = datetime.datetime.strptime(request.POST['date'], "%Y-%m-%d").date()

            currentdate=datetime.date.today()
            now = str(currentdate.strftime("%Y-%m-%d"))
            today = datetime.datetime.strptime(now, "%Y-%m-%d").date()
            
            if date < today:
                log.is_late=True
            else:
                log.is_late=False
            log.user= get_object_or_404(User, id=session_user.id)
            log.save()
            return  render(request, self.template_name, {'log_form':form})
       
class logView(LoginRequiredMixin, View):
    model = Log
    template_name = 'home.html'
    def get(self, request):

        session_user= request.user.id
        date = request.GET['date']
        date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        #view total logs 
        
        start_week = date - datetime.timedelta(date.weekday())
        end_week = start_week + datetime.timedelta(7)

        total_today_log = Log.objects.filter(date=date, user_id=session_user).aggregate(Sum('duration'))
        
        week_log = Log.objects.filter(date__range=[start_week, end_week], user_id=session_user).aggregate(Sum('duration'))
       
        month_log = Log.objects.filter(date__month=date.month, user_id=session_user).aggregate(Sum('duration'))
       
        today_log = Log.objects.filter(date=date, user_id=session_user)

        return render(request, self.template_name, {'total_today_log': total_today_log, 'week_log': week_log, 'month_log':month_log, 'today_log':today_log})



