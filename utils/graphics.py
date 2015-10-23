# -*- coding: utf-8 -*-

from django.conf import settings

import shortuuid
import subprocess

from cStringIO import StringIO
try:
    from PIL import Image
except ImportError:
    import Image


def compression(data):
    im = Image.open(StringIO(data))
    fmt = im.format.lower()
    if fmt in ['png', 'jpg', 'jpeg']:
        out = StringIO()
        if fmt in ['png', ]:
            im_name = shortuuid.uuid()
            im.save(settings.BEFORE_QUANT.format(im_name))
            subprocess.call(settings.QUANT_CMD.format(im_name), shell=True)  # 阻塞
            try:
                # Refer: http://pngquant.org/
                # Instructs pngquant to use the least amount of colors required to meet or exceed the max quality.
                # If conversion results in quality below the min quality the image won't be saved.
                im = Image.open(settings.AFTER_QUANT.format(im_name))
                im.save(out, format=fmt)
            except IOError:
                return data
        else:
            im.save(out, format=fmt, optimize=True, quality=75)
        data = out.getvalue()
    return data


def thumbnail(data, size):
    im = Image.open(StringIO(data))
    fmt = im.format.lower()
    im = im.resize(size, Image.ANTIALIAS)
    out = StringIO()
    im.save(out, format=fmt, optimize=True, quality=75)
    return out.getvalue()
