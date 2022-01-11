function calculate(min,max){
        const reducer = (previousValue, currentValue) => previousValue + currentValue;
        var sum1 = max - min
        
        var test = 0
        var sllsum= new Array()
        for(var i = 0 ; i<=sum1;i++){
                
                test = min + i ;
                sllsum.push(test)
               
        }
        alert(sllsum.reduce(reducer))
}

calculate(1,3);
calculate(4,8);


function avg(data){
        
        var count = data.count

        allsalary = 0
        for(var i =0; i <= count-1;i++){
                var salary = data.employees[i].salary
                allsalary = allsalary + salary
        }
        allsalary = allsalary / count
        alert(allsalary)
}
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

function maxProduct(nums){
        
        var text = new Array()

        for(var i = 0;i <=nums.length-1;i++){
                for(var j = 0;j <=nums.length-1;j++){
                        text.push(nums[i]*nums[j])
                }
        }

        var one = 0 
        var alltime = nums.length
     
        for(var i = 0;i <=nums.length-1;i++){
                delete text[one];
                one = one + alltime+1;
               
        }
              var myArrayNew = text.filter(function (value) {
                return value != null
        });
       

        alert( Math.max(...myArrayNew) )
    
}

maxProduct([5,20,2,6])
maxProduct([10,-20,0,3])
maxProduct([-1,2])
maxProduct([-1,0,2])
maxProduct([-1,-2,0])


function twoSum(nums, target){
        var test = 0
        var nums1 = nums
        var wow = new Array()
        nums.forEach(function(numsitem, numsindex, array) {
                nums1.forEach(function(nums1item, nums1index, array) {
                
                if (numsindex !=nums1index){
                        test = numsitem+nums1item
                        
                }
                if(test==target){
                
                        
                        wow.push(numsindex )
                       
                }
                

        });
        });
         
                       return wow

        
        }


let result = twoSum([2,11,7,15],9)
console.log(result)

function maxZeros(nums){
        var test = new Array()
        var text = 0 
        for(var i = 0;i<=nums.length;i++){
                
                if(nums[i] == 0){
                        text = text+1
                        if(i==nums.length-1){
                                test.push(text)
                        }
                }
                if(nums[i] == 1){
                        test.push(text)
                        
                        text = 0
                       
                }
              
                
        }
        alert( Math.max(...test) )
                
}       
maxZeros([0,1,0,0]);
maxZeros([1,0,0,0,0,1,0,1,0,0]);
maxZeros([1,1,1,1,1]);
maxZeros([0,0,0,1,1]);
