# Intuition first, code next ( Python, Java and C++ ) and time complexity analysis at the end.

# INTUITION : 

'''
We need to merge the intervals into the minimum number of intervals such that no two intervals overlap.
To do this, we can sort the intervals based on their start times and then iterate through them, merging overlapping intervals as we go.

We will add the non-overlapped intervals into an result arry , which we are going to return at the last. 

Initially, the first array will be added to the result array.

Then onwards, we will compare the endTime of the last interval in the result array with the startTime of the current interval.
If the startTime of the current interval is greater than the endTime of the last interval in the result array, it means the intervals are non-overlapping, and we can add the current interval to the result array.

Also, if the startime is equal to, or less than the endtime of the previous, then it means they are overlapping, which means we cant add the current interval into the result.

But, here's a catch, which many might miss - don't forget to update the endtime of the previous intervals with the maximum of current endtTime and previous endTime.

After the iteration, we will return the result array which will contain the merged intervals.
'''

# CODE : 

# PYTHON : 

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort()
        prev = -1 
        res = []
        for i in range(n):
            if intervals[i][0] > prev :
                res.append([intervals[i][0],intervals[i][1]])
                prev = intervals[i][1]
            elif res :
                res[-1][1] = max(res[-1][1],intervals[i][1])
                prev = res[-1][1]
        return res

        

# JAVA : 


'''
class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> a[0] - b[0]);
        List<int[]> res = new ArrayList<>();
        int prev = -1;
        for (int i = 0; i < intervals.length; i++) {
            if (intervals[i][0] > prev) {
                res.add(new int[]{intervals[i][0], intervals[i][1]});
                prev = intervals[i][1];
            } else {
                int[] last = res.get(res.size() - 1);
                last[1] = Math.max(last[1], intervals[i][1]);
                prev = last[1];
            }
        }
        return res.toArray(new int[res.size()][]);
    }
}

'''



# C++ : 



'''
class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end());
        vector<vector<int>> res;
        int prev = -1;
        for (int i = 0; i < intervals.size(); i++) {
            if (intervals[i][0] > prev) {
                res.push_back({intervals[i][0], intervals[i][1]});
                prev = intervals[i][1];
            } else {
                res.back()[1] = max(res.back()[1], intervals[i][1]);
                prev = res.back()[1];
            }
        }
        return res;
    }
};

'''




# TIME COMPLEXITY :

'''
-> Sorting the array = 0(nlogn)
-> Iterating through the array = O(n)
-> Overall time complexity = O(nlogn)
'''

# SPACE COMPLEXITY :

'''
-> O(n) for the result array.
-> O(1) for the variables used.
-> Overall space complexity = O(n)
'''
