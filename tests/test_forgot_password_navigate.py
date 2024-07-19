def test_forgot_password_navigate(login_page_fx, pas_reset_page_fx):
    login_page_fx.open()
    login_page_fx.forgot_pas_click()

    assert pas_reset_page_fx.passreset_page_display(), ""
