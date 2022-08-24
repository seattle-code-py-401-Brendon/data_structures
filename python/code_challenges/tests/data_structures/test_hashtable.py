import pytest
from python.code_challenges.data_structures.hashtable import Hashtable


def test_exists():
    assert Hashtable


# @pytest.mark.skip("TODO")
def test_get_apple():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected

def test_contains_apple():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.contains("apple")
    expected = True
    assert actual == expected

def test_keys_apple():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    hashtable.set("brendon", "also used for apple sauce")
    actual = hashtable.keys()
    expected = ['brendon', 'apple']
    assert actual == expected

@pytest.mark.xfail
def test_xfail_keys():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    hashtable.set("brendon", "also used for apple sauce")
    actual = hashtable.keys()
    expected = ['apple', 'brendon']
    assert actual == expected


def test_edge_case():
    hashtable = Hashtable()
    hashtable.set(1234, "Used for apple sauce")
    actual = hashtable.keys()
    expected = [1234]
    assert actual == expected



# @pytest.mark.skip("TODO")
# def test_internals():
#     hashtable = Hashtable(1024)
#     hashtable.set("ahmad", 30)
#     hashtable.set("silent", True)
#     hashtable.set("listen", "to me")
#     actual = []

    # NOTE: purposely breaking encapsulation to test the "internals" of Hashmap
    # for item in hashtable._buckets:
    #     if item:
    #         actual.append(item.display())

    # expected = [[["silent", True], ["listen", "to me"]], [["ahmad", 30]]]

    # assert actual == expected
