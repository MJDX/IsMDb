from django.contrib import admin

# Register your models here.
from review.models import *

admin.site.register(Cast)
admin.site.register(Suggestion)
admin.site.register(MovieReview)
admin.site.register(ReactComment)
admin.site.register(ReportComment)
admin.site.register(ReportMember)
admin.site.register(ReportReview)
admin.site.register(UpVote)
admin.site.register(MovieCast)

