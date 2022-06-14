import pytest
from ten_thousand.game_logic import GameLogic

pytestmark = [pytest.mark.version_3]


def test_validate_legal_keepers():
    roll = (1, 2, 3, 4, 5)
    keepers = (5, 1)
    actual = GameLogic.validate_keepers(roll, keepers)
    expected = True
    assert actual == expected


def test_validate_illegal_keepers():
    roll = (1, 2, 3, 4, 5)
    keepers = (1, 1, 1, 1, 1)
    actual = GameLogic.validate_keepers(roll, keepers)
    expected = False
    assert actual == expected


def test_validate_illegal_overflow():
    roll = (1,)
    keepers = (1, 1, 1, 1, 1, 1)
    actual = GameLogic.validate_keepers(roll, keepers)
    expected = False
    assert actual == expected

def test_validate_list_comparison_greater_than():
    roll = (1,1,2)
    keepers = (2,2)
    actual = GameLogic.validate_keepers(roll, keepers)
    expected = False
    assert actual == expected

def test_validate_list_comparison_greater_than_six():
    roll = (6,2,6,3,6,3)
    keepers = (6,6,6,6)
    actual = GameLogic.validate_keepers(roll, keepers)
    expected = False
    assert actual == expected