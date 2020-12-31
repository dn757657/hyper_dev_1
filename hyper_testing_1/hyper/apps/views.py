from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import TemplateView
from hyper.apps.forms import NewProjectForm, NewTagForm
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

User = get_user_model()

class AppsView(LoginRequiredMixin, TemplateView):
    pass

# calendar
apps_calendar_calendar_view = AppsView.as_view(template_name="apps/calendar/calendar.html")

#chat
apps_chat_chat_view = AppsView.as_view(template_name="apps/chat/chat.html")

# ecommerce
apps_ecommerce_checkout_view = AppsView.as_view(template_name="apps/ecommerce/checkout.html")
apps_ecommerce_customers_view = AppsView.as_view(template_name="apps/ecommerce/customers.html")
apps_ecommerce_orders_details_view = AppsView.as_view(template_name="apps/ecommerce/orders-details.html")
apps_ecommerce_orders_view = AppsView.as_view(template_name="apps/ecommerce/orders.html")
apps_ecommerce_products_details_view = AppsView.as_view(template_name="apps/ecommerce/products-details.html")
apps_ecommerce_products_view = AppsView.as_view(template_name="apps/ecommerce/products.html")
apps_ecommerce_sellers_view = AppsView.as_view(template_name="apps/ecommerce/sellers.html")
apps_ecommerce_shopping_cart_view = AppsView.as_view(template_name="apps/ecommerce/shopping-cart.html")

# email
apps_email_indox_view = AppsView.as_view(template_name="apps/email/inbox.html")
apps_email_read_view = AppsView.as_view(template_name="apps/email/read.html")

# projects
apps_projects_add_view = AppsView.as_view(template_name="apps/projects/add.html")
apps_projects_details_view = AppsView.as_view(template_name="apps/projects/details.html")
apps_projects_gantt_view = AppsView.as_view(template_name="apps/projects/gantt.html")
apps_projects_list_view = AppsView.as_view(template_name="apps/projects/list.html")

# projects development
apps_projects_dev_list_view = AppsView.as_view(template_name="apps/projects_dev/list.html")
apps_projects_dev_add_old_view = AppsView.as_view(template_name="apps/projects_dev/add_old.html")
# apps_projects_dev_add_view = AppsView.as_view(template_name="apps/projects_dev/add.html")

# social
apps_social_feed_view = AppsView.as_view(template_name="apps/social/feed.html")

# tasks
apps_tasks_details_view = AppsView.as_view(template_name="apps/tasks/details.html")
apps_tasks_kanban_view = AppsView.as_view(template_name="apps/tasks/kanban.html")
apps_tasks_list_view = AppsView.as_view(template_name="apps/tasks/list.html")


def apps_projects_dev_add_view(request):

    if request.method == "POST":
        new_project_form = NewProjectForm(data=request.POST)
        # print(new_project_form['start_date'])

        if new_project_form.is_valid():

            # saving user data to database
            project_data = new_project_form.save()
            project_data.save()

            # profile = profile_form.save(commit=False)
            # # committing now would casue collisions maybe override username
            # profile.user = user

            # # dealing with user uploaded files
            # if 'profile_pic' in request.FILES:
            #     profile.profile_pic = request.FILES['profile_pic']
            #
            # profile.save()
            # TODO: add a 'project created' redirect? with option to goto or add another?
        else:
            print(new_project_form.errors)
    else:
        # request is http request?
        new_project_form = NewProjectForm()

    return render(request, 'apps/projects_dev/add.html',
                 {'project_form': new_project_form,})


def apps_projects_dev_add_tag_view(request):

    if request.method == "POST":
        new_tag_form = NewTagForm(data=request.POST)
        # print(new_project_form['start_date'])

        if new_tag_form.is_valid():

            # saving user data to database
            tag_data = new_tag_form.save()
            tag_data.save()

        else:
            print(new_tag_form.errors)
    else:
        # request is http request?
        new_tag_form = NewTagForm()
        print("I am a cunt")

    return render(request, 'apps/projects_dev/add_tag.html',
                 {'tag_form': new_tag_form,})
