import pytest
from page.Console_page import Consolepage
from test_case import test_ALogin

class TestConsolelogin:


    @pytest.mark.parametrize(
        "password",
        [("zl123456")],
        ids=["case3"]
        )
    def test_conlogin(self, browser, password):
        """登录控制台"""
        page = Consolepage(browser)

        # 模块测试代码（正式验证需注释）
        # test_ALogin.Testlogin.test_login(self, "18210785192", "zl123456", browser)

        #正式代码
        page.console_table.click()
        page.console_password.send_keys(password)
        page.console_login_btn.click()
        console_page = page.console_assert.text
        page.wait(2)
        assert console_page == "欢迎使用企云会控制台"


    if __name__ == '__main__':
        pytest.main(["-v", "-s", "test_Console.py::TestConsolelogin::test_conlogin", "--html", "./report.html"])

