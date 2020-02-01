from cmd import Cmd
import mocks
 
mockDict = {
	'2/5' : mocks.R25,
	'callhome' : mocks.callhome
}
#add commands by following this format:
# from cmd import Cmd
 
# class MyPrompt(Cmd):
#    def do_exit(self, inp):
#         print("Bye")
#         return True
 
#    def do_add(self, inp):
#         print("Adding '{}'".format(inp))

# 	 def do_<func>(self, inp):
# 		  code here
 
# MyPrompt().cmdloop()
# print("after")

class MyPrompt(Cmd):
	def do_exit(self, inp):
		'''exit the application'''
		print("Bye")
		return True

	def do_Input(self, inp):
		print(inp)

	def do_showInterface(self, inp):
		#add other ok instances of inputs, this is so that putting showInterface noc101 returns an error instead of the noc101 text
		if(inp == '2/5'):
			print(mockDict.get(inp))

	def do_callhome(self, inp):
		'''displays the Call Home configuration'''
		if(inp == ''):
			print(mockDict.get('callhome'))

	def do_callhomeprofile(self, inp):
		'''displays the Call Home destination profile named Noc101'''
		if(inp == 'Noc101'):
			print(mockDict.get(inp))

	def do_cdpshowall(self, inp):
		if(inp == ''):
			print(mockDict.get('cdpall'))

	def do_cdpshowneighbors(self, inp):
		if(inp == ''):
			print(mockDict.get('cdpneighbors'))

	def do_cfsapplication(self, inp):
		if(inp == ''):
			print(mockDict.get('cfsapplication'))

	def do_cfsapplicationcallhome(self, inp):
		if(inp == ''):
			print(mockDict.get('cfsapplicationcallhome'))

	def do_cfslockcallhome(self, inp):
		if(inp == ''):
			print(mockDict.get('cfslockcallhome'))

	def do_config(self, inp):
		pass

	def shutdown(self,inp):
		pass


	do_EOF = do_exit

 
MyPrompt().cmdloop()



