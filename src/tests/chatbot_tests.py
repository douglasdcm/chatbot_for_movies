import unittest
from backend.chatbot import ChatBotInit
from unittest import mock
import io


class TestPredictMethods(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestPredictMethods, self).__init__(*args, **kwargs)
        self.pred = None

    def test_chatbot_can_be_instantiated(self):
        cb = ChatBotInit()
        self.assertTrue(cb)

    def test_chabot_predict_from_user_input(self):
        # reference: https://forum.learncodethehardway.com/t/testing-input-and-print/1757/10

        # arrange
        cb = ChatBotInit()
        msg = "exit"
        exp = None

        original_input = mock.builtins.input
        mock.builtins.input = lambda _: msg

        # act
        actual = cb.init_chat_cmd()

        # assert
        self.assertEqual(actual, exp)
        mock.builtins.input = original_input

    def test_chabot_print_prediction_from_user_input(self):
        # reference: https://forum.learncodethehardway.com/t/testing-input-and-print/1757/10

        # arrange
        cb = ChatBotInit()
        msg = "exit"
        exp = "Bye!"

        original_input = mock.builtins.input
        mock.builtins.input = lambda _: msg

        with mock.patch("sys.stdout", new=io.StringIO()) as fake_stdout:
            cb.init_chat_cmd()

        actual = fake_stdout.getvalue()

        self.assertIn(exp, actual)

        mock.builtins.input = original_input

    def test_chabot_print_prediction_from_user_input_not_bye(self):
        # arrange
        msg = "any message not bye"

        cb = ChatBotInit()

        original_input = mock.builtins.input
        mock.builtins.input = lambda _: msg

        with mock.patch("sys.stdout", new=io.StringIO()) as fake_stdout:
            cb.init_chat_cmd(run_once=True)

        actual = fake_stdout.getvalue()

        self.assertTrue(actual)

        mock.builtins.input = original_input

    def test_chabot_print_prediction_from_user_input_keystroke(self):
        # arrange
        msg = u"\u2191"  # arrow down
        cb = ChatBotInit()

        original_input = mock.builtins.input
        mock.builtins.input = lambda _: msg

        with mock.patch("sys.stdout", new=io.StringIO()) as fake_stdout:
            cb.init_chat_cmd(run_once=True)

        actual = fake_stdout.getvalue()

        self.assertTrue(actual)

        mock.builtins.input = original_input

    def test_chabot_print_prediction_from_user_input_ctrl_c(self):
        # arrange
        msg = u"\u0003"  # ctrl   c
        cb = ChatBotInit()

        original_input = mock.builtins.input
        mock.builtins.input = lambda _: msg

        with mock.patch("sys.stdout", new=io.StringIO()) as fake_stdout:
            cb.init_chat_cmd(run_once=True)

        actual = fake_stdout.getvalue()

        self.assertTrue(actual)

        mock.builtins.input = original_input


if __name__ == "__main__":
    unittest.main()
