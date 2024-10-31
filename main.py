# Donovan Farley-Freeman
# 10/31/24
# Creating a recursive sorting function



def merge_sort(num_list):
  if len(num_list) == 1:
    left = num_list
    right = []
  else:
    left = num_list[0:len(num_list)//2]
    right = num_list[len(num_list)//2:len(num_list)]
    left = merge_sort(left)
    right = merge_sort(right)
  
  num_listR = []
  while (len(left) != 0) and (len(right) != 0):
    if left[0] >= right[0]:
      num_listR.append(right[0])
      right.remove(right[0])
    else:
      num_listR.append(left[0])
      left.remove(left[0])
  
  if len(left) == 0:
    for num in range(len(right)):
      num_listR.append(right[num])
  else:
    for num in range(len(left)):
      num_listR.append(left[num])


  return num_listR



def main():
    nums1 = [6,2,5,8,3,4,8]
    nums2 = [1,2,3,4,5,6,7,8]
    nums3 = [8,2,6,0,1,3]

    for num_list in [nums1, nums2, nums3]:
        print(f"\nOriginal: {num_list}")
        new = merge_sort(num_list)
        print(f"Sorted: {new}\n")

if __name__ == "__main__":
    main()