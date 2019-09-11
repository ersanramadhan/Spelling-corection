
import fuzzy
import editdistance
import os
import time

#file directory root
os.chdir('/Users/ersanramadhan/Desktop/Knowledge Tech/Data')

start_time = time.time()
# open a file
def open_file(file_name):
    lst = []
    fo = open(file_name, "r")
    for line in fo:
        words = line.split()
        lst.append(words[0])
    fo.close()
    return lst

misspell = open_file("misspell.txt")
dict = open_file("dict.txt")
correct= open_file("correct.txt")
# print("dataset : ")
# print (len(misspell))
# print (len(dict))
# print(len(correct))


# using edit distance to generate a possible predictions for a misspelled word
def edit_distance():
    predictions = []
    for word in misspell:
        threshold = len(word)
        temp = []
        for i in dictionary:
            count = editdistance.eval(word, i)
            if count < threshold:
                threshold = count
                temp = [i]
            elif count == threshold:
                temp.append(i)
        predictions.append(temp)
    return predictions

# calculating the precision of the predictions for misspelled words
def calculate(predictions):
    index = 0
    correct_counter = 0
    predict_counter = 0
    for word in predictions:
        if len(word) > 1:
            for elem in word:
                if elem == correct[index]:
                    correct_counter += 1
                pred_counter += 1
        elif len(word) == 1:
            if word[0] == correct[index]:
                correct_counter += 1
            predict_counter += 1
        index += 1
    
    return (correct_counter, predict_counter)

#using soundex to generate a possible predictions for a misspelled word
def using_soundex():
    soundex = fuzzy.Soundex(4)
    soundex_predics = []
    for element in misspell:
        temp = []
        for elem in dict:
            if soundex(element) == soundex(elem):
                temp.append(elem)
        soundex_predics.append(temp)
    return soundex_predics



edit_predics = edit_distance()
edit_calc = calculate(edit_predics)
edit_precision = edit_calc[0] / edit_calc[1]
edit_accuracy = edit_calc[0] / len(edit_predics)
# print("precision when using edit distance :")
# print(edit_precision)
# print("accuracy when using edit distance : ")
# print(edst_accuracy)


print("edit distance: ")
print (len(edit_predics))
print (edit_calc[0])
print (edst_calc[1])


soundex_predics = using_soundex()
soundex_calc = calculate(soundex_predics)
soundex_precision = soundex_calc[0] / soundex_calc[1]
soundex_accuracy = soundex_calc[0] / len(soundex_predics)

# print("precision when using edit distance :")
# print(soundex_precision)
# print("accuracy when using edit distance : ")
# print(soundex_accuracy)

print("soundex :")
print (len(soundex_predics))
print (soundex_calc[0])
print (soundex_calc[1])

print("--- %s seconds ---" % (time.time() - start_time))
