#!/usr/bin/env python
# coding: utf-8

# In[6]:


num = int(input("Enter the number: "))
sum1 = 0
while num > 0:
    sum1 = sum1 + num
    num = num - 1
print(f"The sum of n natural numbers is: {sum1}")


# In[22]:


n = int(input("Enter the number: "))
if n > 1:
    for i in range(2, n):
        if (n%i == 0):
            print("Entered no. is not a prime no.")
            break
    else:
        print("Entered no. is a prime no.")
            
else:
    print("No. is not a prime no.")

