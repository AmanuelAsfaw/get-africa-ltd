from django.contrib import admin

from opal_app.models import ExportedOpal, GemStone, Message, OpalCollection, OpalProduct

# Register your models here.

admin.site.register(OpalProduct)
admin.site.register(OpalCollection)
admin.site.register(GemStone)
admin.site.register(ExportedOpal)
admin.site.register(Message)