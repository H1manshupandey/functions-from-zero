
import click
from mylib.bot import scrape



@click.command()
@click.option("--name", help="Web page we want to scrape")



def cli(name = "Microsoft"):
    results = scrape(name)
    click.echo(click.style(f"{results}", bg = "blue", fg = "green"))


if __name__ == "__main__":
    cli()


