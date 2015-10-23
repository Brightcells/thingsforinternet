# -*- coding: utf-8 -*-

from django.conf import settings

from utils.graphics_utils import compression

import qiniu


QINIU = settings.QINIU
auth = qiniu.Auth(QINIU['access_key'], QINIU['secret_key'])


def upload(data, compress=True, key=None, mime_type='application/octet-stream', bucket=QINIU['bucket']):
    data = compression(data) if compress else data
    token = auth.upload_token(bucket, key=key)
    ret, _ = qiniu.put_data(token, key, data, mime_type=mime_type)
    return ret


def upload_with_file(f, bucket=QINIU['bucket']):
    ret = upload(f['body'], mime_type=f['content_type'], bucket=bucket)
    return ret and ret.get('key')


def qiniu_file_url(key):
    return key and (u'{0}{1}'.format(QINIU['domain'], key) if not key.startswith('http') else key)


def qiniu_file_url_https(key):
    return key and (u'{0}{1}'.format(QINIU['domain_https'], key) if not key.startswith('http') else key.replace(QINIU['domain'], QINIU['domain_https']))
