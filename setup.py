from setuptools import setup

import re

with open('color_palette/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

print(version)

requirements = []
try:
    with open('requirements.txt') as f:
        requirements = f.read().splitlines()
except FileNotFoundError:
    pass

with open("docs/README.md", "r") as f:
    readme = f.read()

setup(name="color_palette",
      packages=["color_palette"],
      author="SnowballSH, one-wq, 12944qwerty",
      version=version,
      description="A color palette module",
      long_description=readme,
      long_description_content_type="text/markdown",
      install_requires=requirements,
      python_requires=">=3.6",
      url="https://github.com/SnowballSH/ColorPalette",
      download_url="https://github.com/SnowballSH/ColorPalette/archive/v0.2.6.1.tar.gz",
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: MIT License",
          "Natural Language :: English",
          "Operating System :: OS Independent",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
          "Programming Language :: Python :: 3.8",
          "Topic :: Artistic Software"
        ],)
