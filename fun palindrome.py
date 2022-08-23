
def palindrome(num):
    if (num==num[::-1]):
        return 'palindrome'
    else:
        return 'not a palindrome'
num = input(123421)
print(palindrome(num))