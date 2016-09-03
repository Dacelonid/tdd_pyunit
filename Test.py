class TestCase:
    def __init__(self, name):
        self.name = name

    def run(self):
        method = getattr(self, self.name)
        method()



class WasRun(TestCase):
    def __init__(self, name):
        self.was_run = None
        TestCase.__init__(self, name)

    def test_method(self):
        self.was_run = True

class TestCaseTest(TestCase):
    def test_running_test(self):
        test = WasRun("test_method")
        assert(not test.was_run)
        test.run()
        assert(test.was_run)

TestCaseTest("test_running_test").run()