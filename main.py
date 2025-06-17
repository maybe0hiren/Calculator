import logic

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.properties import StringProperty

inputList = []
numbers = []
operations = []

Window.size = (640, 960)
Window.resizable = False
Window.clearcolor = (0, 0, 0, 1)


def merger():
    finalList = []
    buffer = ""

    for x in inputList:
        if isinstance(x, float):
            buffer += str(int(x)) 
        elif x == '.':
            buffer += '.'
        else:
            if buffer:
                finalList.append(float(buffer))
                buffer = ""
            finalList.append(x)

    if buffer:
        finalList.append(float(buffer))

    separate(finalList)


def separate(finalList):
    numbers.clear()
    operations.clear()

    for x in finalList:
        if isinstance(x, float):
            numbers.append(x)
        else:
            operations.append(x)


def execute():
    print(inputList)
    merger()
    print(numbers)
    print(operations)
    answer = logic.fillVectors(numbers, operations)
    print(answer)
    return str(answer)

class rootWidget(FloatLayout):
    textOnScreen = StringProperty("")

    def clickedM(self, button):
        answer = float(execute())
        self.textOnScreen = " "
        numbers.clear()
        operations.clear()
        inputList.clear()
        if button == '+':
            logic.mValueTransfer(answer)
        else:
            logic.mValueTransfer(-answer)

    def backButton(self):
        inputList.pop()
        self.textOnScreen = self.textOnScreen[:-1]

    def displayText(self, value):
        self.textOnScreen += value

    def displayAnswer(self):
        answer = execute()
        self.textOnScreen = answer[:6] if len(answer) > 6 else answer
        numbers.clear()
        operations.clear()
        inputList.clear()
        logic.mValueTransfer(0.0)

    def clearScreen(self):
        self.textOnScreen = ""
        numbers.clear()
        operations.clear()
        inputList.clear()
        logic.mValueTransfer(0.0)

    def clicked(self, char):
        if char.isdigit():
            inputList.append(float(char))
        else:
            inputList.append(char)


class calculatorApp(App):
    def build(self):
        return rootWidget()


if __name__ == "__main__":
    calculatorApp().run()
