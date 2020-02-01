from cmd import Cmd
import mocks
 
mockDict = {
	'2/5' : mocks.R25,
	'callhome' : mocks.callhome,
	'Noc101' : mocks.Noc101,
	'cdpall' : mocks.cdpall,
	'cdpneighbors' : mocks.cdpneighbors,
	'cfsapplication' : mocks.cfsapplication,
	'cfsapplicationcallhome' : mocks.cfsapplicationcallhome,
	'cfslockcallhome' : mocks.cfslockcallhome,
	'cfsregionsbrief' : mocks.cfsregionsbrief,
	'cfsregionsregion 4' : mocks.cfsregionsregion4,
	'cfsstatus' : mocks.cfsstatus,
	'checkpointstable' : mocks.checkpointstable,
	'configurationsessionmyACLs' : mocks.configurationsessionmyACLs,
	'configurationsessionstatus' : mocks.configurationsessionstatus,
	'configurationsessionsummary' : mocks.configurationsessionsummary
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

	def do_cfsregions(self, inp):
		'''try brief or region 4'''
		if(inp in {'brief', 'region 4'}):
			print(mockDict.get('cfsregions'+inp))

	def do_cfs(self, inp):
		if(inp == 'status'):
			print(mockDict.get('cfsstatus'))
		if(inp == 'application'):
			print(mockDict.get('cfsapplication'))
		if(inp == 'application name callhome'):
			print(mockDict.get('cfsapplicationcallhome'))
		if(inp == 'lock name callhome'):
			print(mockDict.get('cfslockcallhome'))
		if(inp == 'peers name callhome'):
			print(mockDict.get('cfspeerscallhome'))

	def do_checkpoint(self, inp):
		if(inp == 'stable'):
			print(mockDict.get('checkpointstable'))

	def do_configuration(self, inp):
		if(inp == 'session myACLS'):
			print(mockDict.get('configurationsessionmyACLs'))
		if(inp == 'session status'):
			print(mockDict.get('configurationsessionstatus'))
		if(inp == 'session summary'):
			print(mockDict.get('configurationsessionsummary'))





	def do_config(self, inp):
		pass

	def shutdown(self,inp):
		pass


	do_EOF = do_exit

 
MyPrompt().cmdloop()



