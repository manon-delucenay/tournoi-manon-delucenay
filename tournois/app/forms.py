from django.forms import ModelForm, Textarea
from django.utils.translation import gettext_lazy as _
from .models import Comments


class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ["content"]
        widgets = {
            "content": Textarea(attrs={"cols": 80, "rows": 3}),
        }
