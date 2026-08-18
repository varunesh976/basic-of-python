from collections import deque


def is_palindrome(a):
    dq = deque()

    for ch in a:
        if ch.isalnum():
            dq.append(ch.lower())

    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False

    return True


a = input("Enter a string: ")

if is_palindrome(a):
    print("Palindrome")
else:
    print("Not a Palindrome")
