import pip
import json
from bson import Binary, Code
from bson.json_util import dumps

print dumps([{u'claims': {u'ApiUpdate': True, u'WebService': True}}])
print json.dumps(['foo', {'bar':('baz', None, 1.0, 2)}])

installed_packages = pip.get_installed_distributions()
installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
     for i in installed_packages])
print(installed_packages_list)
