#sorted in ascending order
#in-place alogrithm
#first unique value in the first position
#second unique value in second postion...etc

#two-pointer method
#initialize both pointers at the second value
#compare right pointer from the previous value
#if equal increment right pointer by 1
#left pointer stays 
#if right pointer not equal to the previous value 
#overwrite the value at the left pointer with the right pointer value
#increment left and right pointer by 1
#result= return left pointers index after right pointer goes out of bounds