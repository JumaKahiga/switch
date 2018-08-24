import os
import wx

class Ligo(wx.Frame):
	def __init__(self, parent, title):
		super(Ligo, self).__init__(parent, title='Ligo', size=(0,0))
		self.Move((0,0))

def main():
	app= wx.App()
	mimi= Ligo(None, title='Moving')
	mimi.Show()
	app.MainLoop()

if __name__ == '__main__':
	main()
print ("Starting programs termination......")

os.system ("taskkill /f /im notepad.exe")
os.system("taskkill /f /im winword.exe")
os.system("taskkill /f /im excel.exe")
os.system("taskkill /f /im SnippingTool.exe")
os.system("taskkill /f /im outlook.exe")
os.system("taskkill /f /im chrome.exe")
os.system("taskkill /f /im calc.exe")
os.system("taskkill /f /im iexplore.exe")
os.system("taskkill /f /im powershell.exe")
os.system("taskkill /f /im wordpad.exe")
os.system("taskkill /f /im firefox.exe")
#os.system("taskkill /f /im explorer.exe")

print ('.......Programs terminated')

insight= int(input("Do you want to restart the computer. Yes=1, No=2: "))
print (insight)

#os.system('shutdown /s /t 1')

if insight==1:
	os.system('shutdown /r /t 1')
	print ("Computer shutting down in 3 seconds")
else:
	print ("Clean up done")		