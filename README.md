# mkdocstring-parser

This repo creates a simple parser for mkdocstrings. The idea is simple, given
a `mkdocstrings` signature block, replace it with it rendered markdown in-place.

To view the complete guide on generating Nixtlaverse documentation, click [here](https://www.notion.so/nixtla/Env-Setup-1aa34e7ecc8c804096f7d0915aa4f2d5?source=copy_link#2a334e7ecc8c8006901aed0eb6ebd2f0)

## example

```md
# title

::: my_module.my_function
```

gets rendered as

````md
# title

```py
def my_function(a, b):
    ...
    ...
    # and so on
```

````

## to run the code

```sh
python parser.py
```

## cases to be mindful of while creating tests for the parser

- [ ] class with no public methods (datasetsforecast.favorita.CodeTimer)
  - it documents the instance variables then
- [X] dataclass
- [X] pure functions
- [X] pure functions (with decorator-based docstring)
