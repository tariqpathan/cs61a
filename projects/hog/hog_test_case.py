import hog

always = hog.always_roll

def strat0(s0, s1):
        if s0 == 0: return 3
        if s0 == 7: return 5
        return 8

def strat1(s0, s1):
        if s0 == 0: return 1
        if s0 == 4: return 2
        return 6

# s0, s1 = hog.play(strat0, strat1, score0=0, score1=0, goal=21, 
#     dice=hog.make_test_dice(
#         2, 2, 3, 4, 2, 2, 2, 2, 2, 3, 5, 2, 2, 2, 2, 2, 2, 2, 6, 1))

# print(s0, s1)

# s0, s1 = hog.play(always(2), always(1), score0=17, score1=6, goal=21, 
#     dice=hog.make_test_dice(1, 2))

# print(s0, s1)

def echo(s0, s1):
    print("echo called")
    print(s0, s1)
    return echo

def count(n):
    # print(n)
    def say(s0, s1):
        # print(s0, s1)
        print(n)
        # print("DEBUG: returning count(n+1)", n + 1)
        return count(n + 1)
    return say

def echo2(s0, s1):
    print(s0, s1)
    return echo2

def total(s0, s1):
    print("total", s0 + s1)
    return echo3

def echo3(s0, s1):
    print("echo3", s0, s1)
    return total

strat0 = always(1) #lambda score, opponent: 1 - opponent // 10
strat1 = always(1)

# s0, s1 = hog.play(strat0, strat1, dice=hog.make_test_dice(2, 3), goal=15, say=echo3)

def echo_0(s0, s1):
    print('*', s0)
    return echo_0

def echo_1(s0, s1):
    print('**', s1)
    return echo_1

s0, s1 = hog.play(strat0, strat1, dice=hog.make_test_dice(2), goal=3, say=hog.both(echo_0, echo_1))