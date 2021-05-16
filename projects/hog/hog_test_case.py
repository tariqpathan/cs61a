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

s0, s1 = hog.play(always(2), always(1), score0=17, score1=6, goal=21, 
    dice=hog.make_test_dice(1, 2))

print(s0, s1)