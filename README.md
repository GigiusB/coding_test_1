# GBronzini Coding test

This is the requested coding test.

[Installation](#Installing-runtime) will define a new shell command `news_search`.

You can use `news_search` without arguments to get some help or `news_search --help` for additional help.



### Prerequisites

This projects has been developed and tested using Python 3.6


```
Give examples
```

### Installing runtime

This Python project uses the standard setuptools.

You can generate the source distribution using the following command:

`python setup.py sdist`

The above command will generate a file called *nhs_code_test-X.Y.Z.tar.gz* int the *dist* folder

You can install the command line utility provided by this project:

- either from the source code `pip install .` if you want to modify the code and test the changes
- or from the source distribution: `pip install dist/nhs_code_test-X.Y.Z.tar.gz`

A [Pipfile](https://pipenv.readthedocs.io/en/latest/) file is also provided should you wish to use it.

### Installing dev environment

If using pip: `pip install -r requirements.txt`

If using pipenv:
```
pipenv install
pipenv install -d
```

## Running the tests

Tests can be executed launching `pytest`. 

Make sure you have installed properly your [dev environment](#Installing-dev-environment)

More info on pytest is available [here](https://docs.pytest.org/en/latest/) 

## Authors

* **Giovanni Bronzini** - [Linkedin profile](https://www.linkedin.com/in/giovannibronzini/)


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
