from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.audio import SoundLoader
from kivy.lang import Builder
from kivy.animation import Animation
from kivy.uix.modalview import ModalView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
import random


class HomeGame(Screen):
    pass


class MathGame(Screen):
    pass


class TekaTekaGame(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(on_enter=self.generate_puzzle)
        self.popup = None
        self.operators = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y
        }

    def generate_puzzle(self, *args):
        while True:

            self.num1 = random.randint(1, 9)
            self.num2 = random.randint(1, 9)

            valid_operators = []
            for op in self.operators.keys():
                result = self.operators[op](self.num1, self.num2)

                if result == int(result) and 1 <= result <= 9:
                    valid_operators.append(op)

            if valid_operators:
                break

        self.correct_operator = random.choice(valid_operators)
        self.result = int(
            self.operators[self.correct_operator](self.num1, self.num2))

        self.ids.num1_image.source = f"image/{self.num1}.png"
        self.ids.num2_image.source = f"image/{self.num2}.png"
        self.ids.result_image.source = f"image/{self.result}.png"

        possible_operators = list(self.operators.keys())
        possible_operators.remove(self.correct_operator)
        wrong_operators = random.sample(possible_operators, 2)
        options = [self.correct_operator] + wrong_operators
        random.shuffle(options)

        self.ids.option1.text = options[0]
        self.ids.option2.text = options[1]
        self.ids.option3.text = options[2]

    def check_answer(self, selected_operator):
        if selected_operator == self.correct_operator:
            self.ids.result.text = "Correct!"
            self.show_win_popup()
        else:
            self.ids.result.text = "Try Again"
            self.show_lose_popup()

    def show_win_popup(self):
        self.popup = ModalView(size_hint=(0.7, 0.7), auto_dismiss=False)
        self.popup.background_color = (0, 0, 1, 1)

        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        you_win_label = Image(source="image/win.png", size_hint=(1, 0.4))
        layout.add_widget(you_win_label)

        stars_image = Image(source="image/star.png", size_hint=(1, 0.4))
        layout.add_widget(stars_image)

        button_layout = FloatLayout(size_hint=(1, 0.2))

        home_button = Button(
            size_hint=(None, None),
            size=(40, 40),
            on_release=self.go_home,
            background_normal='image/ho.png',
            background_down='image/home.png'
        )
        next_button = Button(
            size_hint=(None, None),
            size=(40, 40),
            on_release=self.go_next,
            background_normal='image/next.png',
            background_down='image/next.png'
        )

        home_button.pos_hint = {'center_x': 0.3, 'center_y': 0.5}
        next_button.pos_hint = {'center_x': 0.7, 'center_y': 0.5}

        button_layout.add_widget(home_button)
        button_layout.add_widget(next_button)

        layout.add_widget(button_layout)
        self.popup.add_widget(layout)
        self.popup.open()

    def show_lose_popup(self):
        self.popup = ModalView(size_hint=(0.7, 0.7), auto_dismiss=False)
        self.popup.background_color = (0, 0, 1, 1)

        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        you_win_label = Image(source="image/lose.png", size_hint=(1, 0.4))
        layout.add_widget(you_win_label)

        # stars_image = Image(source="image/star.png", size_hint=(1, 0.4))
        # layout.add_widget(stars_image)

        button_layout = FloatLayout(size_hint=(1, 0.2))

        home_button = Button(
            size_hint=(None, None),
            size=(40, 40),
            on_release=self.go_home,
            background_normal='image/ho.png',
            background_down='image/home.png'
        )
        next_button = Button(
            size_hint=(None, None),
            size=(40, 40),
            on_release=self.go_next,
            background_normal='image/next.png',
            background_down='image/next.png'
        )

        home_button.pos_hint = {'center_x': 0.3, 'center_y': 0.5}
        next_button.pos_hint = {'center_x': 0.7, 'center_y': 0.5}

        button_layout.add_widget(home_button)
        button_layout.add_widget(next_button)

        layout.add_widget(button_layout)
        self.popup.add_widget(layout)
        self.popup.open()

    def go_home(self, *args):
        self.manager.current = 'mathgame'
        if self.popup:
            self.popup.dismiss()

    def go_next(self, *args):
        self.generate_puzzle()
        if self.popup:
            self.popup.dismiss()


