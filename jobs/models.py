from django.db import models

# Create your models here.
# نسوي بايثون كلاس 
class Job(models.Model):
    # بالرسمه اللي رسمناها نبي فيها صوره
    #كل فيلد نشوف الخصائص حقتها بالدوكيمنتش 
    # ااب لود تو نخليه يروح فولدر الايميجز وياخذ الصوره 
    image = models.ImageField(upload_to='images/')
    # نحتاج شرح للصورة اللي حطينها 
    summary = models.CharField(max_length=200)
    