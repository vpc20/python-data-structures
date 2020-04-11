

# stack
stack_list = []

# push data
stack_list.append('Python')
stack_list.append('Ruby')
stack_list.append('Java')
print(stack_list)

if stack_list:
    print('Stack contains data')
else:
    print('Stack is empty')

# pop data
stack_list.pop()
print(stack_list)
stack_list.pop()
print(stack_list)
stack_list.pop()
print(stack_list)

if stack_list:
    print('Stack contains data')
else:
    print('Stack is empty')


# queue
queue_list = []

# enqueue
queue_list.append('Intellij')
queue_list.append('Eclipse')
queue_list.append('Netbeans')
print(queue_list)

#dequeue
del queue_list[0]
print(queue_list)
del queue_list[0]
print(queue_list)
del queue_list[0]
print(queue_list)


