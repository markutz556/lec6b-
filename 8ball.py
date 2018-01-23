#!/usr/bin/env python3
import random
import sys
again = True
answers_list = ["It is certain","It is decidedly so", "Without a doubt",
				"Yes definitely, You may rely on it", "As I see it, yes",
				"Most likely", "Outlook good", "Yes", "Signs point to yes",
				"Reply hazy try again", "Ask again later", "Better not tell you now",
				"Cannot predict now", "Concentrate and ask again", "Don't count on it",
				"My reply is no", "My sources say no", "Outlook not so good",
				"Very doubtful"]
while again:
	question = str(input("Question (press enter to quit): "))
	answers = random.randint(0, 19)
	if question.endswith("?"):
		print(answers_list[answers])
	elif question == "":
		again = False
	else:
		print("8 ball doesn't understand.")
