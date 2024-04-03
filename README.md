# pyBookBot

## description

* A `boot.dev` guided project.
  * everything after commit id: `432051146baee1c38fc5c0cafc54271e21138107` are features added beyond scope of project.
* features added beyond scope of project:
  * `pyBookBot` generates reports for more than one book.
  * `pyBookBot` checks if a `books/` directory exists, it gets all the books in that directory, and checks if they are `.txt` files before generating a report.
  * added unit tests to `pyBookBot`
    * tests can be run in a `shell` via `./test.sh`
    * depends on `pytest` as the test runner

## to do

- [ ] change `main.py` to `py_book_bot.py`
- [ ] convert `test.sh`, `reports_setup.sh`, `test_helper0.sh`, `test_helper1.sh`, `test_cleanup0.sh`, `test_cleanup1.sh` scripts to `python` modules
- [ ] use `main` idiom on line 81 of `main.py`
- [ ] take book file download link and filename from user as `stdin`
- [ ] determine if downloaded file is a text file (bytecode?), go above and beyond extension checking
