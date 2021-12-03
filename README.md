Brief.me PyPI server
====================

This is the PyPI server of Brief.me

## How to add a new release with the make command?
You can use the following make command to create a new app release:
```bash
make bump app=marketing-blocks version=0.1
```

## How to add a new release without the make command?
Adding a new release for an existing app is a 4 steps process.

### 1. Update the version number in the setup.py
Here is an example for the release `0.1` for the marketing-blocks app:
```python
from setuptools import setup

setup(
    name='marketing-blocks',
    version='0.1',
    ...,
)
```

### 2. Create a new release

### 3. Add the new release to python-package-server
When the release is published you can add it the `python-package-sever` app.
Here is an example for the release `0.1` of the marketing-blocks app:
```html
<!-- marketing-blocks/index.html --> 
<!DOCTYPE html>
<html>
  <head>
    <title>Marketing Blocks</title>
  </head>
  <body>
    <a href="git+https://github.com/briefmnews/marketing-blocks.git@0.1#egg=marketing_blocks-0.1">
      marketing-blocks-0.1
    </a>
    <br/>
    <a href="git+https://github.com/briefmnews/marketing-blocks.git@0.0.1#egg=marketing_blocks-0.0.1">
      marketing-blocks-0.0.1
    </a>
    <br/>
  </body>
</html>
```

### 4. Commit your changes
Here is an example of commit:
```shell
git commit -m "feat(marketing-blocks): release version 0.1"
```
Our private PyPI server is hosted by github pages.
The deployment process might take up to 5 minutes.

## How to use?
Let's take the django app `marketing-blocks` as example.   
In order to add the release `0.1` of `marketing-blocks` to one of your existing project, 
you need to add the following to your `requirements.py`:
```shell
--extra-index-url https://briefmnews.github.io/python-package-server/
marketing-blocks==0.1

Django==2.2.24
...
```

In this situation, pip will try to find indexes from https://briefmnews.github.io/python-package-server/ before the official PyPI server.
