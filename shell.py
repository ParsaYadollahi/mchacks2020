from cmd import Cmd
 
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
	do_EOF = do_exit

 
MyPrompt().cmdloop()

