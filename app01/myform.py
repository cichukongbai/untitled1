
from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets
from app01 import models

class RegForm(forms.Form):
    username=forms.CharField(max_length=8,min_length=3,label='用户名',
                             error_messages={'max_length':'用户名过长','min_length':'用户名太短了','required':'该项必填'},
                            widget=widgets.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(max_length=8, min_length=3, label='密码',
                               error_messages={'max_length': '密码过长', 'min_length': '密码太短了', 'required': '该项必填'},
                               widget=widgets.PasswordInput(attrs={'class': 'form-control'}))
    # re_password = forms.CharField(max_length=8, min_length=3, label='确认密码',
    #                            error_messages={'max_length': '确认密码过长', 'min_length': '确认密码太短了', 'required': '该项必填'},
    #                            widget=widgets.PasswordInput(attrs={'class': 'form-control'}))
    # email=forms.EmailField(error_messages={'required':'该项必填','invalid':'格式错误'},
    #                        widget=widgets.EmailInput(attrs={'class': 'form-control'}))

    # 局部校验username字段
    def clean_username(self):
        name=self.cleaned_data.get('username')
        user=models.UserInfo.objects.filter(username=name).first()
        if user:
            raise ValidationError('该用户已存在')
        else:
            return name
    # # 全局校验密码
    # def clean(self):
    #     pwd=self.cleaned_data.get('password')
    #     re_pwd=self.cleaned_data.get('re_password')
    #     if not pwd == re_pwd:
    #         raise ValidationError('两次密码不一致')
    #     else:
    #         return self.cleaned_data