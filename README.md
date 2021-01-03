# README for pytest-bdd example

Code for an example talked about here: https://cheesecakelabs.com/blog/behavior-driven-development-tests-pokedex-bdd/ 

Also need to ensure Firefox and Geckodriver, https://github.com/mozilla/geckodriver, are installed.


# Run from terminal

```
(.venv) C:\Users\rnwol\workspace\pokedex-pytest-bdd>pytest -v
================================================================================================================= test session starts =================================================================================================================
platform win32 -- Python 3.8.6, pytest-6.2.1, py-1.10.0, pluggy-0.13.1 -- c:\users\rnwol\workspace\pokedex-pytest-bdd\.venv\scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\rnwol\workspace\pokedex-pytest-bdd
plugins: bdd-4.0.2
collected 2 items                                                                                                                                                                                                                                      

tests/step_definitions/test_pokedex_steps.py::test_name_pokedex_search[Pikachu-Pikachu] PASSED                                                                                                                                                   [ 50%]
tests/step_definitions/test_pokedex_steps.py::test_name_pokedex_search[Charmander-Charmander] PASSED                                                                                                                                             [100%]

================================================================================================================= 2 passed in 15.06s ==================================================================================================================
```