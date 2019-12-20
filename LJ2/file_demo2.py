#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
j = '''{"name":"小明","sex":"不详"}'''
a = json.loads(j)
a["sex"]="男"
print(a)





