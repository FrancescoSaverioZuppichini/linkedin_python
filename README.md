# LinkedIn Python 💙🐍
This package allows you to easily create post on LinkedIn using python, it follow LinkedIn v2 APIs.

The official LinkedIn doc is [here](https://learn.microsoft.com/en-gb/linkedin/consumer/integrations/self-serve/share-on-linkedin)

## Installation

You can install the package using pip

```
pip install linked_pythoon
```

## Getting Started

### Obtain a token

You need to obtain a token, is not an easy process since you need to create a LinkedIn app, please follow this [youtube tutorial](https://youtu.be/YJoof1kX_kQ)

Then, run 

```bash
export LINKEDIN_TOKEN=<YOUR_TOKEN>
```

in your current shell

### Creating a Post
To create a post, you can simple use the `User` class.

```python
from linkedin_python import User

user = User()
res = user.create_post(
    "Post content",
    images=[
        ("/home/zuppif/Documents/LinkedInGPT/grogu.jpg", "image description"),
        ("/home/zuppif/Documents/LinkedInGPT/grogu_2.png", "image description"),
    ],
)
```

This will create a post with two images.

## Contribution

We welcome all the contributions, here some dev specific stuff. To contribute

```bash
git clone git@github.com:FrancescoSaverioZuppichini/linkedin_python.git
cd linkedin_python && pip install -e ".[dev]"
```

This will install of the dev packages, e.g. `black` and `isort`

### Code Quality 🧹

We provide two handy commands inside the `Makefile`, namely:

- `make style` to format the code
- `make check_code_quality` to check code quality (PEP8 basically)

So far, **there is no types checking with mypy**.

### Tests 🧪

[`pytests`](https://docs.pytest.org/en/7.1.x/) is used to run our tests.

### Publish on PyPi 🚀

**Important**: Before publishing, edit `__version__` in [src/__init__](/src/__init__.py) to match the wanted new version.

We use [`twine`](https://twine.readthedocs.io/en/stable/) to make our life easier. You can publish by using

```
export PYPI_USERNAME="you_username"
export PYPI_PASSWORD="your_password"
export PYPI_TEST_PASSWORD="your_password_for_test_pypi"
make publish -e PYPI_USERNAME=$PYPI_USERNAME -e PYPI_PASSWORD=$PYPI_PASSWORD -e PYPI_TEST_PASSWORD=$PYPI_TEST_PASSWORD
```

You can also use token for auth, see [pypi doc](https://pypi.org/help/#apitoken). In that case,

```
export PYPI_USERNAME="__token__"
export PYPI_PASSWORD="your_token"
export PYPI_TEST_PASSWORD="your_token_for_test_pypi"
make publish -e PYPI_USERNAME=$PYPI_USERNAME -e PYPI_PASSWORD=$PYPI_PASSWORD -e PYPI_TEST_PASSWORD=$PYPI_TEST_PASSWORD
```

**Note**: We will try to push to [test pypi](https://test.pypi.org/) before pushing to pypi, to assert everything will work

### CI/CD 🤖

We use [GitHub actions](https://github.com/features/actions) to automatically run tests and check code quality when a new PR is done on `main`.

On any pull request, we will check the code quality and tests.

When a new release is created, we will try to push the new code to PyPi. We use [`twine`](https://twine.readthedocs.io/en/stable/) to make our life easier. 

The **correct steps** to create a new realease are the following:
- edit `__version__` in [src/__init__](/src/__init__.py) to match the wanted new version.
- create a new [`tag`](https://git-scm.com/docs/git-tag) with the release name, e.g. `git tag v0.0.1 && git push origin v0.0.1` or from the GitHub UI.
- create a new release from GitHub UI

The CI will run when you create the new release.
