# READ ME

My solution used two classes: 1) PolyHendronDie 2) DiceCalculator. PolyHendronDie calculates the random,min,max values per dice. 
DiceCalculator parses the expression, performs the operations, and computes the result. I used regular expressions to parse out whether the expression was a dice, operation, or number.
I decided not to parse die that did not have an associated number of rolls. Another aspect to consider was assigning the max value (per dice) when the operation was subtraction for the minimum sum of the expression, etc.

## Build Docker Container

I decided to use a rest api to read in the input file, perform the calculation, and output the json result. 

Learning Flask, on the fly, was a bit more challenging than expected (I thought it was going to be very easy), but I also thought it would be overkill to use GRPC.

```
docker build -t dice-api .

docker run -d -p 5000:5000 dice-api
```

# Run the Client Script

The client script will send the contents of the inputfile to the rest api, collect the result, and save the result in a json file (formatted).

```
python client_script.py --input_filename example_input.txt --output_filename outout.json
```