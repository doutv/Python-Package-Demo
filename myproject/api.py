# api.py
from myproject.utils.common import prepare_init_data, get_rule, parse_data_by_rule
import click


@click.group()
def cli():
    prepare_init_data()


@cli.command()
@click.argument('data')
@click.option('--schema', default="无")
def parse(data, schema):
    print(f"parsing {data} in {schema}")
    print(f"result is {parse_data_by_rule(data)}")


@cli.command()
def rule():
    print(get_rule())
