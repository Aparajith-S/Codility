# Codility
solutions to challenges/lessons that are completed. Sharing answers to challenges that have expired and to lessons are not in violation as per codility's rules. 

## Task 1 : Manhattan Problem:
***************************
You are going to build a stone wall. The wall should be straight and N meters long, and its thickness should be constant; however, it should have different heights in different places. The height of the wall is specified by an array H of N positive integers. H[I] is the height of the wall from I to I+1 meters to the right of its left end. In particular, H[0] is the height of the wall's left end and H[N−1] is the height of the wall's right end.

The wall should be built of cuboid stone blocks (that is, all sides of such blocks are rectangular). Your task is to compute the minimum number of blocks needed to build the wall.

Write a function:

    int solution(int H[], int N);

that, given an array H of N positive integers specifying the height of the wall, returns the minimum number of blocks needed to build it.

For example, given array H containing N = 9 integers:

    H[0] = 8    H[1] = 8    H[2] = 5
    H[3] = 7    H[4] = 9    H[5] = 8
    H[6] = 7    H[7] = 4    H[8] = 8  
the function should return 7. The figure shows one possible arrangement of seven blocks.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array H is an integer within the range [1..1,000,000,000].

solution is provided in `Task_1_manhattan.c`

## Task2: Min perimeter Rectangle
******************************
An integer N is given, representing the area of some rectangle.

The area of a rectangle whose sides are of length A and B is A * B, and the perimeter is 2 * (A + B).

The goal is to find the minimal perimeter of any rectangle whose area equals N. The sides of this rectangle should be only integers.

For example, given integer N = 30, rectangles of area 30 are:

    (1, 30), with a perimeter of 62,
    (2, 15), with a perimeter of 34,
    (3, 10), with a perimeter of 26,
    (5, 6), with a perimeter of 22.

Write a function:

that, given an integer N, returns the minimal perimeter of any rectangle whose area is exactly equal to N.

For example, given an integer N = 30, the function should return 22, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..1,000,000,000].

solution is provided in `Task_2_Min_perimeter.c`

## Task 3: common prime divisors
********************************
Given 2 integers find if these integers have common prime divisors.

example:
if N =15 and M =75 the prime divisors are same {3,5}
if N=10 and M = 30 then they dont have same prime divisors {2,5} != {2,3,5}

Solution is provided in `Task_3_divisors.py`

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

## Task 5: Distinct Absolute values
************************************

A non-empty array A consisting of N numbers is given. The array is sorted in non-decreasing order. The absolute distinct count of this array is the number of distinct absolute values among the elements of the array.

For example, consider array A such that:
   
    A[0] = -5
    A[1] = -3
    A[2] = -1
    A[3] =  0
    A[4] =  3
    A[5] =  6

The absolute distinct count of this array is 5, because there are 5 distinct absolute values among the elements of this array, namely 0, 1, 3, 5 and 6.

Write a function:

    int solution(int A[], int N);

that, given a non-empty array A consisting of N numbers, returns absolute distinct count of array A.

For example, given array A such that:

    A[0] = -5
    A[1] = -3
    A[2] = -1
    A[3] =  0
    A[4] =  3
    A[5] =  6

the function should return 5, as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..100,000];
        each element of array A is an integer within the range [−2,147,483,648..2,147,483,647];
        array A is sorted in non-decreasing order.

Solution is provided in `Task_5_distinct_Abs.c`

## Sieve of Eratosthenes
************************

The genius greek polymath who gave us with an interesting way to find prime numbers.
the sieve of finding prime numbers as he was attributed to it. 
       
       Time complexity : O(N)

Unknown witty poem:

    Sift the Two's and Sift the Three's,
    The Sieve of Eratosthenes.
    When the multiples sublime,
    The numbers that remain are Prime.

link: [https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes]

code is given in `Task_6_primes.py`
