## Exercise: Writing and testing functions

We want to mimic the *write feature*⇄ *test feature* workflow. This is supposed to be easy and fun, so feel free to make mistakes with the potion and test as much as you want.

Complete the `make_python_expert_potion`  function that makes the Python expert potion (instructions below). 

Get Professor Snape to inspect your potion as shown for the example potion (make sure you change the target potion to `python_expert`).



### Brewing instructions

Make a new potion called `python_expert` according to these instructions:

```
- Set up a pewter cauldron and light a fire underneath it.
- Add fish eyes, unicorn hair and tea leaves and stir anti-clockwise.
- Let simmer for 2 hours (should turn from transparent to green).
- Have Snape inspect the potion (use target_potion='python_expert').
```

Note that the `example_potion()`function is missing a crucial step and does not pass Snape's inspection. You can find more information by accessing the documentation of `Potion()`using `help(potions.potion.Potion)` from a Python interpreter.



### Tests

The `inspection_by_Snape()` function checks your function (ingredients, setup etc.); you call  as shown in the example potion in `make_potion.py`.

Note that if you call inspection_by_Snape, you should never get an error, so you will have to read what Snape does and says to find out what went wrong.

At any time, you can check whether your  `make_python_expert_potion`  function returns the correct type using pytest (from the /ODD_dir). Definitely also do this once your potion has passed the inspeciton by Snape.



### Help

You may change the import statements to anything more comfortable.

You can access the documentation for any function you use via the help function in a Python interpreter: `help(package_name.module_name.class_name.method_name)`. If you have changed your import statements to use `Potions()`directly, you can also access its documentation in that way i.e. `help(Potions)`.

(Press `q`to exit the help)

You also may look into the files in `/potions`and `/tools`
