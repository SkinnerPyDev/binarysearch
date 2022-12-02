def binar_search(l,target):
  start =0
  end = len(l)
  middle = 0
  steps = 0
  while start <= end:
    try:
      steps += 1
      print(f"Steps:{steps} {l[start:end+1]}")
      middle = (start + end) // 2
      if target == l[middle]:
        print(f"target {target} is found in {steps} steps")
        return middle
      if target < l[middle]:
        end = middle - 1
      else:
        start = middle + 1
    except IndexError:
      print(f'{target} is not in list')
      return -1

l = [2,4,6,44,3,55,67,38,52,58,25,24,8,46,88,446,7,56,56,7,6,]
l.sort()
target = 24
binar_search(l,target)