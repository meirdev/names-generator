import string

import names_generator


def test_get_random_name():
    while True:
        name1 = names_generator.get_random_name()
        name2 = names_generator.get_random_name()

        if name1 != name2:
            break


def test_get_random_name_with_retry():
    name = names_generator.get_random_name(1)

    assert name[-1] in string.digits


def test_get_random_name_skip_boring_wozniak(mocker):
    i = 0

    def _random_choice_mock(*args, **kwargs):
        nonlocal i

        if i == 0:
            val = "boring"
        elif i == 1:
            val = "wozniak"
        else:
            val = "word"

        i += 1

        return val

    mocker.patch("random.choice", side_effect=_random_choice_mock)

    names_generator.get_random_name()

    assert i == 4
