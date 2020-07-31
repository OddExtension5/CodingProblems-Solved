###################################################################
########## LINUX SHELL : BASH || HACKERRANK PROBLEMS ##############
###################################################################


##### PROBLEM 1 #####
## /* Your task is to use for loops to display only odd natural numbers from  1 to 99 */ ##

for ((i=0; i<100; i++));
do
    rem=$(( $i %2 ))

    if [[ $rem -ne 0 ]];
    then
        echo $i
    fi
done


##### PROBLEM 2 #####
## /* Write a Bash script which accepts name as input and displays a greeting: "Welcome (name)" */ ##

read name
echo "Welcome $name"


##### PROBLEM 3 #####
## /* Use a for loop to display the natural numbers from 1 to 50. */ ##

for ((i=1; i<51; i++));
do
    echo $i
done


##### PROBLEM 4: The World of Numbers #####
## /* Given two integers, X and Y, find their sum, difference, product, quotient and remainder. */ ##

read X
read Y

add=$(( X + Y))
sub=$(( X - Y))
mul=$(( X*Y ))
quot=$(( X/Y ))
rem=$(( X%Y ))

echo $add
echo $sub
echo $mul
echo $quot
echo $rem

##### PROBLEM 5: Compairing Number #####
:' /* Given two integers, X and Y , identify whether X < Y  or X > Y orX = Y.

Exactly one of the following lines:
- X is less than Y
- X is greater than Y
- X is equal to Y
*/
'
read X
read Y

if [[ $X -eq $Y ]];
then
    echo "X is equal to Y"
elif [[ $X -gt $Y ]];
then 
    echo "X is greater than Y"
else
    echo "X is less than Y"
fi

##### PROBLEM 6: Getting started with conditionals #####
:'
Read in one character from STDIN.
If the character is 'Y' or 'y' display "YES".
If the character is 'N' or 'n' display "NO".
No other character will be provided as input.
'
read m

if [[ $m == Y || $m == y ]];
then
    echo "YES"
fi

if [[ $m == N || $m == n ]];
then 
    echo "NO"
fi

##### PROBLEM 7: More on Conditionals #####
:'
Given three integers (X, Y, and Z ) representing the three sides of a triangle, identify whether the triangle is scalene, 
isosceles, or equilateral.

If all three sides are equal, output EQUILATERAL.
Otherwise, if any two sides are equal, output ISOSCELES.
Otherwise, output SCALENE.
'

read X
read Y
read Z

if [[ $X == $Y && $Y == $Z ]];
then
    echo "EQUILATERAL"
elif [[ $X != $Y && $Y != $Z && $Z != $X ]];
then
    echo "SCALENE"
else
    echo "ISOSCELES"
fi


##### PROBLEM 8: Arithmetic Operations #####
:'
A mathematical expression containing +,-,*,^, / and parenthesis will be provided. 
Read in the expression, then evaluate it. Display the result rounded to 3 decimal places.
'

read exp
value=` echo "$exp" | bc -l`
printf "%.3f" $value


##### PROBLEM 9: Compute the Average #####
:'
Given N integers, compute their average, rounded to three decimal places.
'

read n
arr=($(cat))
arr=${arr[*]}
printf "%.3f" $(echo $((${arr// /+}))/$n | bc -l)

# OR

read n
printf "%.3f" $(echo "("$(cat)")/$n" | tr ' ' '+' | bc -l)

# OR

read n
sum=0
for (( i=0; i<$n; i++ ));
do
    read temp
    sum=$(($sum+$temp))
done
printf "%.3f\n" $(bc -l <<< "$sum/$n")

#### PROBLEM 10: Functions and Fractals - Recursive Trees #####
:'
Problem Link: https://www.hackerrank.com/challenges/fractal-trees-all/problem?h_r=next-challenge&h_v=zen
'

