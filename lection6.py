# numlist = ['1', '2', '3']
# separator = ''
# print(separator.join(numlist))


# a = ['hi', 'world']
# b = ' '
# c = b.join(a)
# print(c)

# a = "aijan"
# b = "sanjar"
# c = ''.join(a + ' ' + b)
# print(c)

# def reverse_seq(n):
#     return [i for i in range(n, 0, -1)]     #codewars
# import random

# def rps(user1, user2):
# #     beats = {'rock': "scissers", 'scissers': "paper", 'paper': ""}
# total = 0

#
# while total <= 50:
#     chislo = int(input("number:  "))
#     total += chislo
# print(f"the total num is {total}  ")


def solution(A, B):
    survivals = 0
    stack = []
    for i in range(len(A)):
        if B[i] == 0:
            while(len(stack)) != 0:
                if stack[-1] > A[i]:
                    break
                else:
                    stack.pop()
            else:
                survivals += 1
        else:
            stack.append(A[i])
    survivals += len(stack)

    return survivals






