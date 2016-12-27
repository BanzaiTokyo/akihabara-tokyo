from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static

import settings
import views


urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name="index"),
    url(r'^recent$', views.HomeView.as_view(), name="recent"),
    url(r'^newregister$', views.NewRegisterView.as_view(), name="new_register"),
    url(r'^newlogin$', views.NewLoginView.as_view(), name="new_login"),
    url(r'^profile/(?P<pk>\d+)$', views.ProfileView.as_view(), name="profile"),
    url(r'^thread/(?P<pk>\d+)$', views.ThreadView.as_view(), name="thread"),
    url(r'^thankyou$', views.ThankyouView.as_view(), name="thankyou"),
    url(r'^question$', views.QuestionView.as_view(), name="question"),
    url(r'^comment$', views.CommentView.as_view(), name="comment"),
    url(r'^accounts/register/$', views.AkibaRegistrationView.as_view()),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^profile/edit$', views.ProfileEditView.as_view(), name="profile_edit"),
    url(r'^submit$', views.NewThreadView.as_view(), name="new_thread"),
    url(r'^thread/(?P<pk>\d+)/edit$', views.EditThreadView.as_view(), name="edit_thread"),
    url(r'^thread/(?P<thread_id>\d+)/reply$', views.ReplyThreadView.as_view(), name="reply_thread"),
    url(r'^comment/(?P<post_id>\d+)/reply$', views.ReplyCommentView.as_view(), name="reply_comment"),
]

# in debug mode launch debug_toolbar
if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)