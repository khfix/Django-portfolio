from django.db import models
class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    logo = models.FileField(upload_to='logos/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    video = models.FileField(upload_to='videos/',null=True, blank=True)
    def __str__(self):	
	    return self.name
    class Meta:
        ordering = ['-updated']

class Photo(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='photos')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.FileField(upload_to='photos/')
    class Meta:
        ordering = ['-updated']
    
class programmingLang(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='programmingLangs')
    name = models.CharField(max_length=20)
    logo = models.FileField(upload_to='logos/')
    def __str__(self):
        return self.project.name + " - " + self.name
    
class Link(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='links')
    name = models.CharField(max_length=20)
    url = models.CharField(max_length=100)
    icon = models.FileField(upload_to='icons/')
    def __str__(self):
        return self.project.name + " - " + self.name

class Hashtag(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='hashtags')
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class Code(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='codes')
    function_name = models.CharField(max_length=50)
    code = models.TextField()
    def __str__(self):
        return self.project.name + " - " + self.function_name
    
    