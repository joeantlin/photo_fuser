from django import forms
from apps.log_app.models import User
from .models import Photo, Comment

# def myid(request):
#     id = request.session["id"]
#     return id

class UploadPhoto(forms.Form):
    photo1 = forms.ImageField()
    photo2 = forms.ImageField()

class CombinePhoto(forms.Form):
    title       = forms.CharField()
    description = forms.CharField(
                        required    = False,
                        widget      = forms.Textarea(
                            attrs={
                                "rows": 10,
                                "cols": 20
                            }
                        )
                    )
    # creator     = forms.ModelChoiceField(
    #                     queryset=User.objects.all(),
    #                     widget  = forms.TextInput(
    #                         attrs   = {
    #                             # "type": "hidden"
    #                             # "value":
    #                         }
    #                     )
    #                 )

