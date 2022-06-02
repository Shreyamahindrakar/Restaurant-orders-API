from django.urls import path
from menu import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('create-order/', views.CreateMenuView.as_view(), name='create_order'),
    path('allMenuItem/all/<str:id>/',views.Menuview.as_view(),name="menu_item"),
    path('Menuitem/all/',views.Menuview.as_view(),name="menu_item"),
    path('menu-item/get/<str:id>/',views.SingleMenuView.as_view(),name="Get_Menu"),
    path('search-menu/',views.SearchMenuView.as_view(),name="search_menu"),
    path('recent-order/',views.OrderStatusView.as_view(),name="recent order status"),
    path('past-order/',views.OrderStatusView.as_view(),name="past_order_status")
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)