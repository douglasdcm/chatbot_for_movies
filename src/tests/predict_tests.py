import unittest
from backend.predict import Prediction 
import pandas as pd
from settings import EMERGENCY_MSG, NAIVE_MSG

class ModelMock():

    def predict(self, expected):

        if expected[0][0] == 1:
            return 1 #question
        else:
            return 0 #answer


class TokenizerMock():

    def texts_to_matrix(self, msg: list):

        if 'qqq' in msg[0]:
            return [[1, 0] ,
                    [0, 0]] #question
        else:
            return [[0, 0] ,
                    [0, 0]] #answer


class TestPredictMethods(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestPredictMethods, self).__init__(*args, **kwargs)
        self.pred = None

    def tearDown(self):
        self.pred = None

    def setUp(self):

        what = 'what music'
        when = 'when movie'
        how = 'how house'
        who = 'who'
        yes = 'yes know lesson'
        no = 'no firend'
        maybe = 'maybe solve problem'
        never = 'never'

        questions = set([what, when, how, who])
        answers = set([yes, no, maybe, never])

        #the sum of page computes must tend to 1
        pc_questions = {what: 0.7, when: 0.2, how: 0.1, who: 0.0}
        pc_answers = {yes: 0.5, no: 0.25, maybe: 0.25, never: 0.0}    

        messages = pd.DataFrame(columns=['msg', 'msg_2', 'msg_pre_processed'],
                                data=[['what are you doing for music?','never mind', what],
                                      ['never mind', 'when are you doing?', never],
                                      ['when are you doing for movie?','yes I know', when],
                                      ['yes I know the lesson', 'how are you doing?', yes],
                                      ['how are you doing the house?', 'no chance', how],
                                      ['no chance my friend','test are you doing?', no],
                                      ['maybe I am helping to solve the problem','maybe what?', maybe],
                                      ['test are you doing in the company?','end of line','test are you doing company'],
                                      ['$%¨¨&*()','special character','$%¨¨&*()'],
                                      ['123456','number character','123456'],
                                      ['a','one character','a']
                                ]) 

        model = ModelMock()

        tokenizer = TokenizerMock()
        self.pred = Prediction(questions=questions,
                            answers=answers,
                            pc_questions=pc_questions,
                            pc_answers=pc_answers,
                            messages=messages,
                            model=model,
                            tokenizer=tokenizer)


    def test_can_predit_message_in_dataframe(self):
        #arrange
        msg = 'yes I know the lesson'
        exp = 'how are you doing?'

        #act
        actual = self.pred.predict(msg)

        #assert
        self.assertEqual(actual, exp)


    def test_can_predit_message_not_in_dataframe(self):
        #arrange
        msg = 'this messge is not in dataframe'
        exp = NAIVE_MSG

        #act
        actual = self.pred.predict(msg)

        #assert
        self.assertTrue(actual in exp)


    def test_can_predit_message_not_in_df_but_similar(self):
        #arrange
        msg = 'this messge is NEVER in dataframe' #similar to 'never'
        exp = 'when are you doing?'

        #act
        actual = self.pred.predict(msg)

        #assert
        self.assertEqual(actual, exp)

    
    def test_can_predit_message_with_all_special_char(self):
        #arrange
        msg = '$%¨¨&*()' #pre_processing will clean all
        exp = EMERGENCY_MSG

        #act
        actual = self.pred.predict(msg)

        #assert
        self.assertTrue(actual in exp)


    def test_can_predit_message_with_some_special_char(self):
        #arrange
        msg = 'never $%¨¨&*()' #pre_processing will clean all
        exp = 'when are you doing?' #biggest page rank

        #act
        actual = self.pred.predict(msg)

        #assert
        self.assertEqual(actual, exp)


    def test_can_predit_message_when_is_question(self):
        #arrange
        msg = 'how are you doing the house boy qqq' #qqq is the '?'
        exp = 'no chance'

        #act
        actual = self.pred.predict(msg)

        #assert
        self.assertEqual(actual, exp)


    def test_can_predit_message_when_is_string_of_number(self):
        #arrange
        msg = '123456'
        exp = EMERGENCY_MSG

        #act
        actual = self.pred.predict(msg)

        #assert
        self.assertTrue(actual in exp)


    def test_can_predit_message_when_has_some_numbers(self):
        #arrange
        msg = 'when I saw the movie 123456 times qqq' #qqq is the '?'
        exp = 'yes I know'

        #act
        actual = self.pred.predict(msg)

        #assert
        self.assertEqual(actual, exp)


    def test_can_predit_message_upper_case(self):
        #arrange
        msg = 'MAYBE IS A PROBLEM'
        exp = 'maybe what?'

        #act
        actual = self.pred.predict(msg)

        #assert
        self.assertEqual(actual, exp)

    def test_can_predit_message_one_character(self):
        #arrange
        msg = 'a'
        exp = EMERGENCY_MSG

        #act
        actual = self.pred.predict(msg)

        #assert
        self.assertTrue(actual in exp)


    def test_can_predit_message_empty(self):
        #arrange
        msg = ''
        exp = EMERGENCY_MSG

        #act
        actual = self.pred.predict(msg)

        #assert
        self.assertTrue(actual in exp)


    def test_can_predit_message_null(self):
        #arrange
        msg = None
        exp = EMERGENCY_MSG

        #act
        actual = self.pred.predict(msg)

        #assert
        self.assertTrue(actual in exp)


    def test_can_predit_message_is_number(self):
        #arrange
        msg = 123456
        exp = EMERGENCY_MSG

        #act
        actual = self.pred.predict(msg)

        #assert
        self.assertTrue(actual in exp)

if __name__ == '__main__':
    unittest.main()