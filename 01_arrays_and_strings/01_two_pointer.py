'''
Two pointers is an extremely common technique used to solve array and 
string problems. 
It involves having two integer variables that both move along an 
iterable. 
This means we will have two integers, usually named something like
i and j, or left and right which each represent an index of the array
or string.
'''
import logging as log
from Utility_Module import utility_decorator

#set logging level at debug
log.basicConfig(level=log.INFO)

class TwoPointers:

    #Constructor method
    def __init__(self, name):
        self.name = name

    # Test if two strings are palindrome
    @utility_decorator
    def is_palindrome(self, input_string : str) -> bool:
        #left index initialized to start index of string
        left_index = 0
        #right index initialized to start index of string
        right_index = len(input_string) - 1
        '''
        Iterate till both pointers meet near center of string.
        This way the space complexity is cloe to O(1) as there are only 
        two integers and time complexity is close to O(n) the number
        of loops.
        ''' 
        while (left_index < right_index):
            #Info on characters at first and last index
            log.debug(f" Character at left index : {input_string[left_index]}")
            log.debug(f" Character at right index : {input_string[right_index]}")
            
            # check if characters match and if not return false
            if (input_string[left_index] != input_string[right_index]):
                return False
            
            #increment left pointer
            left_index += 1
            #decrement right pointer
            right_index -= 1
        
        #if we exit the loop then it means the characters on both
        #directions have matched. So return true.
        return True

    '''
    Below method checks if pair of integers in the passed array
    sum up to target.
        * Brute force method will be to iterate over all integers.
        *  Each number in the array can be paired with another number, 
            so this would result in a time complexity of O(exp(n)), where
            n is length of array.
        * We use two pointer technique to acheive O(1) space and 
          O(n) time complexity.
    '''
    @utility_decorator
    def check_for_target_sum(self, arr1 : list[int],
                              target_sum : int) -> bool:
        #check if list is empty raise error
        if ( len(arr1) == 0 ):
            raise ValueError("List cant be empty")
        
        #left index to be initialized to start index of list
        left_index = 0
        #right index to be initialized to end index of list
        right_index = len(arr1) - 1
        log.info(f"target sum is : {target_sum}")

        '''
        This algorithm uses O(1 space complexity and O(n)
        time complexity)
        '''
        #Use while loop to iterate
        while (left_index < right_index):
            #debug info of integers at first and last index
            log.debug(f"left side value : {arr1[left_index]}")
            log.debug(f"right side value : {arr1[right_index]}")
            
            #add up the value of integers at left amd right index.
            curr_sum = arr1[left_index] + arr1[right_index]
            log.info(f"current sum is : {curr_sum}")
            
            # check if value is equal to target_sum
            if ( curr_sum == target_sum ):
                return True
            
            # If they dont match need to check if curr_sum is greater
            # than target_sum and move the pointer from right side.
            if ( curr_sum > target_sum ):
                #decrement right index and move right pointer.
                right_index -= 1
            else:
                #increment left index and move left pointer.
                left_index += 1
        
        # if the passed target_sum does not add up to passed integers.
        return False

    '''
    Below function defines a combined sorted array from two iterales.
        * If we apendnd both the arrays and sort it will be
          O((n+m)*(log(m+n)) time complexity
        * If we use two pointer it will be O(n+m) time and O(1)
          space complexity.
    '''
    @utility_decorator
    def combine_sorted_array(self, arr1 : list[int],
                              arr2 : list[int]) -> list[int]:
        #initialize the indexes.
        arr1_index = arr2_index = 0
        #inititialize resultant sorted list
        sorted_list = []

        log.debug(f"arr1 list is : {arr1}")
        log.debug(f"arr2 list is : {arr2}")

        #Iterate both the lists till one gets exhausted. 
        #Then append the rest.
        while ( arr1_index < len(arr1) and 
               arr2_index < len(arr2) ):
            '''
            compare both lists to find which element is lesser
            at that particular index and add it to list and increment
            that index.
            '''
            if ( arr1[arr1_index] < arr2[arr2_index] ):
                
                log.debug(f"arr1 element is : {arr1[arr1_index]}")
                log.debug(f"arr2 element is : {arr2[arr2_index]}")

                log.info(f"Appending {arr1[arr1_index]}")
                sorted_list.append(arr1[arr1_index])
                arr1_index += 1
            else:
                log.info(f"Appending {arr2[arr2_index]}")
                sorted_list.append(arr2[arr2_index])
                arr2_index += 1
        
        #If arr1 still has elements append them
        while ( arr1_index < len(arr1) ):
            log.info(f"Appending {arr1[arr1_index]}")
            sorted_list.append(arr1[arr1_index])
            arr1_index += 1

         #If arr2 still has elements append them
        while ( arr2_index < len(arr2) ):
            log.info(f"Appending {arr2[arr2_index]}")
            sorted_list.append(arr2[arr2_index])  
            arr2_index += 1

        return sorted_list        

    '''
    test if string is in sub-sequence method.
        * we need to check if the characters of "s" appear in the same
        order in "t", with gaps allowed. 
        * s is a subsequence of t if we can "find" all the letters of s,
        which means that i == s.length at the end of the algorithm
        * Using two pointers it will be O(1) space and O(n) time complexity.
    '''
    @utility_decorator
    def is_subsequence(self, source_str : str, target_str : str) -> bool:
        # print source and target strings
        log.debug(f"Source string is : {source_str}")
        log.debug(f"Target string is : {target_str}")

        source_str_index = target_str_index = 0

        '''
        1. Iterate through both string chars.
        2. if source_str[source_str_index] matches increment index.
        3. post execution if s has moved all the way to end then 
            we found a match.
        '''
        while ( source_str_index < len(source_str) 
            and target_str_index < len(target_str) ):
            #logging the characters
            log.debug(f" source_str char at {source_str_index} is : {source_str[source_str_index]}")
            log.debug(f" target_str char at {target_str_index} is : {target_str[target_str_index]}")

            #check for match
            if ( source_str[source_str_index] == target_str[target_str_index] ):
                source_str_index += 1
            #increment target str ir-respective of match.
            target_str_index += 1

        #if source_str has traversed its entire lenth it means that
        #subsequence condition has been acheived.
        return (source_str_index == len( source_str ))

    '''
        * This method will reverse the string.
        * The input string is given as an array of characters s.
        * The challenge is to modify input array with o[1] extra memory
    '''
    @utility_decorator
    def reverse_string(self, source_str : list[str] ) -> str:
        log.debug("source string is : {source_str}")

        #raise error if list is empty.
        if ( len(source_str) == 0):
            raise ValueError("Source string cannot be empty")
        
        i = 0
        j = len(source_str) - 1

        #Iterate through the loop and assign
        while (i < j):            
            source_str[i], source_str[j] = source_str[j], source_str[i]
            log.debug(f"char at {i} is : {source_str[i]}")
            log.debug(f"char at {j} is : {source_str[j]}")
            i += 1
            j -= 1
 
        return source_str

    '''
    Squares of a Sorted Array
        * Given an integer array nums sorted in non-decreasing order, 
        return an array of the squares of each number sorted in 
        non-decreasing order.
        * Squaring each element and sorting the new array is very 
        trivial, could you find an O(n) solution using a different 
        approach?
    '''
    @utility_decorator
    def squares_of_sorted_array(self, input_arr : list[int]) -> list[int]:
        '''
        * Use the two pointer approach to square compare and
          move the pointers.
        '''
        log.info(f"input list is : {input_arr}")

        # #moderate approach
        # #Time complexity is O(n log(n))
        # #Space complexity is O(n)
        # log.info("Ending squares_of_sorted_array method : ")
        # #use list comprehension and sorted
        # return sorted( x*x for x in input_arr)

        #check for list emptiness
        if ( len(input_arr) == 0):
            raise ValueError("List cant be empty")
        
        input_arr_len = len(input_arr)
        log.debug(f"i/p array length : {input_arr_len}")
        left_index = 0
        right_index = input_arr_len - 1
        
        #initializing sorted list with 0 of input array length.
        squares_of_sorted_list = [0] * input_arr_len
        log.debug(f"sorted array length : {len(squares_of_sorted_list)}")

        '''
        The key is non-decreasing numbers. it means negative
        and positive numbers in the list will be in kind of asc 
        sorted in their context.
        * Lets do a abs(left) to abs(right) comparison and place 
        the larger value in last cell of new list. 
        * This will provide the sorted list.
        * use for loop to iterate from back till 0 and step by -1.
        '''
        for i in range(input_arr_len - 1, -1, -1):
            
            log.debug(f"left element : {abs(input_arr[left_index])}")
            log.debug(f"right element : {abs(input_arr[right_index])}")

            #Compare absolute values at left and right pointers
            if ( abs(input_arr[left_index]) 
                < abs(input_arr[right_index]) ):
                #assign the right index value to be squared
                square = input_arr[right_index]
                # move the right pointer
                right_index -= 1
            else:
                #assign the left index value to be squared
                square = input_arr[left_index]
                #move the left pointer
                left_index += 1
            
            #Place the value in square sorted list
            squares_of_sorted_list[i] = square * square
        
        return squares_of_sorted_list

        

                
