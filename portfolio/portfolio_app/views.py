from django.views.generic import TemplateView
from .models import Experience, Project, Skill

class PortfolioView(TemplateView):
    """
    A class-based view to display the portfolio page.
    It fetches data from the models and passes it to the template context.
    """
    template_name = 'portfolio_app/home.html'

    def get_context_data(self, **kwargs):
        """
        Retrieves data from the database and adds it to the context dictionary.
        """
        # Call the base implementation first to get the context
        context = super().get_context_data(**kwargs)
        
        # Add your custom data to the context
        context['experiences'] = Experience.objects.all().order_by('-start_date')
        context['projects'] = Project.objects.all().order_by('id')
        context['skills'] = Skill.objects.all().order_by('category')
        
        return context