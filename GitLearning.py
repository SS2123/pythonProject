def sum_of_n_numbers(n):
    total = 0
    count = 1
    while count <= n:
        total += count
        count += 1
    return total
n = int(input("Enter the value of n: "))
print("The sum of the first", n, "numbers is:", sum_of_n_numbers(n))
 