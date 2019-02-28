import random
import time

def test_assert_number():
    random_number = random.randint(1, 10)
    assert random_number > 0

def test_assert_membership():
    current_hour = time.localtime().tm_hour
    assert current_hour in range(0, 24)

def test_steps():
    random_number = random.randint(1, 10)
    assert random_number > 0, 'Random number is too small!'

    current_year = time.localtime().tm_year
    assert current_year < random_number, 'We missed beginning of our era!'

    time.sleep(10000)
    current_year = time.localtime().tm_year
    assert current_year > 3000, 'We are still not in the future!'
