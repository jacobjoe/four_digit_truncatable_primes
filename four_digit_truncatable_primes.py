""" Four digit Truncatable prime numbers"""
# import time module for calculate time of calculation
import time
start = time.time()
# set initial four digit number
num = 1000
lst_left_right = []
lst_right_left = []
# while loop for loop below five digit number
while num < 10000:
    # check whether num is prime or not
    for i in range(2, num):
        if num % i == 0:
            num += 1
            break
    # if prime, else part takes place from left to right
    else:
        num_str = str(num)
        # take 2nd, 3rd and 4th number and check prime
        three = num_str[1]+num_str[2]+num_str[3]
        num_three = int(three)
        for i in range(2, num_three):
            if num_three % i == 0:
                num += 1
                break
        else:
            # take 3rd and 4th number and check prime
            two = num_str[2]+num_str[3]
            num_two = int(two)
            for j in range(2, num_two):
                if num_two % j == 0:
                    num += 1
                    break
            else:
                # take 4th number and check prime
                one = num_str[3]
                num_one = int(one)
                if num_one == 1:
                    lst_left_right.append(num)
                    num += 1
                elif num_one > 1:
                    for i in range(2, num_one):
                        if num_one % i == 0:
                            num += 1
                            break
                    else:
                        lst_left_right.append(num)
                        num += 1

# check Truncatable primes from right to left
num = 1000
# while loop for loop below five digit
while num < 10000:
    for i in range(2, num):
        if num % i == 0:
            num += 1
            break
    # if prime, else part takes place from right to left
    else:
        num_str = str(num)
        # take 1st 2nd and 3rd number and check prime
        three = num_str[0]+num_str[1]+num_str[2]
        num_three = int(three)
        for i in range(2, num_three):
            if num_three % i == 0:
                num += 1
                break
        else:
            # take 1st and 2nd number and check prime
            two = num_str[0]+num_str[1]
            num_two = int(two)
            for j in range(2, num_two):
                if num_two % j == 0:
                    num += 1
                    break
            else:
                # take 1st number and check prime
                one = num_str[0]
                num_one = int(one)
                if num_one == 1:
                    lst_right_left.append(num)
                    num += 1
                elif num_one > 1:
                    for i in range(2, num_one):
                        if num_one % i == 0:
                            num += 1
                            break
                    else:
                        lst_right_left.append(num)
                        num += 1
# lst_3 for select number which is in both appended list
lst_3 = []
for i in lst_left_right:
    if i in lst_right_left:
        lst_3.append(i)
print("There are", len(lst_3), '"Truncatable primes" in four digit natural numbers ')
for i in lst_3:
    print(i)
print("Sum of all Truncatable primes is", sum(lst_3))
end = time.time()
print("Time :", end - start)
