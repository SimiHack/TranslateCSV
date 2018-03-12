from googletrans import Translator
import csv
import timeit

lt=[]
translator = Translator()
with open('C:/Users/simple/Desktop/MyApp/sample.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        translations = translator.translate(row, dest='en')
        for translation in translations:
            lt.append(translation.text)
with open('C:/Users/simple/Desktop/MyApp/output.csv', "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for val in lt:
        writer.writerow([val])
        
start_time = timeit.default_timer()
# code you want to evaluate
elapsed = timeit.default_timer() - start_time
print("Translation has been complete in {}".format(elapsed))
