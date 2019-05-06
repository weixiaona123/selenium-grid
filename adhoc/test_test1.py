import pytest
class TestSuite:
    def test_1(self, app):
        app.driver.get('http://console.appadhoc.com')
        print(app.driver.title)
        assert 'A/B Testing' in app.driver.title

    def test_2(self, app):
        app.driver.get('http://www.bing.com')
        assert True
if __name__ == "__main__":
    pytest.main(["-s", "test_test1.py"])