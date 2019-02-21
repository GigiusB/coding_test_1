# GBronzini Coding test

This is the requested coding test.

[Installation](#Installing-runtime) will define a new shell command `news_search`.

You can use `news_search` without arguments to get some help or `news_search --help` for additional help.

An example datafile is provided in [data/hscic-news](data/hscic-news)

No library was used for implementing the search algorithm.

The following libraries have been used:
- [Click](https://click.palletsprojects.com/en/7.x/) for enhancing the user experience
wih the command line
- [Pytest](https://docs.pytest.org/en/latest/) for unit testing the command line utility

## Example usage

Help: 

```bash
$ news_search --help
Usage: news_search [OPTIONS] QUERY [[AND|OR]]

  Will search the database. If operator is == OR (default) then entries must
  match at least one of the terms provided in the QUERY parameter. If
  operator is == OR then entries must match all of the terms provided in the
  QUERY parameter.

Options:
  --datafile FILENAME
  --help               Show this message and exit.
```

Example commands:
```bash
$ news_search "which while" AND
7

$ news_search "which while" OR
2,3,7,9

```

## Search algorithm

The query string is first purged from any punctuation and then converted to a set of 
lowercase words.
The Python set will ensure duplicate words are discarded.

For each document in the datafile we will then first get a set of words by applying the 
same word extraction algorithm as for the query parameter. The resulting set is compared
to the query set using the following operators:
- `set.issubset` if the operator request parameter was AND
- `set.intersection` if the operator request parameter was OR

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
