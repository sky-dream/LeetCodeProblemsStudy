﻿Given two straight line segments (represented as a start point and an end point), compute the point of intersection, if any. If there's no intersection, return an empty array.

The absolute error should not exceed 10^-6. If there are more than one intersections, return the one with smallest X axis value. If there are more than one intersections that have same X axis value, return the one with smallest Y axis value.

# Example 1:
```
Input: 
line1 = {0, 0}, {1, 0}
line2 = {1, 1}, {0, -1}
Output:  {0.5, 0}
```
# Example 2:
```
Input: 
line1 = {0, 0}, {3, 3}
line2 = {1, 1}, {2, 2}
Output:  {1, 1}
```
# Example 3:
```
Input: 
line1 = {0, 0}, {1, 1}
line2 = {1, 0}, {2, 1}
Output:  {}  (no intersection)
```
# Note:

- The absolute value of coordinate value will not exceed 2^7.
- All coordinates are valid 2D coordinates.