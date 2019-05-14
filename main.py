import kivy
kivy.require("1.10.1")

from random import randint
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.core.clipboard import Clipboard
from kivy.uix.button import Button


greeting = ['oi pessoal, ', '', 'eae galera, ', 'oi migxs, ', 'gente amada, ', 'pessoal, ', 'amados, ', 'queridos ', 'comrades, ', 'meus companheiros, ']
reason = ['amanha preciso acordar cedo pra cortar o cabelo, ', 'preciso estudar pra uma prova, ', 'hoje eu nao posso, ', 'vou comer com meus pais, ', 'enceraram a escada aqui de casa hoje, ', 'tenho que fazer janta pra minha irma hoje, ', 'estragou o chuveiro aqui de casa e estou envolvido com isso, ', 'hoje nao vou poder, ', 'tenho uma formatura pra ir, ', 'corri na chuva e liguei o ar, ']
cheers = ['divirtam-se!', 'na proxima nos vemos!', 'aproveitem!', 'enjoy guys', 'beijos', 'ate', 'depois nos falamos']

class RootWidget(FloatLayout):
    def gedbot(self):
        roll_1 = randint(0, len(greeting)-1)
        roll_2 = randint(0, len(reason)-1)
        roll_3 = randint(0, len(cheers)-1)
        answer = greeting[roll_1] + reason[roll_2] + cheers[roll_3]
        self.display.text = answer

class CopyToClip(Button):
    def copyto(self):
        Clipboard.copy(self.parent.parent.ids.display.text)
        

class GedbotApp(App):

    def build(self):
        return RootWidget()

if __name__ == '__main__':
    GedbotApp().run()
