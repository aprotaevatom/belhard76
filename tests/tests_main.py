from pytest import mark, fixture

from main import is_palindrome


@fixture()
def foo():
    print("FOO")


@mark.asyncio
@mark.parametrize(
    ("text", "result"),
    (
        ("qweewq", True),
        ("asdf", False),
    ),
)
async def test_is_palindrome(text, result, foo):
    assert is_palindrome(text) == result
