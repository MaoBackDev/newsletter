from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import *
from django.conf import settings
from django.core.mail import send_mail, EmailMessage

from newsletter.models import Newsletter
from newsletter.forms import NewsletterForm


class DashboardHomeView(TemplateView):
    template_name = 'dashboard/index.html'


class NewsletterDashboardHomeView(View):
    template_name = 'dashboard/list.html'

    def get(self, request, *args, **kwargs):
        newsletters = Newsletter.objects.all()
        context = {
            'newsletters': newsletters
        }
        return render(request, self.template_name, context)


class NewsletterCreateView(View):
    template_name = 'dashboard/create.html'

    def get(self, request, *args, **kwargs):
        form = NewsletterForm()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = NewsletterForm(request.POST or None)

            if form.is_valid():
                instance = form.save()
                newsletter = Newsletter.objects.get(id=instance.id)

                if newsletter.status == 'Published':
                    subject = newsletter.subject
                    body = newsletter.body
                    from_email = settings.EMAIL_HOST_USER

                    for email in newsletter.email.all():
                        send_mail(subject=subject, from_email=from_email, recipient_list=[email], message=body, fail_silently=True)

                return redirect('dashboard:list')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


class NewsletterDetailView(View):
    template_name = 'dashboard/detail.html'

    def get(self, request, pk, *args, **kwargs):
        newsletter = get_object_or_404(Newsletter, pk=pk)
        context = {
            'newsletter': newsletter
        }
        return render(request, self.template_name, context)


class NewsletterUpdateView(UpdateView):
    model=Newsletter
    form_class=NewsletterForm
    template_name='dashboard/update.html'
    success_url='/dashboard/detail/2/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type':'update'
        })
        return context

    def post(self, request, pk, *args, **kwargs):

        newsletter = get_object_or_404(Newsletter, pk=pk)
        if request.method == 'POST':
            form = NewsletterForm(request.POST or None)

            if form.is_valid():
                instance = form.save()
                newsletter = Newsletter.objects.get(id=instance.id)

                if newsletter.status == 'Published':
                    subject = newsletter.subject
                    body = newsletter.body
                    from_email = settings.EMAIL_HOST_USER

                    for email in newsletter.email.all():
                        send_mail(subject=subject, from_email=from_email, recipient_list=[email], message=body, fail_silently=True)

                return redirect('dashboard:detail', pk=newsletter.id)
            return redirect('dashboard:detail', pk=newsletter.id)
        else:
            form = NewsletterForm(instance=newsletter)
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


class NewsletterDeleteView(DeleteView):
    model=Newsletter
    template_name='dashboard/delete.html'
    success_url='/dashboard/list/'