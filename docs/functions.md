# Functions overview
The functions for certain shapes are located in the corresponding files.

## circle.py
### area(r)
Finds an area of circle with radius r.\
**_Receive:_**\
r (float): radius of circle.\
**_Return:_**\
circle area (float): S = πr²
```
r = 10
S = area(r) # 314.1592...
```
### perimeter(r)
Finds a perimeter of circle with radius r.\
**_Receive:_**\
r (float): radius of circle.\
**_Return:_**\
circle perimeter (float): P = 2*π*r
```
r = 10
P = perimeter(r) # 62.8318...
```

## rectangle.py
### area(a, b)
Finds an area of rectangle with sides a and b.\
**_Receive:_**\
a (float): rectangle length\
b (float): rectangle width\
**_Return:_**\
rectangle area (float): S = ab
```
a = 6
b = 5
S = area(a, b) # 30
```
### perimeter(a, b)
Finds a perimeter of rectangle with sides a and b.\
**_Receive:_**\
a (float): rectangle length\
b (float): rectangle width\
**_Return:_**\
rectangle perimeter (float): P = a + a + b + b = 2(a + b)
```
a = 6
b = 5
P = perimeter(a, b) # 22
```

## square.py
### area(a, b)
Finds an area of square with side a.\
**_Receive:_**\
a (float): square side\
**_Return:_**\
square area (float): S = a * a = a²
```
a = 6
S = area(a) # 36
```
### perimeter(a)
Finds a perimeter of square with side a.\
**_Receive:_**\
a (float): square side\
**_Return:_**\
square perimeter (float): P = a + a + a + a = 4a
```
a = 6
P = perimeter(a) # 24
```

## triangle.py
### area(a, h)
Finds an area of triangle with base a and height h.
> **NOTE:**  The height is dropped to the base of the triangle

**_Receive:_**\
a (float): rectangle length\
b (float): rectangle width\
**_Return:_**\
triangle area (float): S = a * h / 2
```
a = 5
h = 6
S = ares(a, h) # 15
```
### perimeter(a, b, c)
Finds a perimeter of triangle with sides a, b and c.\
**_Receive:_**\
a (float): first triangle side\
b (float): second triangle side\
c (float): third triangle side\
**_Return:_**\
triangle perimeter (float): P = a + b + c
```
a = 3
b = 4
c = 5
P = perimeter(a, b, c) # 12
```