def test_unsuccessful_login(login_page_fx, invalid_user):
    login_page_fx.open()
    login_page_fx.login(invalid_user)

    assert login_page_fx.get_error_message()
