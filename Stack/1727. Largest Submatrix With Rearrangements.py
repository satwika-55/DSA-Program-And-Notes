""
1. Just utilising the similar concepts of : 85.Maximal Reactangle to get maximum no of consecutive 1's then
2. Sort in reverse order after each row(means we are just merging the bigger heights together) 
3. Calculate the maximum rectangle after sorting (by finding height & width). 

Time : O(row * col * log(col)

"""

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        max_area = 0
        
        # Tracks running consecutive vertical heights of '1's for each column
        heights = [0] * n
        
        for i in range(m):
            for j in range(n):
                # Accumulate heights if cell is 1, reset to 0 if it breaks
                heights[j] = heights[j] + 1 if matrix[i][j] == 1 else 0
            
            # Create a copy and sort heights in descending order 
            # This simulates shifting the best columns next to each other
            sorted_heights = sorted(heights, reverse=True)
            
            # Calculate the area row by row using the sorted column bars
            for k in range(n):
                # Height is restricted by the shortest column in the sorted group
                curr_height = sorted_heights[k]
                # Width is the number of columns processed so far
                curr_width = k + 1
                
                max_area = max(max_area, curr_height * curr_width)
                
        return max_area


# Method 2 :
"""
Instead of re-sorting all 'n' columns from scratch using O(n *log n) sort(), we can construct the new sorted column order in linear O(n) time:
    Iterate through the previous row's sorted column list.If a column has height > 0 in the current row, append it to a non_zeros list. 
    Because we process them in their previously sorted order, adding +1 keeps them in perfectly sorted order!
    If a column has height == 0, append it to a zeros list.Concatenate non_zeros + zeros to get the new sorted column indices!

Time : O(row * col)
"""

from typing import List

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        max_area = 0
        
        # heights[j] stores running consecutive 1s ending at current row for column j
        heights = [0] * n
        
        # Maintain column indices ordered by their height descending.
        # Initially [0, 1, ..., n-1] is fine since all heights start at 0.
        sorted_cols = list(range(n))
        
        for i in range(m):
            # Step 1: Update heights for the current row
            for j in range(n):
                heights[j] = heights[j] + 1 if matrix[i][j] == 1 else 0
            
            # Step 2: Re-order column indices in O(n) without sorting.
            # Traverse columns in their PREVIOUS sorted order.
            next_sorted_cols = []
            zeros = []
            
            for col in sorted_cols:
                if heights[col] > 0:
                    # Column extended (+1); preserves previous relative sorted order
                    next_sorted_cols.append(col)
                else:
                    # Column broke (reset to 0); pushed to the end
                    zeros.append(col)
                    
            # Combine non-zero heights (tallest to shortest) with zero heights at the end
            sorted_cols = next_sorted_cols + zeros
            
            # Step 3: Calculate max area using the O(n) updated order
            for k in range(n):
                col = sorted_cols[k]
                curr_height = heights[col]
                curr_width = k + 1
                
                # Area = height of the shortest column in the group * number of columns
                max_area = max(max_area, curr_height * curr_width)
                
        return max_area
