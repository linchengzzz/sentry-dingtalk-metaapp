# !/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms


class DingTalkOptionsForm(forms.Form):
    access_token = forms.CharField(
        max_length=255,
        help_text='DingTalk webhook cccess_Token'
    )
    phone = forms.CharField(
        max_length=255,
        help_text='DingTalk Phone number'
    )
