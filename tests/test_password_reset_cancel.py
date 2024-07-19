
"""
When being on reset password page
If the user clicks Cancel button they are returned to the login page back
It is impossible to click Cancel button without adding username, so the step is included
"""


def test_password_reset_cancel(login_page_fx, pas_reset_page_fx, valid_user):
    login_page_fx.open()
    login_page_fx.forgot_pas_click()

    pas_reset_page_fx.passreset_page_display()

    pas_reset_page_fx.enter_username(valid_user)
    pas_reset_page_fx.click_cancel_button()

    assert login_page_fx.open, ""
