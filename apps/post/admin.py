from django.contrib import admin
from .models import Banner, About


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('caption', 'active')
    list_filter = ('active',)
    search_fields = ('caption',)