def test_class_methods():
    #initialize TwoPointers class
    two_pointer = TwoPointers("Hello")

    #Call method to check palindrome
    input_str = input("please enter string to check if it's palindrome : ")
    flag = two_pointer.is_palindrome(input_str)
    log.info(f"{input_str} is a palindrome : {flag}")

    #Test target_sum method
    int_list = [1, 2, 4, 6, 8, 10, 12, 15, 19]
    target_sum = int( input("Please enter target_sum : ") )
    #call method to check target sum acheived in list of integers
    result = two_pointer.check_for_target_sum(int_list, target_sum)
    log.info(f"The target sum achieved : {result}")

    #calling combine sorted array method
    list1 = [ 1, 5, 8, 18 ]
    list2 = [ 2, 6, 7, 9, 17, 25, 27, 30 ]

    sorted_list_arr = two_pointer.combine_sorted_array(list1, list2)
    print( f"Sorted list is : {sorted_list_arr}" )

    #Test sub sequence method
    source_str = input("Please enter source string : ")
    target_str = input("Please enter target string : ")
    result = two_pointer.is_subsequence(source_str, target_str)
    print(f"Is {source_str} is a subsequence of  {target_str} : {result}")

    source_str_list = ["H", "a", "n", "n", "a", "h"]
    reversed_list = two_pointer.reverse_string(source_str_list)
    print(f" Reversed list is : {reversed_list}")

    input_list = [-7, -3, 2, 3, 11]
    sorted_list = two_pointer.squares_of_sorted_array(input_list)
    print(f"Squared list is : {sorted_list}")

if __name__ == "__main__":
    test_class_methods()