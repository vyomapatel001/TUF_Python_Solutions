def insert_at_bottom(stack, item):
    """
    Insert an item at the bottom of the stack.
    
    :param stack: List representing the stack.
    :param item: Item to be inserted at the bottom.
    :return: None, the stack is modified in place.
    """
    if not stack:
        stack.append(item)
        return
    
    # Remove the top element
    top = stack.pop()
    
    # Recursively insert the item at the bottom
    insert_at_bottom(stack, item)
    
    # Push the top element back onto the stack
    stack.append(top)

def reverse(stack):
    """
    Reverse the order of elements in a stack using recursion.
    
    :param stack: List representing the stack to be reversed.
    :return: None, the stack is modified in place.
    """
    if not stack:
        return
    
    # Remove the top element
    top = stack.pop()
    
    # Reverse the remaining stack
    reverse(stack)
    
    # Insert the removed element at the bottom
    insert_at_bottom(stack, top)

if __name__ == "__main__":
    stack = [1, 2, 3, 4, 5]
    print("Original Stack:", stack)
    
    reverse(stack)
    
    print("Reversed Stack:", stack)

# This code defines two functions: insert_at_bottom and reverse.
# The insert_at_bottom function inserts an item at the bottom of a stack, while the reverse function reverses the order of elements in a stack using recursion.
# The main block demonstrates the usage of these functions by reversing a sample stack.

# Time Complexity: O(n^2) in the worst case due to the recursive calls and stack operations.
# Space Complexity: O(n) for the recursion stack and the stack itself.