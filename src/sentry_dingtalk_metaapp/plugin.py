# !/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests
import sentry_dingtalk_metaapp
from .forms import DingTalkOptionsForm
from sentry.plugins.bases.notify import NotificationPlugin

DING_TALK_API = 'https://oapi.dingtalk.com/robot/send?access_token={token}'


class DingTalkPlugin(NotificationPlugin):
    author = 'Linchengzzz'
    author_url = 'https://github.com/linchengzzz/sentry-dingtalk-metaapp'
    description = 'sentry extension which can send error to ding-talk'
    resource_links = [
        ('Source', 'https://github.com/linchengzzz/sentry-dingtalk-metaapp'),
        ('Bug Tracker', 'https://github.com/linchengzzz/sentry-dingtalk-metaapp/issues'),
        ('README', 'https://github.com/linchengzzz/sentry-dingtalk-metaapp/blob/master/README.md'),
    ]
    version = sentry_dingtalk_metaapp.VERSION

    slug = 'DingTalk:Robot'
    title = 'DingTalk:Robot'
    conf_key = slug
    conf_title = title
    project_conf_form = DingTalkOptionsForm

    def is_configured(self, project):
        return bool(self.get_option('access_token', project))

    def notify_users(self, group, event, *args, **kwargs):
        if not self.is_configured(group.project):
            self.logger.info('ding-talk token config error')
            return None

        if self.should_notify(group, event):
            self.logger.info('send msg to ding-talk robot yes')
            self.send_msg(group, event, *args, **kwargs)
        else:
            self.logger.info('send msg to ding-talk robot no')
            return None

    def send_msg(self, group, event, *args, **kwargs):
        del args, kwargs

        error_title = u'Sentry: 检测到来自【%s】的异常' % event.project.slug
        user_phone = self.get_option('phone', group.project)

        data = {
            "msgtype": 'markdown',
            "markdown": {
                "title": error_title,
                "text": u'### {title} \n\n > {message} \n\n [更多详细信息]({url}) \n\n @{phone}'.format(
                    title=error_title,
                    message=group.message,
                    url=u'{url}events/{id}/'.format(
                        url=group.get_absolute_url(),
                        id=event.event_id if hasattr(event, 'event_id') else event.id
                    ),
                    phone=user_phone
                )
            },
            "at": {
                "atMobiles": [user_phone],
                "isAtAll": False
            }
        }

        requests.post(
            url=DING_TALK_API.format(token=self.get_option('access_token', group.project)),
            headers={
                'Content-Type': 'application/json'
            },
            data=json.dumps(data).encode('utf-8')
        )
