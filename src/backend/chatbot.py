from predict import Prediction

class ChatBotInit:

	def init_chat(self):
		print('Getting out of bed...')
		print(' Tip: You can type \"bye\" to leave.')

		m = None
		me_prefix = '  You: '
		bot_prefix = '  Me:  '
		exit = 'bye'

		p = Prediction()

		print('I am ready to talk.')
		while(m != exit):
			m = str(input(me_prefix))

			if m != 'bye':
				r = str(p.predict(m))
				print(bot_prefix + r)

		print(bot_prefix + 'Bye!')