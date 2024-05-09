from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.text import gettext_lazy as _
from .models import User


class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'first_name', 'last_name',
                    'gender', 'email', 'mobile',
                    'is_staff', 'is_active',
                    )

    list_filter = ('is_active', 'is_staff',
                   )

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_('Personal Details'), {'fields': ('first_name', 'last_name',
                                            'gender', 'mobile', 'photo',
                                            )
                                 }
         ),
        (_('Permissions'), {'fields': ('is_staff', 'is_active',
                                       'groups', 'user_permissions'
                                       )
                            }
         ),
        (_('Important Dates'), {'fields': ('date_joined', 'modified',)
                                }
         ),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('password1', 'password2'),
        }),
        (_('Personal Details'), {'fields': ('first_name', 'last_name',
                                            'gender', 'email',
                                            'mobile', 'photo',
                                            )
                                 }
         ),
        (_('Permissions'), {'fields': ('is_staff', 'is_active',
                                       'groups', 'user_permissions'
                                       )
                            }
         ),
    )

    search_fields = ('email', 'mobile', 'first_name',
                     'last_name', 'user_uuid'
                     )

    ordering = ('id',)
    readonly_fields = ('date_joined', 'modified')



admin.site.register(User, CustomUserAdmin)