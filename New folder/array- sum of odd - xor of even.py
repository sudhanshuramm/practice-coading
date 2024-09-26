#find the difference between the sum of the array of off index and XOR of element at even index


def arraysum(nums):
    sum1=0
    sum2=0
    for i in range(len(nums)):
        if i%2==0:
            sum2=sum2^nums[i]
           
        else:
            
             sum1=sum1+nums[i]
    return sum1-sum2

nums = list(map(int, input().split()))
print(arraysum(nums))
