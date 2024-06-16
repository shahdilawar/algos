'''
Sliding window technique
- This is used for problems involving subarrays.
- There is a very common group of problems involving subarrays that 
can be solved efficiently with sliding window. 

- First, the problem will either explicitly or implicitly define 
    criteria that make a subarray "valid". There are 2 components 
    regarding what makes a subarray valid:
    1. A constraint metric. This is some attribute of a subarray. 
    It could be the sum, the number of unique elements, the frequency 
    of a specific element, or any other attribute.
    2. A numeric restriction on the constraint metric. This is what 
    the constraint metric should be for a subarray to be considered 
    valid.
- Second, the problem will ask you to find valid subarrays in some way.
    The most common task you will see is finding the best valid 
    subarray. 
    The problem will define what makes a subarray better than another. 
    For example, a problem might ask you to find the longest valid 
    subarray.
    Another common task is finding the number of valid subarrays. 
'''

import logging as log

#set logging level at debug
log.basicConfig(level=log.INFO)

class SlidingWindow:

    #find the longest subarray with a sum less than or equal to k
    # work done in each loop iteration is amortized constant, 
    # so this algorithm has a runtime of O(n) and O(1) space complexity
    def find_longest_subarray_length(self, nums : list[int], sum : int) -> int:
        log.info("Started : find_longest_subarray_lenth method")
        log.info(f"list is : {nums}")

        # if empty list is passed, raise error
        if (len(nums)== 0):
            raise ValueError("List cant be empty")
        
        #initialize the left_index, right_index and long_window_length
        # to 0
        left_index = curr_sum = long_window_length = 0
                
        # Iterate the passed list / array.
        # Check which sub-array has the longest length
        for right_index in range( len(nums) ):
            #curr_sum is added to whole elements.
            log.debug(f"value is : {nums[right_index]}")
            log.debug(f"right index is : {right_index}")
            curr_sum += nums[right_index]

            # Check if curr_sum has exceeded sum
            # Then shrink the sliding window by removing elements 
            # from left.
            while (curr_sum > sum):
                log.debug(f"curr_sum in while loop : {curr_sum}")

                #remove the left element from sliding window 
                curr_sum -= nums[left_index]
                #increment to next element
                left_index += 1

                if (left_index <= right_index):
                    log.debug(f"value is : {nums[left_index]}")
                    log.debug(f"left index is : {left_index}")

            
            long_window_length = max( long_window_length,
                                    right_index - left_index +1 )
            
        log.info("Ended : find_longest_subarray_lenth")
        return long_window_length
    
    # Method to identify the longest array length post zeroes flip. 
    # we can flip only one zero at a time. 
    # work done in each loop iteration is amortized constant, 
    # so this algorithm has a runtime of O(n) and O(1) space complexity    
    def flip_zeroes_subarray_length(self, binary_string : str) -> int:
        log.info("Started : flip_zeroes_subarray_length method")

        #check if array is not empty
        if ( len(binary_string) == 0 ):
            raise ValueError("List can't be empty")
        
        log.info(f"List is : {binary_string}")
        # initialize the variables
        zeroes_count = left_index = window_length = 0

        # Iterate through the list.
        # Check if the zeroes count in one sliding window is > 0, then
        # record the array length.
        # move the left index and re-size sliding window.
        for right_index in range( len(binary_string) ):
            # check if there is a zero
            if ( binary_string[right_index] == "0" ):
                zeroes_count += 1
            #check if count is > 1, then sliding window has to be reset
            # iterate from left to find the zero position
            # reset the counter to reset sliding window.
            while ( zeroes_count > 1 ):
                log.debug(f"counter increased to {zeroes_count}")
                log.debug(f"left index is : {left_index}")
                # check if we have moved to zero occurence, then reset
                if binary_string[left_index] == "0":
                    log.debug(f"Found preceeding zero position : {left_index}")
                    zeroes_count -= 1
                #iterate left_index
                left_index += 1
            
             # Compare the subarray sliding window length
             # and store in long_window_length
             # memorize sliding window length as (right-left+1)
            log.debug(f"zeroes_count is : {zeroes_count}")
            window_length = max( window_length, 
                                     right_index - left_index + 1)

        log.info("Ended : flip_zeroes_subarray_length method")
        return window_length
    
    #Given an array of positive integers nums and an integer k, 
    # return the number of subarrays where the product of all the 
    # elements in the subarray is strictly less than k.
    # work done in each loop iteration is amortized constant, 
    # so this algorithm has a runtime of O(n) and O(1) space complexity
 
    def find_subarrays_that_match(self, nums : list[int], 
                                  match_val : int) -> int:
        log.info("Started : find_subarrays_that_match method")
        # if match_val is <= 1, then no subarrays can exist.
        if ( match_val <= 1 ):
            return 0
        
        # if list is empty
        if (len(nums) == 0):
            raise ValueError("List cant be empty")
        
        #initialize the variables
        left_index = no_of_valid_sub_arrays = 0
        curr_sum = 1
        
        # Keep right index fixed and check if product of elements 
        # satisfy match value. if so find the numbe of subarrays from
        # left index. 
        for right_index in range(len(nums)):
            # multiply elements of list
            curr_sum *= nums[right_index]
            log.debug(f"curr_sum is : {curr_sum} ")
            # check if cur_sum exceeds match value
            while (curr_sum >= match_val):
                curr_sum //= nums[left_index]
                left_index += 1
            
            # Add the valid subarrays 
            no_of_valid_sub_arrays += right_index - left_index + 1
        
        log.info("Ended : find_subarrays_that_match method")
        return no_of_valid_sub_arrays

    # Given an integer array nums and an integer k, find the sum of 
    # the subarray with the largest sum whose length is k
    # The total for loop iterations is equal to n, where n is length
    # of nums. So this algorithm has a runtime of O(n) and O(1) space complexity
    def find_max_sum_in_fixed_sub_array(self , nums : list[int], 
                                        array_fixed_length : int) -> int:
        log.info("Started : find_max_sum_in_fixed_sub_array method")
        log.debug(f"List is : {nums}")
        if (len(nums) == 0):
            raise ValueError("List cant be empty")

        #initialize the variables.
        curr_sum = max_sum = 0
        # move to fixed length first.
        for i in range(array_fixed_length):
            curr_sum += nums[i]
        
        max_sum = curr_sum
        # iterate through the next range by sliding through window
        # length
        for i in range(array_fixed_length, len(nums)):
            log.debug(f" start index after initial move is : {i}")
            log.debug(f"remove index is : {i - array_fixed_length}")
            curr_sum = nums[i] - nums[i - array_fixed_length]

            #check the maximum value against each iter
            max_sum = max( max_sum, curr_sum)
            log.info("Ended : find_max_sum_in_fixed_sub_array method")
        return max_sum
    
    # Find a contiguous subarray whose length is equal to k that has 
    # the maximum average value and return this value. .
    def find_max_average(self, nums: list[int],
                          fixed_array_length : int) -> float:
        log.info("Started : find_max_average method")
        # Initialize the variables.
        max_average = curr_sum = 0
        
        # Iterate through to first range.
        for i in range(fixed_array_length):
            curr_sum += nums[i]   
        
        log.debug(f"curr_sum in first window is : {curr_sum}")
        #calculate the average for fixed length target window
        max_average = curr_sum / fixed_array_length
        log.debug(f"average after first iteration is : {max_average}")
        
        # Iterate through next sliding window by 
        # decrementing the left most value and adding the next one.
        for j in range( fixed_array_length, len(nums) ):
            # Add the next element and remove the previous first
            # element to sliding window
            curr_sum += ( nums[j] - nums[j - fixed_array_length] )
            log.debug(f"curr_sum in {j}, {j - fixed_array_length} window is : {curr_sum}")
            log.debug(f"average is : {max_average}")
            # check the maximum average by using max function.
            max_average = max(max_average, (curr_sum / fixed_array_length))
         
        log.info("Ended : find_max_average method")
        return max_average
    
    #Find the longest ones in input string.
    def find_longest_ones_in_list(self, nums: list[int], k: int) -> int:
        
        log.info("Started : find_longest_ones_in_list method")
        if ( len(nums) == 0 ):
            raise ValueError("List can't be empty")
        
        log.info(f"List is : {nums} ")

        # initialize the variable
        zeroes_count = left_index  = window_length = 0
        
        #Iterate till we get the zeroes       
        for right_index in range( len(nums) ):
            '''
            Check the occurence of zero and if so increment 
            the zeroes count.
            '''
            if ( nums[right_index] == 0 ):
                zeroes_count += 1
                
            while (zeroes_count > k):
                
                #check if we found zero
                if ( nums[left_index] == 0 ):
                    zeroes_count -= 1
                #move the left index
                left_index += 1
        
            window_length = max(window_length, 
                                right_index - left_index + 1)
        
        log.info("Ended : find_longest_ones_in_list method")
        
        return window_length

