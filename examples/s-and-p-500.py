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
prefix = 's-and-p-500_'
source = 'examples/packages/s-and-p-500/datapackage.json'
target = 'tmp/packages/s-and-p-500/datapackage.json'


# Execution
if __name__ == '__main__':
    run(url, prefix, source, target)
