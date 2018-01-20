# Quetzal

## General

To execute the system, use:

    python3 main.py <system.txt>

This will execute the system and print all log files in the same directory. With `systems/1.txt` we (almost) recreate the given log file in `log4.html`.

## Testing

Unit tests are implemented using the `unittest` package of Python. Both `quetzal` and `datastructures` have their own unit tests in their respective `tests` directory.

### Running all tests

The `run_test.py` script will run all tests that are defined in the `test_list` of the `__init__.py` file in the `tests` directory. This is the simplest and cleanest way to run all tests:

    $ ./run_tests.py

An alternative way is to use the `discover` option of `unittest`, which will run all tests modules in `tests` that follow the pattern `test_*.py`:

    $ python3 -m unittest discover tests -v

Note: this has te be executed from the same directory as `run_tests.py` for the imports to work.

### Running a single test

To run a single test module, in this example `TestStock`, you can manually call `unittest`:

    $ python3 -m unittest tests.test_stock.TestStock -v

You have to reference the method/class in the same way as you would import it for this to work.