def test_class_methods():

    #Initialize the class
    sliding_window = SlidingWindow()

    #Test the find_longest_subarray_length
    num_list = [3, 1, 2, 7, 4, 2, 1, 1, 5]
    target_sum = 9
    print ("-" * 60)
    #result length
    result = sliding_window.find_longest_subarray_length(num_list,
                                                          target_sum)
    print(f"longest subarray length a sum less than or equal to {target_sum} is : {result}")

    print ("-" * 60)
    #test the zeroes length
    binary_str = "1101100111"
    zeroes_length = sliding_window.flip_zeroes_subarray_length(binary_str)
    print(f"zeroes max length : {zeroes_length}")

    print("-" * 60)
    #Test the valid subarrays method
    num_list = [10, 5, 2, 6]
    match_val = 100
    no_of_valid_arrays = sliding_window.find_subarrays_that_match(num_list, 
                                                                  match_val)
    print(f"no_of_valid_arrays is : {no_of_valid_arrays} ")

    print("-" * 60)
    #Test the max sum method
    num_list = [3, -1, 4, 12, -8, 5, 6]
    array_range = 4

    max_sum = sliding_window.find_max_sum_in_fixed_sub_array(num_list, 4)
    print(f"Max value in {num_list} is : {max_sum}")

    print("-" * 60)
    #Test the max average method
    nums = [1, 12, -5, -6, 50, 3]
    fixed_arr_len = 4
    #nums = [5]
    #fixed_arr_len = 1
    max_avg = sliding_window.find_max_average(nums, fixed_arr_len)
    print(f" maximum average in {nums} is : {max_avg}")

    print ("-" * 60)
    #test the longest ones length
    binary_list = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
    max_zeroes_to_flip = 3
    max_ones_arr_length = sliding_window.find_longest_ones_in_list(
                                binary_list, max_zeroes_to_flip)
    print(f"Ones max length : {max_ones_arr_length}")

if __name__ == "__main__":
    test_class_methods()

