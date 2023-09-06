
from __future__ import absolute_import, division, print_function
__metaclass__ = type

import xml.etree.cElementTree as xml

from ansible.module_utils.urls import open_url
from ansible.module_utils.common.text.converters import to_native, to_text

def sophos_firewall_argument_spec():
    """
    Returns the argument_spec of options common to sophos_firewall_* modules
    :return: argument_spec
    """
    return dict(
        auth_username = dict(type = 'str', aliases = ['username'], mandatory = True),
        auth_password = dict(type = 'str', aliases = ['password'], mandatory = True)
    )

class SophosFirewallError(Exception):
    pass