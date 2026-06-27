import pytest

@pytest.mark.registration
def test_user_registration():
    pass

@pytest.mark.smoke
def test_user_login():
    pass

@pytest.mark.registration
@pytest.mark.regression
def test_password_reset():
    pass
