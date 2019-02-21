from click.testing import CliRunner

from nhs.cli import cli


def test_news_positive_searches_or():
    runner = CliRunner()

    result = runner.invoke(cli, ['Care Quality Commission', 'OR'])
    assert result.exit_code == 0
    assert result.output == '0,1,2,3,4,5,6\n'

    result = runner.invoke(cli, ['September 2004', 'OR'])
    assert result.exit_code == 0
    assert result.output == '9\n'

    result = runner.invoke(cli, ['general population generally', 'OR'])
    assert result.exit_code == 0
    assert result.output == '6,8\n'


def test_default_or():
    runner = CliRunner()

    result = runner.invoke(cli, ['Care Quality Commission', 'OR'])
    assert result.exit_code == 0
    assert result.output == '0,1,2,3,4,5,6\n'


def test_news_positive_searches_and():
    runner = CliRunner()

    result = runner.invoke(cli, ['Care Quality Commission admission', 'AND'])
    assert result.exit_code == 0
    assert result.output == '1\n'

    result = runner.invoke(cli, ['general population Alzheimer', 'AND'])
    assert result.exit_code == 0
    assert result.output == '6\n'


def test_news_negative_searches():
    runner = CliRunner()

    result = runner.invoke(cli, ['Care Quality Commission admission DUMMY', 'AND'])
    assert result.exit_code == 0
    assert result.output == '\n'

    result = runner.invoke(cli, ['NONEXITENT DUMMY', 'OR'])
    assert result.exit_code == 0
    assert result.output == '\n'
