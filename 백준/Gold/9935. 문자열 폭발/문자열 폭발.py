sentence = input()
burst = input()

# stack
stack = []
length = len(burst)


for i in range(len(sentence)):
    stack.append(sentence[i])
    if ''.join(stack[-length:]) == burst:
        del stack[-length:]

answer = ''.join(stack)

if not answer:
    print('FRULA')
else:
    print(answer)