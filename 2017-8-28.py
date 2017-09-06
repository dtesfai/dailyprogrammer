usr_input = input()
lucky_nums = list(range(1, usr_input * 2))

key = 0
val = 0

while val < len(lucky_nums):
    if key == 0:
        del lucky_nums[1::2]
        key += 1
        continue
    val = lucky_nums[key]
    del lucky_nums[val-1::val]
    key += 1

if usr_input in lucky_nums:
    print('{0} is a lucky number').format(usr_input)
else:
    prev_lucky_val = max(filter(lambda x: x < usr_input, lucky_nums))
    next_lucky_val = min(filter(lambda x: x > usr_input, lucky_nums))

    print('{0} < {1} < {2}'.format(prev_lucky_val, usr_input, next_lucky_val))