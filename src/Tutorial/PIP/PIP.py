# PIP is a package manager for Python packages, or modules if you like.

# A package contains all the files you need for a module.

# Modules are Python code libraries you can include in your project.

# you can download a package with this:   =>     pip install pachage_name
# example of using and installing a package:

# pip install camelcase
import camelcase

c = camelcase.CamelCase()

txt = 'hellp world'

print(c.hump(txt))


# how to uninstall package:
# pip uninstall package_name
# and then it will ask for a confirmation from you

# list packages:
# pip list