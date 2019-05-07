Brief.me PyPI server
====================

This is the PyPI server of Brief.me

## How to use ?
Let's take the django app `marketing-blocks` as example.   
In order to add the release `0.1` of `marketing-blocks` to one of your existing project, 
you need to add the following to your `requirements.py`:
```shell
--extra-index-url https://briefmnews.github.io/python-package-server/
marketing-blocks==0.1
...
```
**Caution**: the release number needs to be set in the `setup.py` file located in 
[marketing-blocks](https://github.com/briefmnews/marketing-blocks/blob/0.1/setup.py)
as version number.  
Here is an example for the release `0.1`:
```python
from setuptools import setup

setup(
    name='marketing-blocks',
    version='0.1',
    ...,
)
```