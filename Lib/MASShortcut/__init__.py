'''
Python mapping for the MASShortcut framework.

This module does not contain docstrings for the wrapped code, see
<https://github.com/shpakovski/MASShortcut> for documentation.
'''

import objc
import sys
import os
import Foundation

import MASShortcut.constants
from MASShortcut import _metadata
from MASShortcut._inlines import _inline_list_


def _find_framework():
    name = 'MASShortcut.framework'
    home = os.path.expanduser('~')
    paths = [
        os.path.join(os.sep, 'Library', 'Frameworks', name),
        os.path.join(home, 'Library', 'Frameworks', name),
        os.path.join(os.sep, 'System', 'Library', 'Frameworks', name),
    ]
    try:
        paths.append(
            os.path.join(
                Foundation.NSBundle.mainBundle().privateFrameworksPath(),
                name
            )
        )
    except Exception:
        pass
    for path in paths:
        if os.path.exists(path):
            return path
    return os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "MASShortcut.framework"
    )


sys.modules['MASShortcut'] = mod = objc.ObjCLazyModule(
    "MASShortcut",
    "com.github.shpakovski.MASShortcut",
    _find_framework(),
    _metadata.__dict__, _inline_list_, {
        '__doc__': __doc__,
        'objc': objc,
        '__path__': __path__,
        '__loader__': globals().get('__loader__', None),
    }, (Foundation,))

import sys
del sys.modules['MASShortcut._metadata']
