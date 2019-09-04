## Exercise: Importing

For these exercises to work, you have to either:

- make your package available from anywhere by running  `pip install -e /path/to/ODD_dir` from anywhere.

  



------

### Part 1 - importing potions (repetition)

- Check that both `__init__.py` files are empty apart from the print statements. 

- In a terminal, load a Python interpreter (type `python` ) and run

  ```python
  >>> import potions
  ```

  - Can you access the function `func()`in `potion.py` without another import statement?
  - If not, how do you have to change the import statement to be able to access `func()`?
  - Can you access the variable `fish_eyes`in `/tools/ingredients.py` without another import statement?
  - If not, how do you have to change the import statement to be able to access `fish_eyes`?

Tip:

Make sure you quit and reload the Python interpreter whenever you change need to re-run import statements. You can exit the Python interpreter by typing `exit()` or ctrl-d.



------

### Part 2 - adding to the `potions/__init__.py` file to access a module in `/potions`

- Remember that running `import potions` will execute the code in `potions/__init__.py`. 

- What import statement(s) do you have to add to the `/potions/__init__.py` file so that the following lines work (if possible)? Start a new Python interpreter each time you import potions.

  a)
  
  ```python
  >>> import potions
>>> potions.potion.func()
  ```
  
  b)
  
```python
  >>> import potions
  >>> potions.func()
  ```
  
  c)
  
  ```python
  >>> import potions
  >>> func()
  ```

Tips:

Make sure you quit and reload the Python interpreter whenever you changed the `__init__.py`file.

Make sure you saved the changes in the `__init__.py`file.

Make sure you are editing the correct `__init__.py`file.

Remember that you can also import using `from <package_name> import <module_name>` and `from <module_name> import <function_name>`





------

### Part 3 - adding to the `potions/__init__.py` file to access a module in `/potions/tools`

- Add the following import statement to the` /potions/__init__.py` file:

  ```python
  from potions.tools import ingredients
  ```
  
- Which of the following statements will allow you to access the variable `fish_eyes` if you `import potions` in a Python interpreter? 

  a) potions.tools.ingredients.fish_eyes

  b) potions.tools.fish_eyes

  c) potions.ingredients.fish_eyes

  d) potions.fish_eyes

- Now change the import statement in the ` /potions/__init__.py` file to:

  ```python
  from potions.tools.ingredients import fish_eyes
  ```

  a) potions.tools.ingredients.fish_eyes

  b) potions.tools.fish_eyes

  c) potions.ingredients.fish_eyes

  d) potions.fish_eyes



Tip:

Try it out for yourself



------

### Part 4 - can you split statements over the two **init**.py files?

- You maybe noticed that in Part 3 you could not get `potions.tools.fish_eyes` to work (spoilers :) !).  
What import statements in the `/potions/tools/__init__.py` and`/potions/__init__.py` files do you need to get this to work? 
  
  ```python
  >>> import potions
  >>> potions.tools.fish_eyes
  ```

