#two pointer
#take minimum of off left and right pointer
#min(L,R) -h[i] => gives the area of water each column holds

#solution 1
# for every single position to know how much water we can trap at index,i
# we need to know max left and right height of every single position
#make array to store this calculation
#scan through the array
#calculate every single maxLeft position and maxRight position in different arrays
# then take min of maxleft and maxright, allows us to know how much water we can trap
#after the calculations do this: min(L,R) - h[i] > 0 
#if equal to or less than zero no water is trapped
#sum the values at min array
#memory complexity: O(n)


