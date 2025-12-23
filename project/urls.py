from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static

from email_api.views import SendEmailView


# HOME PAGE VIEW
def home(request):
    return HttpResponse("""
        <h1>SkillSort — Resume Screening API</h1>
        <p>Backend server is running successfully ✓</p>
        <p>Try visiting:</p>
        <ul>
            <li>/admin/</li>
            <li>/api/upload/</li>
            <li>/api/screen/</li>
        </ul>
    """)

urlpatterns = [
    path('', home, name='home'),   # ✔️ NEW HOME PAGE ADDED
    path('admin/', admin.site.urls),
    path('api/', include('upload.urls')),
    path('api/jd/', include('jobdesc.urls')),
    path("api/send-email/", SendEmailView.as_view()),
    path("api/email/", include("email_api.urls")),
    path("api/candidate/", include("candidate.urls")),
    path('api/interview/', include('interview.urls')),
    path('api/', include('signup.urls')),
    path("api/login/", include("signup.urls")),
    path("api/hrprofile/", include("hrprofile.urls")),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
