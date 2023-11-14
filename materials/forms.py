from django import forms

from materials.models import Material
from catalog.forms import MixinForm


class BlogForm(MixinForm, forms.ModelForm):
    class Meta:
        model = Material
        fields = ('title', 'text', 'image', 'to_publish')