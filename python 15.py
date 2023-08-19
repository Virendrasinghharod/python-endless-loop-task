#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import threading

def a():
    count = 0
    while count < 5:
        print("a:", count)
        count += 1

def b():
    while True:
        print("b: Running infinitely")

def lw():
    # Create threads for functions a and b
    thread_a = threading.Thread(target=a)
    thread_b = threading.Thread(target=b)

    # Start both threads
    thread_a.start()
    thread_b.start()

    # Wait for both threads to finish
    thread_a.join()
    thread_b.join()

lw()
print("Both functions have finished.")

