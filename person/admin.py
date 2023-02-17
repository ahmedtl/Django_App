from django.contrib import admin
from .models import Person
# Register your models here.
# admin.site.register(Person)


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'last_login',
        'cin',
        'first_name',
        'last_name',
        'is_superuser',
        'is_staff',
        'password',
        'date_joined'
    )

    list_per_page = 3

    search_fields = ['username']
