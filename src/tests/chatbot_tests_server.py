import io
import unittest
from unittest import mock

from backend.chatbot import ChatBotInit
from src.settings import EMERGENCY_MSG, NAIVE_MSG


class TestPredictMethods(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestPredictMethods, self).__init__(*args, **kwargs)
        self.pred = None

    def test_chabot_print_prediction_from_user_input_keystroke(self):
        # arrange
        exp = EMERGENCY_MSG
        msg = "\u2191"  # arrow down
        cb = ChatBotInit()

        actual = cb.get_conversation(msg)

        self.assertTrue(actual in exp)

    def test_chabot_print_prediction_from_user_input_ctrl_c(self):
        # arrange
        exp = EMERGENCY_MSG
        msg = "\u0003"  # ctrl   c
        cb = ChatBotInit()

        actual = cb.get_conversation(msg)

        self.assertTrue(actual in exp)


if __name__ == "__main__":
    unittest.main()
