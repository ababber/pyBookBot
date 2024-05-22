# pyBookBot

## description

* A `boot.dev` guided project.
  * everything after commit id: `432051146baee1c38fc5c0cafc54271e21138107` are features added beyond scope of project.
* features added beyond scope of project:
  * `pyBookBot` generates reports for more than one book.
  * `pyBookBot` checks if a `books/` directory exists, it gets all the books in that directory, and checks if they are `.txt` files before generating a report.
  * `pyBookBot` also checks the reports and error messages that should be generated.
  * added unit tests to `pyBookBot`
    * tests can be run in a `shell` via `./test.sh`
    * depends on `pytest` as the test runner
    * added `python pyBookBot.py test.sh` command line entry point (assuming local namespace uses `python` for running `.py` files)

## to do

* [ ] convert all `test.sh`, `reports_setup.sh`, `test_helper0.sh`, `test_helper1.sh`, `test_cleanup0.sh`, `test_cleanup1.sh` to python f(n)s
* [ ] take source download link and filename from user
* [ ] determine if downloaded file is a text file (bytecode?), go above and beyond extension checking
* [X] use `main` idiom on line 81
* [X] change `main.py` to `pyBookBot.py`
