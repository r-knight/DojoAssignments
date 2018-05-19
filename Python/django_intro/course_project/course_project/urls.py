from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin

from apps.awesomeApp.models import User as U, Fruit, Donut, Group

class UAdmin(admin.ModelAdmin):
    pass
admin.site.register(U, UAdmin)
class FruitAdmin(admin.ModelAdmin):
    pass
admin.site.register(Fruit, FruitAdmin)
class DonutAdmin(admin.ModelAdmin):
    pass
admin.site.register(Donut, DonutAdmin)
class GroupAdmin(admin.ModelAdmin):
    pass
admin.site.register(Group, GroupAdmin)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('apps.courses.urls'))
]
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += (
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )