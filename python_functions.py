def sum_to(n):
   sum = 0

   for val in range(n+1):
      sum += val

   return sum


def largest(numbers_list):
   return max(numbers_list)


def occurrences(str1, str2):
   return str1.count(str2)


def product(*numbers):
   prod = 1

   for num in numbers:
      prod *= num
   
   return prod


print(sum_to(10))

print(largest([2, -5, 28, 16]))

print(occurrences("chicky-pea, chicky-dee, supa free", "chi"))

print(product(-3, 2, 10))