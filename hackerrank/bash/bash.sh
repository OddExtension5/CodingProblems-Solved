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




