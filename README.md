# pyBookBot

## depends on `macOS`/`linux`, `python >= 3.7`, `pytest`, `bash`/`zsh`, `file`, `curl`, `touch`, `rm`

## running and testing

* assuming local shell environment command for python interpreter is `python`
* `python pyBookBot.py run`
  * downloads `books/`, runs the program, and outputs results to `reports/`
* `python pyBookBot.py test`
  * runs tests and cleans up `books/` and `reports/`

## description

* A `boot.dev` guided project.
  * everything after commit id: `432051146baee1c38fc5c0cafc54271e21138107` are features added beyond scope of project.
* features added beyond scope of project:
  * `pyBookBot` generates reports for more than one book.
  * `pyBookBot` checks if a `books/` directory exists, it gets all the books in that directory, and checks if they are `.txt` files before generating a report.
  * `pyBookBot` also checks the reports and error messages that should be generated.
  * added unit tests to `pyBookBot`
    * tests can be run in a `shell` via `./test.sh`
    * added `python pyBookBot.py test.sh` command line entry point (assuming local shell environment uses `python` command for running `.py` files)
    * added check for mime type using sys command `file` (if current OS does not have `file`, mime type test will fail)

## to do

* [ ] add pythonic `prepPyBookBot.py` module to run `python pyBookBot.py main`
* [ ] convert all `test.sh`, `reports_setup.sh`, `test_helper0.sh`, `test_helper1.sh`, `test_cleanup0.sh`, `test_cleanup1.sh` to python modules
* [ ] take source download link and filename from user
* [X] add `main` and `test` option to cli with `shell` implementation
* [X] determine if downloaded file is a text file (bytecode?), go above and beyond extension checking
* [X] use `main` idiom on line 81
* [X] change `main.py` to `pyBookBot.py`
