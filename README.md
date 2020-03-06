# TDD Naan Factory Exercise

This exercise is going to bring together lots of concepts.

Learning Objectives:
- Git 
- GitHUB
- Functions
- TDD
- Separations of concerns
- DRY code
- DOD

## Installing and running

```python
import naan_factory
run_factory()
```

### TDD - Test Driven Development

1. Write the test
2. Run ot, and read the error
3. code and make it pass the test

this helps with:
- Stop over engineering
- Maintainable code
- Reduce technical debt
- Goes well with agile and working code
- errors can be your guide in complex systems

How it works is that we write Unit tests.

### Unit Tests

Test single pieces of code like a function.

** Base of a test **

Usually has 3 phases.
- setup phase (known variables)
- calling of the function / piece of code with known variables
- asserting for expect output

### User Stories for Naan Factory

```
1. 
# As a user, I can use the make_dough with water and flour to make dough.

2.
# As a user, I can use the bake_dough with dough to get naan

3.
# As a user, I can use the run_factory with water and flour and get naan.
```