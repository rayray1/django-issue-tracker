from django.contrib import admin
from issuetracker.models import Issue, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Category, CategoryAdmin)

class IssueAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'priority', 'submitter', 'submitted_date')
    list_filter = ('status', 'submitted_date')
    search_fields = ('title', 'description',)

admin.site.register(Issue, IssueAdmin)
