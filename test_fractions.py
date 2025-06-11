from fractions import reduced_fr

def test_reduced_fr():
    assert reduced_fr (20, 40) == (1, 2)
    assert reduced_fr (3, 9) == (1, 3)
    assert reduced_fr (28, 29) == (28, 29)
    assert reduced_fr (21, 28) == (3, 4)

test_reduced_fr()
print("OK1")

from fractions import pre_per

def test_pre_per():
    assert pre_per (20) == (2)
    assert pre_per (81) == (0)
    assert pre_per (32) == (5)
    assert pre_per (100) == (2)

test_pre_per()
print("OK2")

from fractions import wo_per

def test_wo_per():
    assert wo_per (1, 2) == ('0,5')
    assert wo_per (121, 125) == ('0,968')
    assert wo_per (965, 1000) == ('0,965')
    
test_wo_per()
print ("OK3")

from fractions import exist_per

def test_exist_per():
    assert exist_per (192) == (True)
    assert exist_per (64) == (False)
    assert exist_per (1000) == (False)
    
test_exist_per()
print ("OK4")

from fractions import per_

def test_per_():
    assert per_(1, 3) == ('(3)')
    assert per_(1, 7) == ('(142857)')
    assert per_(1, 11) == ('(09)')
    
test_per_()
print ("OK5")