"""VideoStream URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import categoryview, episodeview
from . import showview
from . import AdminView
from . import UserView
urlpatterns = [
    path('admin/', admin.site.urls),
    #User
    path('userview/',UserView.UserView),
    path('preview/',UserView.Preview),
    path('tvpreview/',UserView.TvPreview),
    path('sports/',UserView.Sports),
    path('userdetailssubmit/', UserView.UserDetailsSubmit),
    path('checkmobilenumber/', UserView.CheckMobileNumber),
    path('usersession/', UserView.UserSession),
    path('userlogout/', UserView.UserLogout),
    path('searching/', UserView.Searching),

    #Admin
    path('adminlogin/',AdminView.AdminLogin),
    path('chklogin', AdminView.CheckLogin),

    #category
    path('categoryinterface/',categoryview.categoryInterface),
    path('submitcategory',categoryview.SubmitCategory),
    path('displayallcategory/', categoryview.DisplayAll),
    path('categorybyid/', categoryview.CategoryById),
    path('editdeletecategorydata/', categoryview.EditDeleteCategoryData),
    path('editicon',categoryview.EditIcon),
    path('displayalljson/', categoryview.DisplayAllJSON),

    #show
    path('showinterface/',showview.ShowInterface),
    path('submitshow',showview.SubmitShow),
    path('displayallshow/',showview.ShowAll),
    path('showbyid/',showview.ShowById),
    path('editdeleteshowdata/',showview.EditDeleteShowData),
    path('editposter', showview.EditPoster),
    path('edittrailer', showview.EditTrailer),
    path('editvideo', showview.EditVideo),
    path('displayallshowjson/', showview.DisplayAllShowJSON),

    #Episode
    path('episodeinterface/',episodeview.EpisodeInterface),
    path('submitepisode',episodeview.SubmitEpisode),
    path('displayallepisode/',episodeview.DisplayAll),
    path('episodebyid/',episodeview.EpisodeById),
    path('editdeleteepisodedata/',episodeview.EditDeleteEpisodeData),
    path('editepisodeposter', episodeview.EditEpisodePoster),
    path('editepisodetrailer', episodeview.EditEpisodeTrailer),
    path('editepisodevideo', episodeview.EditEpisodeVideo),


]
