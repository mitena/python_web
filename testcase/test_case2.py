import requests
import pytest
import allure
@allure.feature("类的说明2")
class Testjekinsss:
    @allure.story("用例的说明2")
    def test_getreqs(self):
        url = 'http://spcare-api.medbanks-test.com/api/trading-product/product/hr/spu?channelCode=3988c7f88ebcb58c&spuCode=00001057'
        res = requests.get(url=url)
        #打印数据
        print(res.json())
        assert res.json()["message"] == "成功!"
