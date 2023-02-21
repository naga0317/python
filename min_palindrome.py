# python3 program to count minimum reduce
# operations to make a palindrome
 
# Returns count of minimum character
# reduce operations to make palindrome.
def countReduce(str):
 
    n = len(str)
    res = 0
 
    # Compare every character of first half
    # with the corresponding character of
    # second half and add difference to
    # result.
    for i in range(0, int(n/2)):
        res += abs( int(ord(str[i])) -
               int(ord(str[n - i - 1])) )
     
    return res
 
# Driver code
str = "abcd"
print(countReduce(str))
