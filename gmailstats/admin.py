from django.contrib import admin
from graphs.models import EmailAccount, Graph

class EmailAccountAdmin(admin.ModelAdmin):
    list_display = ('address', 'password')
    list_filter = ('address', )
    ordering = ('address', )

admin.site.register(EmailAccount)
admin.site.register(Graph)