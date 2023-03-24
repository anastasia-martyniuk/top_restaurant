from django.db import models

TYPE = [("K", "kitchen"), ("C", "client")]


class Printer(models.Model):
    name = models.CharField(max_length=64, help_text="printer name")
    api_key = models.CharField(max_length=64, unique=True, help_text="API access key")
    check_type = models.CharField(max_length=7, choices=TYPE, help_text="the type of check that the printer prints")
    point_id = models.IntegerField(help_text="the point to which the printer is bound")

    def __str__(self):
        return self.name


class Check(models.Model):
    STATUS = [("N", "new"), ("R", "rendered"), ("P", "printed")]

    printer = models.ForeignKey(Printer, on_delete=models.CASCADE, help_text="printer")
    type = models.CharField(max_length=64, choices=TYPE, help_text="check type")
    order = models.JSONField(help_text="order information")
    status = models.CharField(max_length=64, choices=STATUS, help_text="check status")
    pdf_file = models.FileField(help_text="a link to the generated PDF file")

    def __str__(self):
        return self.pdf_file
