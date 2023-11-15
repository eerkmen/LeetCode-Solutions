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

#solution 2
#two pointer
#end points can't contain any water
#maxL, maxR keeps track the max so far
#choose the one that has smaller max value
#shift the smaller one
#if Left pointer is incremented compare the left index to the maxL. if maxL-L!>0 it can't contain water
#if maxL-L>0 it contains water the amount of result 
#time complexity: O(n)
#memory complexity: without using extra memory

class Solution:
    def trap(self, height: List[int]) -> int:
        
        if not height: return 0

        L, R = 0, len(height) - 1
        leftMax, rightMax = height[L], height[R]
        res = 0

        while L < R:
            if leftMax < rightMax:
                L += 1
                leftMax = max(leftMax, height[L])
                res += leftMax - height[L]
            else:
                R -= 1
                rightMax = max(rightMax, height[R])
                res += rightMax - height[R]
        return res
