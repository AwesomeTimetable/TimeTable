from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Deadline, Tag, Course
from .forms import DeadlineForm


# Create your views here.
def index(request):
    """
    index of the page
    :param request:
    :return:
    """
    return render(request, 'dashboard.html')


class DeadlinesView(generic.CreateView, LoginRequiredMixin):
    template_name = 'timetable/deadline.html'
    model = Deadline
    context_object_name = 'deadline_sets'
    form_class = DeadlineForm
    success_url = '/timetable/deadlines/'

    def get_queryset(self):
        return Deadline.objects.order_by('created_time')

    def get_initial(self):
        return {
            'user': self.request.user,
        }

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(generic.CreateView, self).get_context_data(**kwargs)
        context['deadline_form'] = DeadlineForm()
        return context


class TagsView(generic.ListView):
    template_name = 'timetable/tag'
    model = Tag


class TimetablesView(generic.ListView):
    template_name = 'timetable/timetable.html'
    model = Course

