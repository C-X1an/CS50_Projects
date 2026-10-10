# CS50 learning archive

Exercises and projects written while studying Harvard's CS50 material. This repository records practice in programming, algorithms, SQL and web applications; it does not assert course completion or certification.

| Collection | Explore | Main areas |
| --- | --- | --- |
| CS50's Introduction to Programming with Python | [cs50p](cs50p/) | Python, file handling, libraries and tests |
| CS50's Introduction to Computer Science | [cs50x](cs50x/) | C, algorithms, data structures, SQL and web development |
| Finance web exercise | [Week 9 / finance](cs50x/Week9/finance/) | Flask, authentication and SQLite |

The folders retain the original coursework structure. They are a learning archive, not a uniformly maintained application or a claim that every exercise passes the current course grader.

## Finance database setup

Mutable finance accounts and transaction records are excluded from the current tree. To create a clean database with **no accounts, hashes or transactions**:

```sh
cd cs50x/Week9/finance
python init_db.py
```

The initializer reads `schema.sql` and refuses to overwrite existing data. Application dependencies and any quote-provider configuration still need to match the original exercise. This check verifies database setup, not live quote lookup or production readiness. Older commits may still contain the former development database; removing the current file does not rewrite history.

Run the data-free schema check from the repository root:

```sh
python -m unittest discover -s tests -v
```

## Attribution and reuse

Course scaffolding and supplied datasets originate from [CS50](https://cs50.harvard.edu/). Respect the relevant course licenses and [academic honesty rules](https://cs50.harvard.edu/x/2026/honesty/) when studying this work. Supplied investigation and music datasets are coursework inputs; the mutable finance database is excluded. No separate blanket license is declared for this repository.