class BerhitungGame(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(on_enter=self.generate_sequence)
        self.popup = None

    def generate_sequence(self, *args):

        sequence = list(range(1, 9))

        self.missing_positions = sorted(random.sample(range(8), 2))
        self.missing_numbers = [sequence[pos]
                                for pos in self.missing_positions]

        self.correct_answers = self.missing_numbers.copy()

        answers = self.missing_numbers + [random.randint(1, 8)]
        while len(set(answers)) < 3:
            answers = self.missing_numbers + [random.randint(1, 8)]
        random.shuffle(answers)

        sequence_layout = self.ids.sequence_layout
        sequence_layout.clear_widgets()

        for i in range(8):
            if i in self.missing_positions:

                img = Image(source='image/-.png',
                            size_hint=(None, None), size=(100, 100))
            else:

                img = Image(
                    source=f'image/{sequence[i]}.png', size_hint=(None, None), size=(100, 100))
            sequence_layout.add_widget(img)

        self.ids.option1.text = str(answers[0])
        self.ids.option2.text = str(answers[1])
        self.ids.option3.text = str(answers[2])

    def check_answer(self, selected_answer):
        selected = int(selected_answer)
        if selected in self.correct_answers:
            self.correct_answers.remove(selected)
            if not self.correct_answers:
                self.ids.result.text = "Correct!"
                self.show_win_popup()
            else:
                self.ids.result.text = "Good! One more to go!"
        else:
            self.ids.result.text = "Try Again"
            self.show_lose_popup()

    def show_win_popup(self):
        self.popup = ModalView(size_hint=(0.7, 0.7), auto_dismiss=False)
        self.popup.background_color = (0, 0, 1, 1)

        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        you_win_label = Image(source="image/win.png", size_hint=(1, 0.4))
        layout.add_widget(you_win_label)

        stars_image = Image(source="image/star.png", size_hint=(1, 0.4))
        layout.add_widget(stars_image)

        button_layout = FloatLayout(size_hint=(1, 0.2))

        home_button = Button(
            size_hint=(None, None),
            size=(40, 40),
            on_release=self.go_home,
            background_normal='image/ho.png',
            background_down='image/home.png'
        )
        next_button = Button(
            size_hint=(None, None),
            size=(40, 40),
            on_release=self.go_next,
            background_normal='image/next.png',
            background_down='image/next.png'
        )

        home_button.pos_hint = {'center_x': 0.3, 'center_y': 0.5}
        next_button.pos_hint = {'center_x': 0.7, 'center_y': 0.5}

        button_layout.add_widget(home_button)
        button_layout.add_widget(next_button)

        layout.add_widget(button_layout)
        self.popup.add_widget(layout)
        self.popup.open()

    def show_lose_popup(self):
        self.popup = ModalView(size_hint=(0.7, 0.7), auto_dismiss=False)
        self.popup.background_color = (0, 0, 1, 1)

        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        you_win_label = Image(source="image/lose.png", size_hint=(1, 0.4))
        layout.add_widget(you_win_label)

        # stars_image = Image(source="image/star.png", size_hint=(1, 0.4))
        # layout.add_widget(stars_image)

        button_layout = FloatLayout(size_hint=(1, 0.2))

        home_button = Button(
            size_hint=(None, None),
            size=(40, 40),
            on_release=self.go_home,
            background_normal='image/ho.png',
            background_down='image/home.png'
        )
        next_button = Button(
            size_hint=(None, None),
            size=(40, 40),
            on_release=self.go_next,
            background_normal='image/next.png',
            background_down='image/next.png'
        )

        home_button.pos_hint = {'center_x': 0.3, 'center_y': 0.5}
        next_button.pos_hint = {'center_x': 0.7, 'center_y': 0.5}

        button_layout.add_widget(home_button)
        button_layout.add_widget(next_button)

        layout.add_widget(button_layout)
        self.popup.add_widget(layout)
        self.popup.open()

    def go_home(self, *args):
        self.manager.current = 'mathgame'
        if self.popup:
            self.popup.dismiss()

    def go_next(self, *args):
        self.generate_sequence()
        if self.popup:
            self.popup.dismiss()


class PenjumlahanGame(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(on_enter=self.generate_question)
        self.popup = None

    def generate_question(self, *args):
        self.num1 = random.randint(1, 9)
        self.num2 = random.randint(1, 9)
        correct_answer = self.num1 + self.num2

        wrong_answer1 = correct_answer + random.randint(1, 3)
        wrong_answer2 = correct_answer - random.randint(1, 3)

        wrong_answer1 = max(wrong_answer1, 0)
        wrong_answer2 = max(wrong_answer2, 0)

        answers = [correct_answer, wrong_answer1, wrong_answer2]
        random.shuffle(answers)

        self.ids.num1_image.source = f"image/{self.num1}.png"
        self.ids.num2_image.source = f"image/{self.num2}.png"

        self.ids.option1.text = str(answers[0])
        self.ids.option2.text = str(answers[1])
        self.ids.option3.text = str(answers[2])
        self.correct_answer = correct_answer

    def check_answer(self, selected_answer):
        if int(selected_answer) == self.correct_answer:
            self.ids.result.text = "Correct!"
            self.show_win_popup()
        else:
            self.ids.result.text = "Try Again"

    def show_win_popup(self):
        self.popup = ModalView(size_hint=(0.7, 0.7), auto_dismiss=False)
        self.popup.background_color = (0, 0, 1, 1)

        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        you_win_label = Image(source="image/win.png", size_hint=(1, 0.4))
        layout.add_widget(you_win_label)

        stars_image = Image(source="image/star.png", size_hint=(1, 0.4))
        layout.add_widget(stars_image)

        button_layout = FloatLayout(size_hint=(1, 0.2))

        home_button = Button(size_hint=(None, None), size=(40, 40), on_release=self.go_home,
                             background_normal='image/ho.png', background_down='image/home.png')
        next_button = Button(size_hint=(None, None), size=(40, 40), on_release=self.go_next,
                             background_normal='image/next.png', background_down='image/next.png')

        home_button.pos_hint = {'center_x': 0.3, 'center_y': 0.5}
        next_button.pos_hint = {'center_x': 0.7, 'center_y': 0.5}

        button_layout.add_widget(home_button)
        button_layout.add_widget(next_button)

        layout.add_widget(button_layout)

        self.popup.add_widget(layout)

        self.popup.open()

    def go_home(self, *args):
        self.manager.current = 'mathgame'
        if self.popup:
            self.popup.dismiss()

    def go_next(self, *args):
        self.generate_question()
        if self.popup:
            self.popup.dismiss()


class PenguranganGame(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(on_enter=self.generate_question)
        self.popup = None

    def generate_question(self, *args):
        self.num1 = random.randint(1, 9)
        self.num2 = random.randint(1, 9)
        correct_answer = abs(self.num1 - self.num2)

        wrong_answer1 = correct_answer
        wrong_answer2 = correct_answer

        while wrong_answer1 == correct_answer or wrong_answer1 == wrong_answer2:
            wrong_answer1 = random.randint(0, 9)

        while wrong_answer2 == correct_answer or wrong_answer2 == wrong_answer1:
            wrong_answer2 = random.randint(0, 9)

        answers = [correct_answer, wrong_answer1, wrong_answer2]
        random.shuffle(answers)

        self.ids.num1_image.source = f"image/{self.num1}.png"
        self.ids.num2_image.source = f"image/{self.num2}.png"

        self.ids.option1.text = str(answers[0])
        self.ids.option2.text = str(answers[1])
        self.ids.option3.text = str(answers[2])
        self.correct_answer = correct_answer

    def check_answer(self, selected_answer):
        if int(selected_answer) == self.correct_answer:
            self.ids.result.text = "Correct!"
            self.show_win_popup()
        else:
            self.ids.result.text = "Try Again"

    def show_win_popup(self):
        self.popup = ModalView(size_hint=(0.7, 0.7), auto_dismiss=False)
        self.popup.background_color = (0, 0, 1, 1)

        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        you_win_label = Image(source="image/win.png", size_hint=(1, 0.4))
        layout.add_widget(you_win_label)

        stars_image = Image(source="image/star.png", size_hint=(1, 0.4))
        layout.add_widget(stars_image)

        button_layout = FloatLayout(size_hint=(1, 0.2))

        home_button = Button(size_hint=(None, None), size=(40, 40), on_release=self.go_home,
                             background_normal='image/ho.png', background_down='image/home.png')
        next_button = Button(size_hint=(None, None), size=(40, 40), on_release=self.go_next,
                             background_normal='image/next.png', background_down='image/next.png')

        home_button.pos_hint = {'center_x': 0.3, 'center_y': 0.5}
        next_button.pos_hint = {'center_x': 0.7, 'center_y': 0.5}

        button_layout.add_widget(home_button)
        button_layout.add_widget(next_button)

        layout.add_widget(button_layout)

        self.popup.add_widget(layout)

        self.popup.open()

    def go_home(self, *args):
        self.manager.current = 'mathgame'
        if self.popup:
            self.popup.dismiss()

    def go_next(self, *args):
        self.generate_question()
        if self.popup:
            self.popup.dismiss()


class PengaturanGame(Screen):
    pass


class MathApp(MDApp):
    def build(self):
        self.backsound = SoundLoader.load('opening.wav')
        if self.backsound:
            self.backsound.loop = True
            self.backsound.play()

        return Builder.load_file('main.kv')


if __name__ == "__main__":
    MathApp().run()
