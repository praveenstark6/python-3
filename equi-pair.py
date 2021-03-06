"""
Ron Wesley has been bit by a three headed snake and Harry Potter is searching for a potion.
The Witch promises to tell the ingredients of the medicine if Harry can find equi pair of an array.
Listen to the conversation between Harry The witch to know more about equi pairs.
Conversation:- The Witch : To find the equi pair, you must know how to find the slices first.
Harry : What is a slice? The Witch : If Z is an array with N elements,
a slice of indices (X, Y) is Z[X] + Z[X+1]...Z[Y]
Harry : How can I use it to find equi pair?
The Witch : (a, b) is an equi pair if slice of (0, a-1) = slice of (a+1, b-1) = slice of (b+1, N-1)
and b>a+1 and size of array > 4

Input Format:

The first input contains an integer 'N' denotes the size of an array
An array of N integers delimited by whitespace

Output Format:

Print equi pair in first line in the format { a,b }
Print slices in the format { 0,a-1 }, { a+1,b-1 }, { b+1,N-1 }
OR
Print "Array does not contain any equi pair" if there are no equi pairs in the array.

Constraints:

Zi >= 0 and 1<= i <=N
size of array (N) > 4
b > (a+1)
Sample Input :
10
8 3 5 2 10 6 7 9 5 2
Sample Output:
Indices which form equi pair {3,6}
Slices are {0,2},{4,5},{7,9}
"""


num = int(input())
ar = list(map(int, input().split()))


def equi_pair(n, array):
    for i in range(n):
        for j in range(i + 2, n):
            if sum(array[0:i]) == sum(array[i + 1:j]) == sum(array[j + 1:n]):
                return ("Indices which form equi pair {" + str(i) + "," + str(j) + "}\nSlices are {0," + str(i - 1) +
                        "},{" + str(i + 1) + "," + str(j - 1) + "},{" + str(j + 1) + "," + str(n - 1) + "}")
    else:
        return "Array does not contain any equi pair"


print(equi_pair(num, ar))

# code by Praveen
