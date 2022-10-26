def sum_to(n):
   sum = 0

   for val in range(n+1):
      sum += val

   return sum


def largest(numbers_list):
   return max(numbers_list)


def occurrences(str1, str2):
   return str1.count(str2)