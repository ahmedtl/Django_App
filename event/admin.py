from django.contrib import admin, messages
from .models import *
# Register your models here.

# admin.site.register(Event)
admin.site.register(participants)


class participantsInline(admin.TabularInline):
    model = participants
    readonly_fields = ('date_participation',)
    can_delete = True
    classes = ['collapse']


def accept_state(modeladmin, request, queryset):
    rows_update = queryset.update(state=True)

    if (rows_update == 1):
        message_bit = "1 event was"
    else:
        message_bit = f"{rows_update} events were"

    messages.success(request, f"{message_bit} successfully accepted")


def refuse_state(modeladmin, request, queryset):
    rows_update = queryset.update(state=False)

    if (rows_update == 1):
        message_bit = "1 event was"
    else:
        message_bit = f"{rows_update} events were"

    messages.success(request, f"{message_bit} successfully accepted")


accept_state.short_description = "state accepted"
refuse_state.short_description = "state refused"


class upcomingEvent(admin.SimpleListFilter):
    title = 'Event Date'
    parameter_name = 'evt_date'

    def lookups(self, request, model_admin):
        return (
            ('Past', ("Past Events")),
            ('Upcoming Events', ("Upcoming Events")),
            ('Today Events', ("Today Events")),
        )

    def queryset(self, request, queryset):
        if self.value() == 'Past':
            return queryset.filter(evt_date__lt=datetime.today())
        if self.value() == 'Upcoming Events':
            return queryset.filter(evt_date__gt=datetime.today())
        if self.value() == 'Today Events':
            return queryset.filter(evt_date__exact=datetime.today())


@admin.register(Event)
class eventAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'image',
        'description',
        'state',
        'categoy',
        'nbr_participant',
        'evt_date',
        'organisateur',
        'created_date',
        'updated_date',
        'event_participants'
    )

    actions = [accept_state, refuse_state]

    inlines = [participantsInline]

    # fields = (
    #     ('title','categoy'),'state'
    # )

    list_filter = ('categoy', 'state',upcomingEvent,)

    fieldsets = (
        (
            'State',
            {
                'fields': ('state',)
            }
        ),
        (
            'About',
            {
                'fields': (
                    (
                        'title',
                        'image',
                        'categoy',
                        'organisateur',
                        'description'
                    )
                )
            }
        ),
        (
            'Dates',
            {
                'fields': (
                    (
                        'evt_date',
                        'created_date',
                        'updated_date'
                    )
                )
            }
        )
    )

    # autocomplete_fields = ['organisateur']

    ordering = ['title']

    readonly_fields = ('created_date', 'updated_date')

    def event_participants(self, obj):
        count = obj.participant.count()
        return count

    event_participants.short_description = 'nombre de participants'

    search_fields = ['title']
