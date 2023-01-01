from django.db import models
from datetime import datetime, timezone
from ia import settings
import shortuuid
from account.models import profanity_filter
from django.core.exceptions import ObjectDoesNotExist
from PIL import Image
from urllib.parse import urlparse
from django.core.exceptions import ValidationError

YEAR = datetime.now().year
MONTH = datetime.now().month
DAY = datetime.now().day

LINK_LIST = '/Users/parad/IES/CS/IA/media/link_list.txt'

def safe_website(url):
    with open(LINK_LIST, 'r') as f:
        link = urlparse(url)
        if link.scheme != 'https':
            raise ValidationError("Website doesn't come from a secure source")
        for line in f:
            if link.netloc in line:
                return(url)
    raise ValidationError("Sorry, you cannot enter a link from this website 🙁")


class Category(models.Model):
    name = models.CharField(max_length=25)
    icon = models.CharField(max_length=25, default=' ')
    
    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']
        
    def __str__(self):
        return self.name
    
# new class subcategory many to one to category 

def addZero(number):
    return str(number).zfill(2)

SHORT_UUID = shortuuid.ShortUUID().random(length=10)

LOOKING_FOR_HELP = "I'm looking for help"
OFFERING_HELP = "I'm offering help"

POST_TYPES = (
    ("need", LOOKING_FOR_HELP),
    ("offer", OFFERING_HELP),
)

class Post(models.Model):
    id = models.CharField(max_length=10, primary_key=True, unique=True, editable=True, default=SHORT_UUID)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=25, validators=[profanity_filter], unique=True)
    text = models.CharField(max_length=500, validators=[profanity_filter]) 
    date_created = models.DateTimeField(auto_created=True, auto_now_add=True, editable=False)
    date_updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='posts/{}/{}/{}'.format(str(YEAR), addZero(MONTH), addZero(DAY)), null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    rating = models.PositiveSmallIntegerField(default=10)
    visible = models.BooleanField(default=True)
    area = models.CharField(max_length=50, default='Cała Polska')
    type = models.CharField(max_length=20, choices=POST_TYPES, default=LOOKING_FOR_HELP, blank=False, null=False)

    class Meta:
        ordering = ['-rating', '-date_created']
        
    def __str__(self):
        return self.title

    # def save(self, *args, **kwargs):
    #     img = Post.open(self.image.path)
    #     if img.height > 400 or img.width > 400:
    #         new_img = (400, 400)
    #         img.thumbnail(new_img)
    #         img.save(self.image.path)
    #     super().save(*args, **kwargs)
        
    
    @property
    def time_since(self):
        value = self.date_created
        delta = datetime.now(timezone.utc)-value
        if delta.days < 1:
            return str('today at {}'.format(value.strftime('%H:%M')))
        elif delta.days < 2:
            return str('yesterday at {}'.format(value.strftime('%H:%M')))
        else:
            return str(value.strftime('%d/%m/%Y'))
    
class PolandCities(models.Model):
    name = models.CharField(max_length=100)
    voivodeship = models.CharField(max_length=100)
    population = models.BigIntegerField()
    
    class Meta:
        verbose_name_plural = "Poland Cities"

    def __str__(self):
        return self.name
    