from docapp import views
from django.urls import path

urlpatterns=[
    path("base", views.base, name="base"),
    path("", views.home, name="home"),
    path("doctorSignUp", views.doctorSignUp, name="doctorSignUp"),
    path("doctorLogIn", views.doctorLogIn, name="doctorLogIn"),
    path("patientSignUp", views.patientSignUp, name="patientSignUp"),
    path("patientLogIn", views.patientLogIn, name="patientLogIn"),
    path("logout_profile", views.logout_profile, name="logout_profile"),
    path("aboutus", views.aboutus, name="aboutus"),
    path("department", views.department, name="department"),
    path("appointment", views.appointment, name="appointment"),
    path("contact",views.contact, name="contact"),
    # path("singlepage", views.singlepage, name="singlepage"),
    path("profile", views.profile, name="profile"),
    path("profile/<int:id>", views.edit),
    # path("images", views.images, name="image"),
    # path("upload", views.upload_file, name="upload"),
    # path("cards", views.cards, name="cards"),
    # path("appoint", views.appoint, name="appoint"),
    path("myappointments", views.myappointments, name="myappointments"),
    path("myappointments/<int:id>", views.getappointments),
    path("consultation", views.consultation, name="consultation"),
    path("consultation/<int:id>", views.editconsultation),
    path("appoint/<int:id>", views.consultation),
    path("timing", views.timing, name="timing"),
    path("medicine", views.medicine, name="medicine"),
    path("rating", views.rating, name="rate"),
    path("rating/<int:id>", views.rating),
    path("search",views.searchdb, name="search"),
    path("search/<int:id>", views.analyzesearchdb),
    path("newsearch", views.newsearch, name="newsearch"),
]