# Data Structures & Algorithms -- Exam Practice Codes

------------------------------------------------------------------------

## Q1. Count Total Digits in a Number

``` python
n = int(input("Enter number: "))
count = 0

while n != 0:
    n = n // 10
    count += 1

print("Total digits:", count)
```

------------------------------------------------------------------------

## Q2. Reverse Digits of a Number

``` python
n = int(input("Enter number: "))
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

print("Reversed:", rev)
```

------------------------------------------------------------------------

## Q3. Check Palindrome Number

``` python
n = int(input("Enter number: "))
temp = n
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

if rev == temp:
    print("Palindrome")
else:
    print("Not Palindrome")
```

------------------------------------------------------------------------

## Q4. Armstrong Number

``` python
n = int(input("Enter number: "))
temp = n
sum = 0

while n > 0:
    digit = n % 10
    sum = sum + digit*digit*digit
    n = n // 10

if sum == temp:
    print("Armstrong")
else:
    print("Not Armstrong")
```

------------------------------------------------------------------------

## Q5. Decimal to Binary

``` python
n = int(input("Enter number: "))
binary = ""

while n > 0:
    r = n % 2
    binary = str(r) + binary
    n = n // 2

print(binary)
```

------------------------------------------------------------------------

## Q6. Print Alternate Elements

``` python
arr = [1,2,3,4,5,6]

for i in range(0,len(arr),2):
    print(arr[i])
```

------------------------------------------------------------------------

## Q7. Sum and Product of Array

``` python
arr = [1,2,3,4]

sum_val = 0
product = 1

for i in range(len(arr)):
    sum_val = sum_val + arr[i]
    product = product * arr[i]

print("Sum:",sum_val)
print("Product:",product)
```

------------------------------------------------------------------------

## Q8. Count Occurrences of Target

``` python
arr = [1,2,3,2,4,2]
target = 2
count = 0

for i in range(len(arr)):
    if arr[i] == target:
        count += 1

print("Occurrences:",count)
```

------------------------------------------------------------------------

## Q9. Check Sorted Forward/Backward

``` python
arr = [1,2,3,4]

forward = True
backward = True

for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
        forward = False
    if arr[i] < arr[i+1]:
        backward = False

if forward:
    print("Sorted Forward")
elif backward:
    print("Sorted Backward")
else:
    print("Not Sorted")
```

------------------------------------------------------------------------

## Q10. Distinct Elements

``` python
arr = [1,2,2,3,4,4,5]

for i in range(len(arr)):
    found = False
    
    for j in range(i):
        if arr[i] == arr[j]:
            found = True
            break
    
    if not found:
        print(arr[i])
```

------------------------------------------------------------------------

## Q11. Two Elements with Target Sum

``` python
arr = [2,7,11,15]
target = 9

found = False

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i] + arr[j] == target:
            found = True

if found:
    print("Pair Exists")
else:
    print("Pair Does Not Exist")
```

------------------------------------------------------------------------

## Q12. Find Missing Number

``` python
arr = [1,2,4,5]
n = 5

for i in range(1,n+1):
    found = False
    
    for j in range(len(arr)):
        if arr[j] == i:
            found = True
            break
    
    if not found:
        print("Missing:",i)
```

------------------------------------------------------------------------

## Q13. Second Smallest and Second Largest

``` python
arr = [10,20,30,40,50]

small = arr[0]
large = arr[0]

for i in range(len(arr)):
    if arr[i] < small:
        small = arr[i]
    if arr[i] > large:
        large = arr[i]

second_small = large
second_large = small

for i in range(len(arr)):
    if arr[i] > small and arr[i] < second_small:
        second_small = arr[i]

    if arr[i] < large and arr[i] > second_large:
        second_large = arr[i]

print("Second Smallest:",second_small)
print("Second Largest:",second_large)
```

------------------------------------------------------------------------

## Q14. Sum of Max and Min

``` python
arr = [3,5,1,8,2]

max_val = arr[0]
min_val = arr[0]

for i in range(len(arr)):
    if arr[i] > max_val:
        max_val = arr[i]

    if arr[i] < min_val:
        min_val = arr[i]

print("Sum:", max_val + min_val)
```

------------------------------------------------------------------------

## Q15. Find Duplicate

``` python
arr = [1,3,4,2,2]

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i] == arr[j]:
            print("Duplicate:",arr[i])
            break
```

------------------------------------------------------------------------

## Q16. Most Frequent Element

``` python
arr = [1,3,2,1,4,1,2]

max_count = 0
most_freq = arr[0]

for i in range(len(arr)):
    count = 0

    for j in range(len(arr)):
        if arr[i] == arr[j]:
            count += 1

    if count > max_count:
        max_count = count
        most_freq = arr[i]

print("Most Frequent:",most_freq)
```

------------------------------------------------------------------------

## Q17. Missing Number in Array

``` python
arr = [1,2,4,5]
n = 5

for i in range(1,n+1):
    found = False

    for j in range(len(arr)):
        if arr[j] == i:
            found = True
            break

    if not found:
        print("Missing:",i)
```

------------------------------------------------------------------------

## Q18. Check Pair with Target Sum

``` python
arr = [2,7,11,15]
target = 9

found = False

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i] + arr[j] == target:
            found = True

if found:
    print("Pair Exists")
else:
    print("Pair Does Not Exist")
```

------------------------------------------------------------------------

## Q20. Plus One

``` python
digits = [1,2,9]

carry = 1

for i in range(len(digits)-1,-1,-1):
    
    digits[i] = digits[i] + carry
    
    if digits[i] == 10:
        digits[i] = 0
        carry = 1
    else:
        carry = 0
        break

if carry == 1:
    digits = [1] + digits

print(digits)
```

------------------------------------------------------------------------

## Q21. Rotate Array by K

``` python
array = [1, 2, 3, 4, 5]
k=2
def rotate_array(arr, k):
    k = k % len(arr)
    return arr[-k:] + arr[:-k]
```
