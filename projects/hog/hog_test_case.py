from hog import play, always_roll, both, announce_lead_changes, say_scores
from dice import make_test_dice

dice = make_test_dice(1, 2, 3, 3)
always = always_roll

strat0 = strat1 = always(3)

s0, s1 = play(strat0, strat1, dice=dice, goal=8, say=both(say_scores, announce_lead_changes()))