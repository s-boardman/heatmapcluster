# Copyright (c) 2015, Warren Weckesser.  All rights reserved.
# This software is licensed according to the "BSD 2-clause" license.

from __future__ import print_function

from distutils.core import setup


def get_heatmapcluster_version():
    """
    Find the value assigned to __version__ in heatmapcluster.py.

    This function assumes that there is a line of the form

        __version__ = "version-string"

    the file.  It returns the string version-string, or None if such a
    line is not found.
    """
    with open("heatmapcluster.py", "r") as f:
        for line in f:
            s = [w.strip() for w in line.split("=", 1)]
            if len(s) == 2 and s[0] == "__version__":
                return s[1][1:-1]


setup(name='heatmapcluster',
      version=get_heatmapcluster_version(),
      author="Warren Weckesser",
      description="Heatmap cluster dendrogram plotter.",
      license="BSD",
      classifiers=[
          "License :: OSI Approved :: BSD License",
          "Intended Audience :: Developers",
          "Operating System :: OS Independent",
          "Programming Language :: Python, Cython",
      ],
      py_modules=['heatmapcluster'],
      install_requires=[
          'numpy >= 1.6.0',
          'scipy',
          'matplotlib',
      ])
