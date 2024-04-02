#!/bin/bash

mkdir books
cd books
curl https://www.gutenberg.org/cache/epub/84/pg84.txt -o "frankenstein.txt"
wait
curl https://www.gutenberg.org/cache/epub/5200/pg5200.txt -o "metamorphosis.txt"
wait
cd ..
pytest unit_tests.py -vv
rm -r ./test_helpers/__pycache__
rm -r .pytest_cache
rm -r __pycache__
rm -r books
