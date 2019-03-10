#! /usr/bin/python3
# Random quiz generator that generates 35 quiz files and 35 answer files

import random

# Database with states and capitals
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia':
 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# Open, write, canswerOptionslose quiz file and answer file
for quiz_num in range(35):

    # shuffle states
    states = list(capitals.keys())
    random.shuffle(states)

    # write header of quiz
    with open('capitals_quiz_%s.txt' % (quiz_num + 1), 'w') as quiz_file:
        quiz_file.write('Name:\n\nDate:\n\nPeriod:\n\n')
        quiz_file.write('' * 20 + 'State Capitals Quiz, Form %s' % (quiz_num + 1))
        quiz_file.write('\n\n')

        # loop through states, ask question for each state[0-49]
        for question_num in range(50):
            # get right and wrong answers
            correct_answer = capitals[states[question_num]] # searches dictionary with state
            wrong_answers = list(capitals.values())  # gets all capitals
            del wrong_answers[wrong_answers.index(correct_answer)] # erases correct answer from list
            wrong_answers = random.sample(wrong_answers, 3) # gets a random sample of 3
            answer_options = wrong_answers + [correct_answer]
            random.shuffle(answer_options)
            # Write the questions
            quiz_file.write('%s. What is the capital of %s?\n' % (question_num + 1, states[question_num]))
            for i in range(4):
                quiz_file.write('%s. %s\n' % ('ABCD'[i], answer_options[i]))
                quiz_file.write('\n')
            # Write the answer key to a file.
            with open('capitals_quiz_answer_%s.txt' % (quiz_num + 1), 'a') as answer_file:
                answer_file.write('%s. %s\n' % (question_num + 1,'ABCD'[answer_options.index(correct_answer)]))
                answer_file.close()
