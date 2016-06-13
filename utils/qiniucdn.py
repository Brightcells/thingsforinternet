# -*- coding: utf-8 -*-

import pngquant
import qiniu
from django.conf import settings


QINIU = settings.QINIU
auth = qiniu.Auth(QINIU['access_key'], QINIU['secret_key'])
pngquant.config(settings.PNG_QUANT_FILE)


def upload(data, compress=True, key=None, mime_type='application/octet-stream', bucket=QINIU['bucket']):
    data = pngquant.quant_data(data)[1] if compress else data
    token = auth.upload_token(bucket, key=key)
    ret, _ = qiniu.put_data(token, key, data, mime_type=mime_type)
    return ret


def upload_with_file(f, bucket=QINIU['bucket']):
    ret = upload(f['body'], mime_type=f['content_type'], bucket=bucket)
    return ret and ret.get('key')


def qiniu_file_url(key):
    return key and (u'{}{}'.format(QINIU['domain'], key) if not key.startswith('http') else key)


def qiniu_file_url_https(key):
    return key and (u'{}{}'.format(QINIU['domain_https'], key) if not key.startswith('http') else key.replace(QINIU['domain'], QINIU['domain_https']))
