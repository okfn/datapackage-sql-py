# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

import sys
from pprint import pprint

sys.path.insert(0, '.')
from examples.base import run


# Fixtures
url = 'sqlite:///:memory:'
prefix = 'registry_'
source = 'examples/packages/registry/datapackage.json'
target = 'tmp/packages/registry/datapackage.json'


# Execution
if __name__ == '__main__':
    run(url, prefix, source, target)
