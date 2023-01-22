from django.db import models

class Technology(models.Model):
    technology = models.CharField(max_length=30)

    def __str__(self):
        return self.technology

class Company(models.Model):
    choices_type_market = (
        ('M', "Markenting"),
        ('N', "Nutrição"),
        ('D', "Design")
    )
    # COLUMNS
    logo = models.ImageField(upload_to="logo_company", null=True)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    city = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    feature_company = models.TextField()
    type_market = models.CharField(max_length=3, choices=choices_type_market)
    technology = models.ManyToManyField(Technology)

    def __str__(self):
        return self.name

    def count_jobs(self):
        return Job.objects.filter(company__id = self.id).count()

class Job(models.Model):
    choices_experience = (
        ('J', 'Júnior'),
        ('P', 'Pleno'),
        ('S', 'Sênior')
    )

    choices_status = (
        ('I', 'Interesse'),
        ('C', 'Currículo enviado'),
        ('E', 'Entrevista'),
        ('D', 'Desafio técnico'),
        ('F', 'Finalizado')
    )

    email = models.EmailField(null=True)
    company = models.ForeignKey(Company, null=True ,on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=30)
    level_experience = models.CharField(max_length=2, choices=choices_experience)
    data_end = models.DateField()
    status = models.CharField(max_length=30, choices=choices_status)
    technology_mastered = models.ManyToManyField(Technology)
    technology_study = models.ManyToManyField(Technology, related_name='study')

    def __str__(self):
        return self.title