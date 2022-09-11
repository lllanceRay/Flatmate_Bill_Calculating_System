from flat import Bill, Flatmate
from reports import PdfReport, FileSharer

amount = float(input('Hey user! Enter the bill amount: '))
period = input('What is the period? E.g.: December 2021: ')

name1 = input('What is your name? : ')
days_in_house1 = int(input('How many days did you live in the house during the period? : '))

name2 = input('What is the name of another flatmate? : ')
days_in_house2 = int(input(f'How many days did {name2} live in the house during the period? : '))

the_bill = Bill(amount, period)
Flatmate1 = Flatmate(name1, days_in_house1)
Flatmate2 = Flatmate(name2, days_in_house2)

print(f'{name1} pays: ', round(Flatmate1.pays(the_bill, Flatmate2), 2))
print(f'{name2} pays: ', round(Flatmate2.pays(the_bill, Flatmate1), 2))

pdf_report = PdfReport(filename=f'{the_bill.period}.pdf')
pdf_report.generate(Flatmate1, Flatmate2, the_bill)

file_sharer = FileSharer(filepath=pdf_report.filename)
print(file_sharer.share)