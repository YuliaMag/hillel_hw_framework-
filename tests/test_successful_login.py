def test_successful_login(login_page_fx, dashboard_page_fx, valid_user):

    login_page_fx.open()
    login_page_fx.login(valid_user)

    assert dashboard_page_fx.dashboard_displayed()

