/*
Given an integer array nums, return the length of the longest strictly increasing 
subsequence
.

 

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
 

Constraints:

1 <= nums.length <= 2500
-104 <= nums[i] <= 104
 

Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?
*/


function lengthOfLIS(nums: number[]): number {
    let result: number[]  = [];
    for(let i=0; i < nums.length; i++){
        if (i == 0) {
            result.push(nums[i]);
        } else {
            if (result[result.length - 1] < nums[i]) {
                result.push(nums[i]);
            } else {
                let lowerBoundIndex = getLowerBound(result, nums[i]);
                result[lowerBoundIndex] = nums[i];
            }
        }

    }
    return result.length;
    
};

function getLowerBound(arr: number[], target: number): number {
    let low: number = 0;
    let high: number = arr.length -1; 
    let ans: number = arr.length;
    while (low <= high) {
        let mid = Math.floor((low + high) / 2);
        if (arr[mid] >= target) {
            ans = mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }
    return ans;
};