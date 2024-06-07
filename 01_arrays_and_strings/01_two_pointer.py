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

#set logging level at debug
log.basicConfig(level=log.INFO)

class TwoPointers:

    #Constructor method
    def __init__(self, name):
        self.name = name

    #Utility method for print decorators
    def separator_block(self):
        log.info("-" * 50)

    # Test if two strings are palindrome
    def is_palindrome(self, input_string : str) -> bool:
        log.info("Started is_palindrome method")

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
        log.info("End of is_palindrome method")
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
    def check_for_target_sum(self, arr1 : list[int],
                              target_sum : int) -> bool:
        log.info("Started check_for_target_sum method")
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
        log.info("End of check_for_target_sum method")    
        return False

    '''
    Below function defines a combined sorted array from two iterales.
        * If we apendnd both the arrays and sort it will be
          O((n+m)*(log(m+n)) time complexity
        * If we use two pointer it will be O(n+m) time and O(1)
          space complexity.
    '''
    def combine_sorted_array(self, arr1 : list[int],
                              arr2 : list[int]) -> list[int]:
        log.info("Started combine_sorted_array method")
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

        log.info("End of combine_sorted_array method")
        return sorted_list        

def test_class_methods():
    #initialize TwoPointers class
    two_pointer = TwoPointers("Hello")
    
    #separator block
    two_pointer.separator_block()

    #Call method to check palindrome
    input_str = input("please enter string to check if it's palindrome : ")
    flag = two_pointer.is_palindrome(input_str)
    log.info(f"{input_str} is a palindrome : {flag}")

    #separator block
    two_pointer.separator_block()

    #Test target_sum method
    int_list = [1, 2, 4, 6, 8, 10, 12, 15, 19]
    target_sum = int( input("Please enter target_sum : ") )
    #call method to check target sum acheived in list of integers
    result = two_pointer.check_for_target_sum(int_list, target_sum)
    log.info(f"The target sum achieved : {result}")

    #separator block
    two_pointer.separator_block()   

    #calling combine sorted array method
    list1 = [1, 5, 8, 18]
    list2 = [2, 6, 7, 9, 17, 25, 27, 30]

    sorted_list_arr = two_pointer.combine_sorted_array(list1, list2)
    print( f"Sorted list is : {sorted_list_arr}" )

if __name__ == "__main__":
    test_class_methods()