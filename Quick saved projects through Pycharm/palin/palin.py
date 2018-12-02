# finding the next palindrome of a given number
def mirror(new_left_half, num_is_even=False):
    n = len(new_left_half)
    left_half = ''
    right_half = ''

    new_left_half = ''.join(new_left_half)

    if num_is_even:
        #
        left_half = new_left_half[:n]
        right_half = left_half[::-1]
        #
        # for i in range(n):
        #     left_half += new_left_half[i]
        #     right_half = new_left_half[i] + right_half

        return left_half + right_half

    else:
        #
        left_half = new_left_half[:n - 1]
        right_half = left_half[::-1]
        #
        # for i in range(n-1):
        #     left_half += new_left_half[i]
        #     right_half = new_left_half[i] + right_half

        return left_half + new_left_half[n - 1] + right_half


def increment_by_one(left_half):
    #
    left_half_string = ''.join(left_half)
    #
    # for i in range(len(left_half)):
    #     left_half_string += left_half[i]

    left_half_num = int(left_half_string) + 1

    return list(str(left_half_num))


def is_all_nines(num):
    num = ''.join(num)
    num = num.replace('9', '')

    if len(num) > 0:
        return False
    else:
        return True


def find_next_palindrome(num):
    if is_all_nines(num):
        n = len(num)
        palindrome = '1'
        palindrome += '0' * (n - 1)
        palindrome += '1'
        print(palindrome)
    elif len(num) == 1:
        num = ''.join(num)
        num = int(num)
        num += 1
        print(num)
    else:
        min_index = 0
        max_index = len(num) - 1
        length = len(num)

        stop = False

        if length % 2 == 0:
            i = (length // 2) - 1
            j = (length // 2)

            while num[i] == num[j]:
                i = i - 1
                j = j + 1

                if i < min_index and j > max_index:
                    left_half = num[:length // 2]
                    new_left_half = increment_by_one(left_half)
                    mirrored = mirror(new_left_half, True)
                    print(mirrored)
                    stop = True
                    break

            if not stop:
                if num[i] > num[j]:
                    left_half = num[:length // 2]
                    mirrored = mirror(left_half, True)
                    print(mirrored)

                else:
                    left_half = num[:length // 2]
                    new_left_half = increment_by_one(left_half)
                    mirrored = mirror(new_left_half, True)
                    print(mirrored)

        else:
            i = (length // 2) - 1
            j = (length // 2) + 1
            middle = length // 2

            while num[i] == num[j]:
                i = i - 1
                j = j + 1

                if i < min_index and j > max_index:
                    left_half = num[:middle + 1]
                    new_left_half = increment_by_one(left_half)
                    mirrored = mirror(new_left_half)
                    print(mirrored)
                    stop = True
                    break

            if not stop:
                if num[i] > num[j]:
                    left_half = num[:middle + 1]
                    mirrored = mirror(left_half)
                    print(mirrored)

                else:
                    left_half = num[:middle + 1]
                    new_left_half = increment_by_one(left_half)
                    mirrored = mirror(new_left_half)
                    print(mirrored)


t = int(input())

for i in range(t):
    num = list(input())
    find_next_palindrome(num)


