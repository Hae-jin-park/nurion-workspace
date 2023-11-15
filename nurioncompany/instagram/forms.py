import re
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = [
      'message', 'photo', 'tag_set', 'is_public'
    ]

# # 영어 지우기 예제
#   def clean_message(self):
#     message = self.cleaned_data.get('message')
#     if message:
#       message = re.sub(r'[a-zA-Z]','',message)
#     return message