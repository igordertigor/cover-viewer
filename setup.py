import sys
import os
import re
import subprocess
from setuptools import setup


def link_gi():
    origin = '/usr/lib/python3/dist-packages/gi'
    pyex = sys.executable
    venvpath = re.search(r'(.*)/bin/python', pyex).group(1)
    name = os.path.join(venvpath,
                        'lib/python3.{}/site-packages/gi'
                        .format(sys.version_info.minor))
    if not os.path.exists(name):
        cmd = ['ln', '-s', origin, name]
        subprocess.run(cmd)


if __name__ == '__main__':
    link_gi()

    setup(
        name='cmus-cover',
        version='0.1',
        scripts=['cmus-cover-server', 'cmus-cover-set'],
        install_requires=[
            'bottle',
            'pywebview',
            'requests',
            'docopt',
            'jinja2'],
    )
