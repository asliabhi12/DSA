class Solution {
    public int trap(int[] height) {
        int n = height.length;
        int count = 0;
        
        int leftPointer = 0, rightPointer = n - 1;
        
        int maxLeft = height[leftPointer], maxRight = height[rightPointer];
        
        while(leftPointer < rightPointer){
            if(maxLeft <= maxRight){
                leftPointer++;
                maxLeft = Math.max(maxLeft, height[leftPointer]);
                int temp = maxLeft - height[leftPointer];
                count += temp < 0 ? 0 : temp;
            }
            else{
                rightPointer--;
                maxRight = Math.max(maxRight, height[rightPointer]);
                int temp = maxRight - height[rightPointer];
                count += temp < 0 ? 0 : temp;
            }
        }
        return count;
    }
}