def second_largest(lst):
  if not lst or len(lst) < 2:
    return None

  largest = None
  second = None

  for num in lst:
    if largest is None or num > largest:
      largest = num

  for num in lst:
    if num != largest:
      if second is None or num > second:
        second = num 
  
  return second
