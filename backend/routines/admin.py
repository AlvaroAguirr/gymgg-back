from django.contrib import admin
from .models import Routina, RoutineHistory

@admin.register(Routina)
class RoutinaAdmin(admin.ModelAdmin):
    list_display = ("Routine_name", "user", "Last_time_done")
    list_filter = ("user",)
    search_fields = ("Routine_name", "user__email")

@admin.register(RoutineHistory)
class RoutineHistoryAdmin(admin.ModelAdmin):
    list_display = ("routine", "Date_realization", "Time_to_done")
    list_filter = ("Date_realization",)