import json

with open('intentEndTimeEvent.json') as intentEndTimeEvent:
	intent = json.load(intentEndTimeEvent)
with open('../../resources/classes.json') as subjectModel:
	subjects = json.load(subjectModel)
f = open("generatedIntentEndTimeEvent.yml", "w")

for i in intent:
	for subject in subjects:
		f.write(i.replace("Ex", subject) + "\n")
		f.write(i.replace("Ex", subjects[subject]['name']) + "\n")

f.close()