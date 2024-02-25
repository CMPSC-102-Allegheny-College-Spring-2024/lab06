"""Define the command-line interface for the datasummarizer program."""

from pathlib import Path

import typer

from dataanalysis import summarize
from dataanalysis import transform

from rich.console import Console

cli = typer.Typer()

console = Console()


@cli.command()
def main(
    data_file: Path = typer.Option(...),
):
    """Summarize the data values stored in a file."""
    # display details about the file provided on the command line
    data_text = ""
    # --> the file was not specified so we cannot continue using program
    if data_file is None:
        console.print("No data file specified!")
        raise typer.Abort()
    # --> the file was specified and it is valid so we should read and check it
    if data_file.is_file():
        data_text = data_file.read_text()
        data_line_count = len(data_text.splitlines())
        console.print("")
        console.print(
            f":package: The data file contains {data_line_count} data values in it!"
        )
        console.print("")
        console.print(":rocket: Let's do some sophisticated data analysis!")
        # transform the data from a list of textual values to a list of numerical values
        data_list = transform.transform_string_to_number_list(data_text)
        # TODO: compute the mean from the list of numerical values
        console.print("")
        console.print(":abacus: Here are the results of the data analysis:")
        # TODO: display the computed mean in the terminal window
        # TODO: compute the median from the list of numerical values
        # TODO: display the computed median in the terminal window
        # TODO: compute the variance from the list of numerical values
        # TODO: display the computed variance in the terminal window
        # TODO: compute the standard deviation from the list of numerical values
        # TODO: display the computed standard deviation in the terminal window
        # TODO: make sure that you display all floating-point numbers with
        # exactly two decimal places (see the expected output for details)
        console.print("")
        console.print(
            ":light_bulb: What does this tell you about the population of this county?"
        )
        console.print("")
    # --> the file was specified but it does not exist so we cannot continue using program
    elif not data_file.exists():
        console.print(":bomb: The data file does not exist!")
        console.print("Did you incorrectly specify the name of the file?")
