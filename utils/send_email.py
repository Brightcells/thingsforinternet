# -*- coding: utf-8 -*-

from marrow.mailer import Mailer, Message


class SendEmail(object):
    def __init__(self, username='', password='', use='smtp', host='smtp.exmail.qq.com', port='25'):
        self.username = username
        self.mailer = Mailer({
            'transport': {
                'use': use,
                'host': host,
                'port': port,
                'username': username,
                'password': password
            }, 'manager': {}
        })

    def send_email(self, to, subject, content, author=''):
        self.mailer.start()
        self.mailer.send(Message(author=author or self.username, to=to, subject=subject, plain=content))
        self.mailer.stop()
