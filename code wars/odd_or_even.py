from abc import abstractmethod


def mine(number):
    # if number/2 has a of 0 then
    if number % 2 == 0:
        # The Return will exit the function
        return "Even"
    # we cane return odd, since it did not return even, leave out else
    return "Odd"




# This can be condensed because
# - An if statment will pass if a number is passed in exept one so 1 as a remander will pass
#   - this we can skip == 0 or == 1
# - Pthon also has a Ternary Operator
#   - The syntax of this is "[if_true_exe] if [expression] else [if_false_exe]"
#   - This means we can fit a if and else statment on one line as long as their is only one expression


def best(number):
    return "Odd" if number % 2 else "even"






for x in range(0,11):
    print("%d:%s" %(x, best(x)))
