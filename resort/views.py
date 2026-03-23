from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.db.models import Q
from django.views.generic import CreateView, DetailView, ListView, TemplateView

from .forms import BookingRequestForm, RegisterForm
from .models import Favorite, Resort


class HomeView(TemplateView):
    template_name = 'resort/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_resorts'] = Resort.objects.filter(featured=True)[:3]
        context['stats'] = {
            'resorts': Resort.objects.count(),
            'regions': Resort.objects.values('region').distinct().count(),
            'requests': 24,
        }
        return context


class CatalogView(ListView):
    model = Resort
    template_name = 'resort/catalog.html'
    context_object_name = 'resorts'
    paginate_by = 6

    def get_queryset(self):
        queryset = Resort.objects.all()
        search = self.request.GET.get('search', '').strip()
        region = self.request.GET.get('region', '').strip()
        service = self.request.GET.get('service', '').strip()
        ordering = self.request.GET.get('ordering', '').strip()

        if search:
            queryset = queryset.filter(Q(title__icontains=search) | Q(location__icontains=search))
        if region:
            queryset = queryset.filter(region=region)
        if service == 'pool':
            queryset = queryset.filter(has_pool=True)
        if service == 'wifi':
            queryset = queryset.filter(has_wifi=True)
        if ordering == 'price':
            queryset = queryset.order_by('price_from')
        elif ordering == 'rating':
            queryset = queryset.order_by('-rating')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['regions'] = Resort.REGION_CHOICES
        context['query_params'] = self.request.GET
        return context


class ResortDetailView(DetailView):
    model = Resort
    template_name = 'resort/detail.html'
    context_object_name = 'resort'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BookingRequestForm()
        if self.request.user.is_authenticated:
            context['is_favorite'] = Favorite.objects.filter(user=self.request.user, resort=self.object).exists()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = BookingRequestForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.resort = self.object
            booking.save()
            messages.success(request, 'Заявка отправлена. Мы скоро свяжемся с вами.')
            return redirect('resort_detail', pk=self.object.pk)
        context = self.get_context_data(form=form)
        return self.render_to_response(context)


class AboutView(TemplateView):
    template_name = 'resort/about.html'


class ContactView(TemplateView):
    template_name = 'resort/contacts.html'


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'resort/auth/register.html'
    success_url = '/profile/'

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        messages.success(self.request, 'Аккаунт успешно создан.')
        return response


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'resort/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['favorites'] = Favorite.objects.filter(user=self.request.user).select_related('resort')
        return context


@login_required
def toggle_favorite(request, pk):
    resort = get_object_or_404(Resort, pk=pk)
    favorite, created = Favorite.objects.get_or_create(user=request.user, resort=resort)
    if not created:
        favorite.delete()
        messages.info(request, 'Удалено из избранного.')
    else:
        messages.success(request, 'Добавлено в избранное.')
    next_url = request.POST.get('next_url') or request.META.get('HTTP_REFERER') or 'catalog'
    return redirect(next_url)
