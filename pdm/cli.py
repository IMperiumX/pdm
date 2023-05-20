"""Console script for pdm."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for pdm."""
    click.echo("Replace this message by putting your code into "
               "pdm.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
