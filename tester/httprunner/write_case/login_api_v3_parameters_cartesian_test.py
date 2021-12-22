# NOTE: Generated By HttpRunner v3.1.6
# FROM: testcases/login-api-v3-parameters-cartesian.yml


import pytest
from httprunner import Parameters


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseLoginApiV3ParametersCartesian(HttpRunner):
    @pytest.mark.parametrize(
        "param",
        Parameters(
            {
                "username": ["zhangsan", "lisi", "xiaoming"],
                "password": ["zhangsan123", "lisi123", "xiaoming123"],
            }
        ),
    )
    def test_start(self, param):
        super().test_start(param)

    config = Config("login parameters cartesian v3").variables(
        **{"host": "http://127.0.0.1:8888", "status_code": 200}
    )

    teststeps = [
        Step(
            RunRequest("login")
            .post("${host}/login")
            .with_headers(
                **{
                    "User-Agent": "HttpRunner/${get_httprunner_version()}",
                    "Content-Type": "application/x-www-form-urlencoded",
                }
            )
            .with_data("username=${username}&password=${password}")
            .validate()
            .assert_equal("status_code", "${status_code}")
        ),
    ]


if __name__ == "__main__":
    TestCaseLoginApiV3ParametersCartesian().test_start()
