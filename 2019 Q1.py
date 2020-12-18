# output the smallest palindromic number that is higher than the input.

def gen_palindrome(n):
    # n should be a string

    if n=='9': return '11'
    length = len(n)
    mid = length//2
    left = n[:mid]
    middle = ""
    out = ""
    
    if length%2 == 1:
        right = n[mid+1:]
        middle = n[mid]
    else:
        right = n[mid:]
        
    if left[::-1] > right:
        out += left + middle + left[::-1]
    else:
        out += str(int(left + middle) + 1)
        out += out[:mid][::-1]
    return out
    
def main():
    while True:
        n = input("Enter Number: ")
        print(gen_palindrome(n))
    
if __name__ == "__main__":
    main()



