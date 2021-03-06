from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from registration.models import Profile
# Create your views here.

class ProfilesListView(ListView):
	model = Profile
	paginate_by = 9
	template_name = 'profiles/profiles_list.html'

class ProfileDetailView(DetailView):
	model = Profile
	template_name = 'profiles/profiles_detail.html'
	def get_object(self):
		return get_object_or_404(Profile, user__username=self.kwargs['username'])  




