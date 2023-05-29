from django.db import models

class BinaryTreeNode(models.Model):
    id = models.IntegerField(primary_key=True)
    parent_id = models.IntegerField(blank=True, null=True)
    left = models.BooleanField(default=False)
    right = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.id)
