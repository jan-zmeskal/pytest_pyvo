import random
import time


def test_assert_number():
    random_number = random.randint(1, 10)
    assert random_number > 0


def test_assert_membership():
    current_hour = time.localtime().tm_hour
    assert current_hour in range(0, 24)


def test_steps():
    # Generate random number in range from 1 to 10
    random_number = random.randint(1, 10)
    assert 0 < random_number < 11, 'Radnom number is not in the expected range!'

    # Make sure that current year is lower than the random nubmer
    current_year = time.localtime().tm_year
    assert current_year < random_number, 'Oh no! It\'s too late!'

    # Now let's wait a while and check if we are in the far future
    time.sleep(10000)
    current_year = time.localtime().tm_year
    assert current_year > 3000, 'We are still not in the future...'
