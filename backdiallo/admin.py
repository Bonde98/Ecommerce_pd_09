'''from django.contrib import admin
from .models import Payment, Product,Order,Cart
# Register your models here.
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(Payment)'''

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .form import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser,Product,Cart,Order,Payment


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'is_admin', 'is_active',)
    list_filter = ('email', 'is_admin', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_responsible', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(CustomUser)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Payment)