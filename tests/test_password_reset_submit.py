def test_password_reset_submit(login_page_fx, pas_reset_page_fx, valid_user):
    login_page_fx.open()
    login_page_fx.forgot_pas_click()

    pas_reset_page_fx.passreset_page_display()

    pas_reset_page_fx.enter_username(valid_user)
    pas_reset_page_fx.click_reset_password_button()

    assert pas_reset_page_fx.link_sent_successfully_displayed, ""
