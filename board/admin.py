from django.contrib import admin

from board.models import Ad


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price',)