# Задание 3. Создайте класс Calculation , в котором будет одно свойство calculationLine.
# методы: SetCalculationLine который будет который будет изменять значение свойства,
# SetLastSymbolCalculationLine который будет в конец строки прибавлять символ,
# GetCalculationLine который будет выводить значение свойства, GetLastSymbol получение
# последнего символа, DeleteLastSymbol удаление последнего символа из строки;

class Calculation:

    def __init__(self):
        self.calculationLine = ""

    def SetCalculationLine(self, new_line):
        self.calculationLine = new_line

    def SetLastSymbolCalculationLine(self, symbol):
        self.calculationLine += symbol

    def GetCalculationLine(self):
        return self.calculationLine

    def GetLastSymbol(self):
        if self.calculationLine:
            return self.calculationLine[-1]
        else:
            return ""

    def DeleteLastSymbol(self):
        self.calculationLine = self.calculationLine[:-1]


myclass = Calculation()

myclass.SetCalculationLine("ПРИВЕТ МИР")
print("Значение у нас после изменения выглядит так: ", myclass.GetCalculationLine())
myclass.SetLastSymbolCalculationLine("!!")
print("Значение у нас после добавления выглядит так: ", myclass.GetCalculationLine())
print("Последний символ = ", myclass.GetLastSymbol())
myclass.DeleteLastSymbol()
print("Изменения после удаления последнего символа:", myclass.GetCalculationLine())
myclass.DeleteLastSymbol()
print("Изменения после удаления последнего символа:", myclass.GetCalculationLine())
print("Последний символ = ", myclass.GetLastSymbol())
myclass.SetCalculationLine("")
print("Последний символ после добавления в конец пробел = ", myclass.GetLastSymbol())