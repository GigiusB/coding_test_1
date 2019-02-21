import click
from nhs.searchengine import search


@click.command()
@click.argument('query')
@click.argument('-operator', type=click.Choice(['AND', 'OR']), default='OR')
@click.option('--datafile', default="./data/hscic-news", type=click.File())
def cli(query, _operator, datafile=None):
    """Will search the database.
    If operator is == OR (default) then entries must match at least one of the terms provided in the QUERY parameter.
    If operator is == OR then entries must match all of the terms provided in the QUERY parameter."""

    # Formatting results
    results = ','.join(search(datafile, query, _operator))

    # returing results
    click.echo(results)


def main():  # pragma: no cover
    cli()
