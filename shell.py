from cmd import Cmd
import mocks
 
mockDict = {
	'2/5' : mocks.R25
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
		print(mockDict.get(inp))

	def do_config(self, inp):
		pass

	def shutdown(self,inp):
		pass


	do_EOF = do_exit

 
MyPrompt().cmdloop()



