class MyTest(Testcase):
    def test_ok(self):
        self.assertTrue (True)


def test_sample_view(self):
    url = "/apf/v1/test/"
    client = APIClient
    response = client.get (url)
    self.assertEqual(response.status_code,200)