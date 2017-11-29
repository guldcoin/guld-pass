from guldpass import __version__
from setuptools import setup, find_packages

# REQUIREMENTS = [line.strip() for line in open("requirements.txt").readlines()]

setup(name='guld-pass',
      version=__version__,
      platforms='linux',
      description='Very thin python3 client for pass (the standard unix password manager).',
      author='isysd',
      author_email='public@iramiller.com',
      license='MIT',
      url='https://pass.guld.io/',
      py_modules=['guldpass'],
      packages=find_packages(exclude=['tests', 'tests.*']),
      entry_points={'console_scripts': ['guld-pass = guldpass:main']},
      zip_safe=False,
      include_package_data=True,
      # install_requires=REQUIREMENTS,
      classifiers=[
          'Topic :: System :: Administration',
          'Development Status :: 4 - Beta',
          'Intended Audience :: End Users/Desktop',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: MIT License',
          'Operating System :: POSIX',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Topic :: Administration',
          'Topic :: Security',
          'Topic :: Utilities'
])
