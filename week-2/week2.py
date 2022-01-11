


def calculate(min,max):
    sum1 = max - min
    sum1 +=1
    test = 0
    allsum=[]
    for i in range(sum1):
        test = min + i
        allsum.append(test)
        wow = sum(allsum)
    print(wow)

calculate(1,3)
calculate(4,8)


def avg(data):
    count = data["count"]
    allsalary = 0
    for i in range(count):
        salary =  data["employees"][i]["salary"]
        allsalary = allsalary + salary
    allsalary =allsalary / count
    print(allsalary)


avg({
    "count":3,
    "employees":[
        {
            "name":"John",
            "salary":30000
        },
        {
            "name":"Bob",
            "salary":60000
        },
        {
            "name":"Jenny",
            "salary":50000
        },
    
    ]

})

def maxProduct(nums):
    test = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            test.append(nums[i]*nums[j])
           
    
    one = 0 
    for i in range(len(nums)):
        del test[one]
        one = one + len(nums)
    print(max(test))
maxProduct([5,20,2,6])
maxProduct([10,-20,0,3])
maxProduct([-1,2])
maxProduct([-1,0,2])
maxProduct([-1,-2,0])

def towSum(nums,target):
 
    for i in range(len(nums)):
        for j in range(len(nums)-1):
            test = nums[i] + nums[j+1]
            if nums.index(nums[i]) == nums.index(nums[j+1]):
                continue
            if  test == target:
                return  nums.index(nums[i]) , nums.index(nums[j+1])
            
            
            
            
        
    
result=towSum([2,11,7,15],9)

print(result)

def maxZeros(nums):
    test = 0
    allsum = []
    for i in range(len(nums)):
        
        if nums[i] == 0 :
            test = test + 1  
            if i == len(nums)-1:
                allsum.append(test)

        if nums[i] == 1 :
            allsum.append(test)
            test = 0

    print(max(allsum))

maxZeros([0,1,0,0])
maxZeros([1,0,0,0,0,1,0,1,0,0])
maxZeros([1,1,1,1,1])
maxZeros([0,0,0,1,1])
