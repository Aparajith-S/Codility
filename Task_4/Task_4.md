# Problem Description

## Task 4 : chocolate problem
**************************
two positive integers M and N are given.
N represents the number of chocolates arranged in a circle numbered from 0 to N-1

you start eating the chocolates and leave the wrapper behind. you start from 0 and skip next M-1 chocolates or wrappers and eat the next one.

e.g. if you eat chocolate number x then you eat the chocolate with number (N+M)modulo(N)
you halt when you encounter a wrapper.

e.g. N=10 and M = 4 then you eat 0,4,8,2,6. the function you write should return number of chocolates consumed which is 5 in this case. write an efficient algorithm for this.

N,M are integers within the range [1 .. 1,00,000,000]. 

Solution is provided in `Task_4_chocolate.py`
