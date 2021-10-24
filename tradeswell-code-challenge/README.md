# Tradeswell Code Challenge

Dice come in more shapes than a cube. A standard set of polyhedral dice includes
dice with the following number of sides: 20, 12, 10, 8, 6, and 4. Each can
generate a number between 1 and its number of sides. For example, an 8-sided die
generates numbers between 1 and 8 inclusive.

### Die Expression Specification

A die type (number of sides) is expressed by the form ```dS``` where the letter
d is case insensitive and S is the number of sides of the die in question:

```
D8    - 8 sided die
D10  - 10 sided die
D20  - 20 sided die
etc...
```

A die roll of a given type can be expressed by prepending a die type with an
integer indicating the number of times to roll that die type (with the result
being the sum of those rolls).

```
1d8  - roll one 8 sided die
3d6  - roll three six sided dice and sum them
```

In the case where only 1 die of a type is rolled the `1` can be elided.

```
1d6 == d6
```


Dice can be combined through addition and subtraction and “raw” integer
modifiers can be added to the roll:

```
2d6 + d8 + 4
D20 - 1 + 4d12
```

## Task

You will read a file of die roll expressions, one expression per line and output
a json file representing the results. The output json should be a list of json
objects, one object per line showing the results of parsing and evaluating that
line. The format of the json output for one line should look like this:

```
{“roll-result” : the result of the roll
“roll-min” : the minimum possible result of this roll
“roll-max” : the maximum possible result of this roll}
```

Tests are not necessary but can certainly help ensure a correct solution. A
sample input file with the matching JSON output is provided.

Please setup your solution to take either a single argument (the input file) or
two arguments (the input file and the output file). It's perfectly acceptable to
simply dump the solution to stdout.

Your submission should include instructions on how to run your solution.


### Language Choice

Please stick to one of the following implementation languages: JS/Typescript, Python, Kotlin. No Jupyter notebooks please.
