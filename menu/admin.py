from django.contrib import admin
from .models import *

# Register your models here.

class MenuModelAdmin(admin.ModelAdmin):
    list_display=['id','name_item', 'category','price','discounts','platesize']
    search_fields = ['name_item',
                     'category', 
                    'price','discounts',
                    'platesize'
                    ]
admin.site.register(Menu,MenuModelAdmin)

class OrderModelAdmin(admin.ModelAdmin):
    list_display=['id','name', 'date','status']
    search_fields = ['name',
                     'date', 
                    'status',
                    ]
admin.site.register(Order,OrderModelAdmin)
