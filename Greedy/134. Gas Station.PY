#Intuition first, coding next (Python, java and c++) and time complexity analysis at the end.

# Intuition : 

'''
After reading the problem statement, we find that we need an index from where we can start our journey and complete the circuit.
If any index doesnt work, we need to return -1 . 

The place to start from will be the place where we can attain the maximum gas at the initial phase, so that we dont run out of gas at any point of time.

If at all , at any index our gas < 0 , the journey isnt possible and our chosen index is wrong. 

So, we understand that we need to start at a point where gas[i] > cost[i] and furthermore. 
If, at any point sum(gas[i]) < sum(cost[i]), any index from 0 to i isn't valid. 

This fact can be proven. 
Instead of providing prrofs, it would be better if you take a few examples and try to prove it to yourself.
This method will help you improve your edge case finding as well. 

So, now, we will keep a tarck of the sum of gas and cost. At any point, if the sum of cost exceeds the gas, we will set our ans to i+1. 
'''


# CODE : 

# PYTHON : 

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):  # not possible from any gas station
            return -1
        start= 0  # our ans
        total= 0  # store the total gas present
        # checking each gas station one by one, we can only choose any gas station if difference of gas[i] and cost[i]>= 0.
        for i in range(len(gas)):
            total+= gas[i]- cost[i]   # we are just taking diff
            if total < 0:  # means from this gas station 'start' we can't complete a circle
                start = i+1
                total = 0
        return start
    


# JAVA 



'''
class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int gasSum = 0, costSum = 0;
        for (int g : gas) gasSum += g;
        for (int c : cost) costSum += c;
        if (gasSum < costSum) return -1;

        int start = 0, total = 0;
        for (int i = 0; i < gas.length; i++) {
            total += gas[i] - cost[i];
            if (total < 0) {
                start = i + 1;
                total = 0;
            }
        }
        return start;
    }
}
'''


# C++ 



'''
class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        if (accumulate(gas.begin(), gas.end(), 0) < accumulate(cost.begin(), cost.end(), 0)) {
            return -1;
        }
        int start = 0, total = 0;
        for (int i = 0; i < gas.size(); i++) {
            total += gas[i] - cost[i];
            if (total < 0) {
                start = i + 1;
                total = 0;
            }
        }
        return start;
    }
};
'''



# TIME COMPLEXITY :

# -> The time complexity is just 0(n) as we are iterating through the gas and cost arrays once.

# SPACE COMPLEXITY :

# -> The space complexity is O(1) as we are not using any extra space except for a few variables.






