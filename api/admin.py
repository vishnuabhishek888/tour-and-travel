from django.contrib import admin
from api.models import User, Area_Cities, State, Destination, Pick_Up, Drop, Activities, Trip_Detail
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.

class UserModelAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('id','email', 'name', 'tc', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        ('User Credentials', {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name','tc')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserModelAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'tc', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email','id')
    filter_horizontal = ()


# Now register the new UserModelAdmin...
admin.site.register(User, UserModelAdmin)


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'ts']

@admin.register(Area_Cities)
class Area_CitiesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'ts']


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ['id', 'area_cities', 'state', 'name', 'ts']

@admin.register(Pick_Up)
class Pick_UpAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Drop)
class DropAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Activities)
class ActivitiesAdmin(admin.ModelAdmin):
    list_display = ['name', 'durations', 'description']

@admin.register(Trip_Detail)
class Trip_DetailAdmin(admin.ModelAdmin):
    list_display = ['id', 'heading', 'price', 'discount', 'image', 'state', 'area_cities', 'destination']