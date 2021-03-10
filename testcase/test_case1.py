import requests
import pytest
import allure
@allure.feature("类的说明")
class Testjekinss:
    @allure.story("用例的说明")
    def test_getreq(self):
        url = 'http://spcare-api.medbanks-test.com/api/trading-product/product/hr/spu?channelCode=3988c7f88ebcb58c&spuCode=00001057'
        res = requests.get(url=url)
        #打印数据
        print(res.json())
        assert res.json()["message"] == "成功!"

