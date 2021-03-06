from setuptools import setup, find_packages

version = '1.0.4'

long_description = (
    open('README.txt').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')

setup(name='osha.hwc2014',
      version=version,
      description="Policy product for OSHA HWC 2014",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='',
      author_email='',
      url='http://svn.plone.org/svn/collective/',
      license='gpl',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['osha', ],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Products.LoginLockout',
          'Products.PasswordStrength',
          'collective.multilingualtools',
          'collective.quickupload',
          'plone.app.contenttypes',
          'plone.app.event [dexterity]',
          'plone.app.theming',
          'plonetheme.sunburst',
          'osha.hwccontent',
          'osha.hwctheme',
          'slc.xliff',
          'webcouturier.dropdownmenu',
      ],
      extras_require={'test': ['plone.app.testing']},
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
