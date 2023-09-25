from django.urls import reverse
from django.views.generic.base import TemplateView, View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.conf import settings
from django.http.response import JsonResponse
import stripe
from .models import Item



class ItemListView(ListView):
    model = Item
    template_name = "items/items_list.html"
    context_object_name = 'items'


class SuccessView(TemplateView):
    template_name = 'items/success.html'


class CancelledView(TemplateView):
    template_name = 'items/cancelled.html'


class ItemDetailView(DetailView):
    model = Item
    template_name = "items/item_detail.html"
    pk_url_kwarg = 'pk'
    context_object_name = 'item'

    def get_context_data(self, **kwargs):
        context = super(ItemDetailView, self).get_context_data(**kwargs)
        context['STRIPE_PUBLIC_KEY'] = settings.STRIPE_PUBLIC_KEY
        return context


class CreateCheckoutSessionView(View):
    def get(self, request, *args, **kwargs):
        item = Item.objects.get(pk=kwargs['pk'])
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            session = stripe.checkout.Session.create(
                line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                    'name': item.name,
                    },
                    'unit_amount': int(item.price),
                },
                'quantity': 1,
                }],
                mode='payment',
                success_url='http://localhost:8000/success',
                cancel_url='http://localhost:8000/cancel',
            )    
            return JsonResponse({'session_id': session.id})
        except Exception as e:
            return JsonResponse({'error': str(e)})
