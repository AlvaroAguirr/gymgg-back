from django.contrib import admin
from .models import Routina, RoutineHistory,Exercise

@admin.register(Routina)
class RoutinaAdmin(admin.ModelAdmin):
    list_display = ("Routine_name", "user", "Last_time_done")
    list_filter = ("user",)
    search_fields = ("Routine_name", "user__email")

@admin.register(RoutineHistory)
class RoutineHistoryAdmin(admin.ModelAdmin):
    list_display = ("routine", "Date_realization", "Time_to_done")
    list_filter = ("Date_realization",)


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_filter = ("recommended_level", "goal_type")