# Data Analysis

## Assigned: Monday, 26 Feb 2024

## Due: Monday, 4th March 2024

## Expiration Date: Monday 11 March 2024, 2:30pm

# Data Analysis

## Project Goals

This engineering effort invites you to extend your knowledge about the basics of data summarization to implement a program that can summarize a data set of real-world population records. After you finish the `dataanalysis` program it will compute the summary statistics (e.g., mean, median, and standard deviation) of population data from from 1970 until 2019\. As you enhance your technical skills, you will continue to program with tools such as VS Code and both the Python programming language and the Poetry package manager. Ultimately, your goal for this project is to create a program that can efficiently process real-world data about human population size.

## Project Access

You can access this assignment by clicking the link provided to you in Discord or in the course schedule. Once you click this link it will create a GitHub repository that you can clone to your computer. Specifically, you will need to use the `git clone` command to download the project from GitHub to your computer. Now you are ready to add source code and documentation to the project!

## Expected Output

This project invites you to implement a data summarization program called `dataanalysis`. The `dataanalysis` program takes as input a file of floating point values and computes summary statistics about the numbers. Before you continue to work on this assignment, please make sure that you understand the meaning of the data in this file. To accomplish this task, you should examine the discussion of this data set, including its visualization from 1970 until 2019, from the [Residential Population in Crawford County, PA](https://fred.stlouisfed.org/series/PACRAW0POP) from the [Federal Reserve Bank of St. Louis](https://fred.stlouisfed.org/). The main goal for this program is that it should summarize the population data for Crawford County, the county in which Allegheny College is located. Here is an excerpt from the `input/data.txt` file that contains the real-world population data values that the `dataanalysis` program must summarize:

```
1970-01-01,81.342
1971-01-01,83.300
1972-01-01,84.700
1973-01-01,85.500
1974-01-01,86.100
1975-01-01,87.000
1976-01-01,87.600
1977-01-01,87.600
1978-01-01,88.000
1979-01-01,88.100
1980-01-01,88.869
```

Note: The data contains resident population count information between the years 1970 through 2019.

As this example indicates, the numbers in this file are either strings, that should be interpreted as a date, or a floating-point value, that is a recording of a population estimate of people living in Crawford County. After you have studied and understood the structure of this file's contents, you are ready to install the project's dependencies with the command `poetry install` and then run it with the command `poetry run dataanalysis --data-file input/data.txt`. After you running the program you can use its output and the data visualization available from the Federal Reserve Bank of St. Louis to better understand the population trends for Crawford County. Finally, it is worth noting that the numerical output from the `dataanalysis` program contains four properly indented floating-point values that are always rounded to two decimal places.

```
📦 The data file contains 50 data values in it!

🚀 Let's do some sophisticated data analysis!

🧮 Here are the results of the data analysis:

    The computed mean is 87.80!
    The computed median is 88.05!

    The computed variance is 3.69!
    The computed standard deviation is 1.92!

💡 What does this tell you about the population of this county?
```


```
Don't forget that if you want to run the `dataanalysis` you must use your
terminal to first go into the GitHub repository containing this project and
then go into the `dataanalysis` directory that contains the project's code.
Finally, remember that before running the program you must run `poetry
install` to add the dependencies.
```

## Adding Functionality

If you study the file `dataanalysis/dataanalysis/main.py` you will see that it has many `TODO` markers that designate the parts of the program that you need to implement before `dataanalysis` will produce the correct output. If you run the provided test suite with the command `poetry run task test` or you try to run the program with the command `poetry run dataanalysis --data-file input/data.txt` you will see an error message in your terminal window. This is due to the fact that there are key parts of this program that are missing! In addition to implementing the program's `main` function you also need to correctly `import` the correct modules and objects, like `typer`. Along with adding command-line features to the `main` function in the `main` module, you need to provide an implementation of the following functions:

- `def compute_mean(numbers: List[float]) -> float`
- `def compute_median(numbers: List[float]) -> float`
- `def compute_difference(numbers: List[float]) -> List[float]`
- `def compute_variance(numbers: List[float]) -> float`
- `def compute_standard_deviation(numbers: List[float]) -> float`

It is worth noting that, when appropriate, one of the aforementioned functions can call another function. For instance, the `compute_standard_deviation` can call the `compute_variance`, thereby reusing its code and avoiding unnecessary code duplication. In summary, you must follow all of the instructions next to the `TODO` markers in the provided source code to implement a program that can correctly compute the arithmetic mean of the provided data values in the `dataanalysis/input/data.txt` file. In addition to ensuring that your program is adequately documented, has the correct industry-standard format, and adheres to the industry best practices Python programming, you must implement functions that pass a provided Pytest test suite.

If you look in the files called `test_transform.py` and `test_summarize.py` you will find the test suites for the `transform` and `summarize` modules. As you complete your implementation of `dataanalysis` you should repeatedly run these tests, as explained in the next subsection, to confirm that your program's functions are working correctly. Your program should both produce the correct output and the pass the test suite!

## Running Checks

If you study the source code in the `pyproject.toml` file you will see that it includes the following section section of tasks that use [taskipy](https://github.com/illBeRoy/taskipy):

```toml
[tool.taskipy.tasks]
black = { cmd = "black dataanalysis tests --check", help = "Run the black checks for source code format" }
flake8 = { cmd = "flake8 dataanalysis tests", help = "Run the flake8 checks for source code documentation" }
mypy = { cmd = "poetry run mypy dataanalysis", help = "Run the mypy type checker for potential type errors" }
pydocstyle = { cmd = "pydocstyle dataanalysis tests", help = "Run the pydocstyle checks for source code documentation" }
pylint = { cmd = "pylint dataanalysis tests", help = "Run the pylint checks for source code documentation" }
test = { cmd = "pytest -x -s", help = "Run the pytest test suite" }
test-silent = { cmd = "pytest -x --show-capture=no", help = "Run the pytest test suite without showing output" }
all = "task black && task flake8 && task pydocstyle && task pylint && task mypy && task test"
lint = "task black && task flake8 && task pydocstyle && task pylint"
```

This section makes it easy to run commands like `poetry run task lint` to automatically run all of the linters designed to check the Python source code in your program and its test suite. You can also use the command `poetry run task black` to confirm that your source code adheres to the industry-standard format defined by the `black` tool. If it does not adhere to the standard then you can run the command `poetry run black dataanalysis tests` and it will automatically reformat the source code.

You can also run commands like `poetry run task lint` to automatically run all of the linters designed to check the Python source code in your program and its test suite.

If `gradle grade` shows that all checks pass, you will know that you made progress towards correctly implementing and writing about `dataanalysis`. If your program has all of the anticipated functionality, you can run the command `poetry run task test` and see that the test suite produces output like the following. It is important to note that `dataanalysis` comes with two test suites, both of which should pass so as to establish a confidence in the correctness of the program.

```
collected 13 items

tests/test_summarize.py ...........
tests/test_transform.py ..
```


```
Don't forget that when you commit source code or technical writing to your
GitHub repository for this project, it will trigger the run of a GitHub
Actions workflow. If you are a student at Allegheny College, then running
this workflow consumes build minutes for the course's organization! As such,
you should only commit to your repository once you have made substantive
changes to your project and you are ready to confirm its correctness. Before
you commit to your repository, you can still run checks on your own computer
by either using Poetry or Docker and GatorGrader.
```

## Project Reflection

Once you have finished both of the previous technical tasks, you can use a text editor to answer all of the questions in the `writing/reflection.md` file. For instance, you should provide the output of the Python program in a fenced code block, explain the meaning of the Python source code segments that you implemented, and answer all of the other questions about your experiences in completing this project. The reflection's objective is to invite you to explain the Python functions for data summarization and transformation. As part of this project's reflection you should also consider what technical skills taught in the field of computer science will continue to be the most relevant in the future.

## Project Assessment

The grade that a student receives on this assignment will have the following components.

- **GitHub Actions CI Build Status [up to 50%]:**: For the lab01 repository associated with this assignment students will receive a checkmark grade if their last before-the-deadline build passes. This is only checking some baseline writing and commit requirements as well as correct running of the program. An additional reduction will given if the commit log shows a cluster of commits at the end clearly used just to pass this requirement. An addition reduction will also be given if there is no commit during lab work times. All other requirements are evaluated manually.

- **Mastery of Technical Writing [up to 25%]:**: Students will also receive a checkmark grade when the responses to the writing questions presented in the `reflection.md` reveal a proficiency of both writing skills and technical knowledge. To receive a checkmark grade, the submitted writing should have correct spelling, grammar, and punctuation in addition to following the rules of Markdown and providing conceptually and technically accurate answers.

- **Mastery of Technical Knowledge and Skills [up to 25%]**: Students will receive a portion of their assignment grade when their program implementation reveals that they have mastered all of the technical knowledge and skills developed during the completion of this assignment. As a part of this grade, the instructor will assess aspects of the programming including, but not limited to, the completeness and the correctness of the program and the use of effective source code comments.


## GatorGrade

### Checks for GatorGrade

For immediate feedback on submissions, we will be using Gator Grade to inform the of missing components in the submission. As you submit, you will notice that there is a thick red X that will change to a green check mark when all components have been included in the submission. You are encouraged to click on the red X to find a listing of the components to address.

You can check the baseline writing and commit requirements for this lab assignment by running department's assignment checking `gatorgrade` tool. To use `gatorgrade`, you first need to make sure you have Python3 installed (type `python --version` to check). If you do not have Python installed, please see:

- [Setting Up Python on Windows](https://realpython.com/lessons/python-windows-setup/)
- [Python 3 Installation and Setup Guide](https://realpython.com/installing-python/)
- [How to Install Python 3 and Set Up a Local Programming Environment on Windows 10](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-windows-10)

Then, if you have not done so already, you need to install `gatorgrade`:

- First, [install `pipx`](https://pypa.github.io/pipx/installation/)
- Then, install `gatorgrade` with `pipx install gatorgrade`

Finally, you can run `gatorgrade`: `gatorgrade --config config/gatorgrade.yml`

## Seeking Assistance

Students who have questions about this project outside of the lab time are invited to ask them in the course's Discord channel or during instructor's or TLs' office hours.
