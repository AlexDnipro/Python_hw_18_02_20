
#https://www.codewars.com/kata/576bb71bbbcf0951d5000044
#Count of positives/sum of negatives
def count_positives_sum_negatives(arr):
    if len(arr) > 0:
        return [len([x for x in arr if x > 0]), sum([x for x in arr if x < 0])] 
    else:
        return []

#https://www.codewars.com/kata/53da6d8d112bd1a0dc00008b
#Reverse List Order
def reverse_list(l):
  'return a list with the reverse order of l'
  l.reverse()
  return l


#https://www.codewars.com/kata/514b92a657cdc65150000006
#Multiples of 3 or 5
def solution(number):
    return sum(set(x for x in range(3, number) if x % 3 == 0 or x % 5 == 0))