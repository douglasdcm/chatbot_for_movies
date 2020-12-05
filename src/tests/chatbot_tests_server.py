import unittest
from backend.chatbot import ChatBotInit
from unittest import mock
import io
from settings import EMERGENCY_MSG, NAIVE_MSG


class TestPredictMethods(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestPredictMethods, self).__init__(*args, **kwargs)
        self.pred = None

    def test_chabot_print_prediction_from_user_input_keystroke(self):
        # arrange
        exp = EMERGENCY_MSG
        msg = u"\u2191"  # arrow down
        cb = ChatBotInit()

        actual = cb.get_conversation(msg)

        self.assertTrue(actual in exp)

    def test_chabot_print_prediction_from_user_input_ctrl_c(self):
        # arrange
        exp = EMERGENCY_MSG
        msg = u"\u0003"  # ctrl   c
        cb = ChatBotInit()

        actual = cb.get_conversation(msg)

        self.assertTrue(actual in exp)


if __name__ == "__main__":
    unittest.main()
