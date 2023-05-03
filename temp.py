import site
print(site.getsitepackages())

import pkg_resources
print(pkg_resources.get_distribution('linkedin_python'))