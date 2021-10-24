
# Overview

## Problem 1

The following link has a scrambled image Y of a grayscale image X. Image X has a number. Here are some facts:

1. Image X was scrambled in Python 2.7 using the Mersenne Twister random number generator seeded with the number 2.

2. We used the numpy flatten() function to flatten the 2D image into a 1D array.

3. We used the random.shuffle(...) function (not the numpy one) to shuffle a list of numbers [0, 1, 2, …, n-1] where n is the number of pixels in image X.

4. The shuffled list was used to assign the pixels in the scrambled image like Y[i] = X[shuffled[i]] for all i in [0, 1, 2, …, n-1].

5. Tell us, what's the number in image X? If the unscrambled image is noisy, don't worry about it, as long as you can see the number.

## Problem 2

The following is a CSV file containing a list of of 137 points along the perimeter of a circle. The (x,y) positions of the points are rounded to 2 decimal places. All points are listed in clockwise order except one. The CSV file contains 3 columns: point_id, point_x, point_y. What is the point_id of the one point that is not listed clockwise?
