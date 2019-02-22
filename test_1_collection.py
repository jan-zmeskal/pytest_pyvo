# First let's try pytest's test collection. We don't even need import statement
# Run: pytest test_1_collection.py --collect-only


def test_lazy():
    """This test will be collected, because it starts with 'test_` prefix."""
    pass


def lazy_test():
    """This test will not be collectied by pytests."""
    pass
