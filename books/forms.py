from django import forms
from .models import Post
from tinymce.widgets import TinyMCE

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'body', 'category', 'slug')
		
    class Media:
        js = ('/media/tinymce/jscripts/tiny_mce/tiny_mce.min.js',)		