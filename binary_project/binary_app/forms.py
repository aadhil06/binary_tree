from django import forms
from .models import BinaryTreeNode

class BinaryTreeNodeForm(forms.ModelForm):
    class Meta:
        model = BinaryTreeNode
        fields = ['id', 'parent_id', 'left', 'right']
