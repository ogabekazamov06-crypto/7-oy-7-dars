from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=200, verbose_name="Kurs nomi")
    description = models.TextField(verbose_name="Kurs haqida malumot")
    price = models.IntegerField(verbose_name="Kurs narxi")
    image = models.ImageField(upload_to="course_images/", blank=True,null=True, verbose_name="kurs rasmi")

    class Meta:
        verbose_name ="Kurs"
        verbose_name_plural = "Kurslar"
        ordering = ['title']

    def __str__(self):
        return self.title

class Student(models.Model):
    name = models.CharField(max_length=100, verbose_name="Talaba ismi-fimiliyasi")
    email = models.EmailField(verbose_name="Talaba email manzili")
    phone = models.CharField(max_length=20, verbose_name="telfon raqami")
    address = models.CharField(max_length=200, verbose_name="Yashash manzili")
    courses = models.ManyToManyField(Course, related_name='students', verbose_name="yozilgan kurslar")

    liked_courses = models.ManyToManyField(Course, related_name="likes", blank=True,
                                           verbose_name="Yoqtirgan kurslari")
    class Meta:
        verbose_name = "Talaba"
        verbose_name_plural = "Talabalar"
        ordering = ['-id']


    def __str__(self):
        return self.name