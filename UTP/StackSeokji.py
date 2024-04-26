stack_R = input().split()
stack_S = input().split()
stack_T = input().split()

while stack_T:
    stack_S.append(stack_T.pop(0))

print(' '.join(stack_R))
print(' '.join(stack_S))
print(' '.join(stack_T))