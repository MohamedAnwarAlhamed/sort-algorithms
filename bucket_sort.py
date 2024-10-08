def bucket_sort(arr, num_buckets=10):
  if not arr:
    return arr
    
  # Step 1: Create buckets based on num_buckets argument
  buckets = [[] for _ in range(num_buckets)]

  # Step 2: Define factors used to distribute elements into the buckets
  min_value = min(arr)
  max_value = max(arr)
  range_value = max_value - min_value
  
  # Avoid division by zero when all elements are the same
  if range_value == 0:
      return arr

  # Step 3: Calculate the bucket index for each element based on element value and previous factors 
  for elem in arr:
    # Normalizing the value to fit the bucket range
    index = int((elem - min_value) / range_value * (num_buckets - 1))
    index = min(index, num_buckets - 1)  # Prevent index out of range
    buckets[index].append(elem)
    
  # Step 3: Sort each bucket and concatenate the results.
  arr = [item for bucket in buckets for item in sorted(bucket)]

  return arr

arr = [6, 56, 1, 32, 0, 9, 2, 23, 0]
print("Sorted array:", bucket_sort(arr))
