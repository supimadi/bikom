from django.db import models
from django.utils.translation import ugettext_lazy as _

from users.models import CustomUser


FULL_NAME = models.CharField(_('Full Name'), max_length=100)

class BestFriendsModel(models.Model):
    friend = models.ManyToManyField(CustomUser)
    full_name = FULL_NAME
    phone_number = models.CharField(_('Phone Number'), max_length=15, unique=True)

    def __str__(self):
        return self.full_name

class AppointmentSchedule(models.Model):
    teacher = models.ForeignKey(
        CustomUser,
        on_delete=models.DO_NOTHING,
        related_name="staff_teacher",
        limit_choices_to={'is_staff': True},
        null=True,
    )
    student = models.ForeignKey(
        CustomUser,
        on_delete=models.DO_NOTHING
    )
    approved = models.BooleanField(
        _("Approval"),
        null=True,
    )
    date = models.DateField(
        _("Appointment date"),
        help_text=_("Enter what date for when you want meet the teacher."),
    )
    time = models.TimeField(
        _("Appointment time at"),
        help_text=_("Enter what time for when you want meet the teacher."),
    )
    desc = models.TextField(
        verbose_name=_("Description"),
        help_text=_("Describe why you make an appointment."),
        null=True,
    )

    def __str__(self):
        return f"{self.student} appointment"

class StudentProfile(models.Model):
    account = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True)
    instagram = models.CharField(
        _('Instagram Account'), max_length=35,
        help_text=_("Enter your instagram username with the @, i.e: @ziyk123.")
    )
    chield_number = models.CharField(
        _('Chield Number'), max_length=2,
    )
    number_of_sibling = models.CharField(
        _('Number of sibling(s).'), max_length=2,
    )
    # klass == class
    klass = models.CharField(
        _('Class'), max_length=13,
        help_text=_('Enter your class name, i.e: XII TJAT-2. MUST write as example.')
    )

    def __str__(self):
        return f"{self.account} profile"

class FatherStudentModels(models.Model):
    father_full_name = models.CharField(_('Full Name'), max_length=100)
    father_jobs = models.CharField(_('Jobs'), max_length=100)
    child = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.father_full_name

class MotherStudentModels(models.Model):
    mother_full_name = models.CharField(_('Full Name'), max_length=100)
    mother_jobs = models.CharField(_('Jobs'), max_length=100)
    child = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.mother_full_name
