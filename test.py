import django.test

class Test(django.test.TestCase):
    def setUp(self):
        print "setup pass"
    def test_basic_addition(self):
        self.assertEqual(1+1, 2)


if __name__=="__main__":
    django.test.main()