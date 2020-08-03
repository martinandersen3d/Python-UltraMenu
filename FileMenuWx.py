import wx  

class Mywin(wx.Frame): 
            
   def __init__(self, parent, title): 
      super(Mywin, self).__init__(parent, title = title, size = (250,150))  
      self.InitUI() 
         
   def InitUI(self):    
      menubar = wx.MenuBar() 
		
      fileMenu = wx.Menu() 
      newitem = wx.MenuItem(fileMenu,wx.ID_NEW, text = "New",kind = wx.ITEM_NORMAL) 
      newitem.SetBitmap(wx.Bitmap("new.bmp")) 
      fileMenu.AppendItem(newitem) 
		
      fileMenu.AppendSeparator()
		
      editMenu = wx.Menu() 
      copyItem = wx.MenuItem(editMenu, 100,text = "copy",kind = wx.ITEM_NORMAL)
      copyItem.SetBitmap(wx.Bitmap("copy.bmp")) 
		
      editMenu.AppendItem(copyItem) 
      cutItem = wx.MenuItem(editMenu, 101,text = "cut",kind = wx.ITEM_NORMAL) 
      cutItem.SetBitmap(wx.Bitmap("cut.bmp")) 
		
      editMenu.AppendItem(cutItem) 
      pasteItem = wx.MenuItem(editMenu, 102,text = "paste",kind = wx.ITEM_NORMAL) 
      pasteItem.SetBitmap(wx.Bitmap("paste.bmp")) 
		
      editMenu.AppendItem(pasteItem) 
      fileMenu.AppendMenu(wx.ID_ANY, "Edit", editMenu) 
      fileMenu.AppendSeparator() 
         
      radio1 = wx.MenuItem(fileMenu, 200,text = "Radio1",kind = wx.ITEM_RADIO) 
      radio2 = wx.MenuItem(fileMenu, 300,text = "radio2",kind = wx.ITEM_RADIO) 
		
      fileMenu.AppendItem(radio1) 
      fileMenu.AppendItem(radio2) 
      fileMenu.AppendSeparator() 
         
      fileMenu.AppendCheckItem(103,"Checkable") 
      quit = wx.MenuItem(fileMenu, wx.ID_EXIT, '&Quit\tCtrl+Q') 
		
      fileMenu.AppendItem(quit) 
      menubar.Append(fileMenu, '&File') 
		
      self.SetMenuBar(menubar) 
      self.text = wx.TextCtrl(self,-1, style = wx.EXPAND|wx.TE_MULTILINE) 
      self.Bind(wx.EVT_MENU, self.menuhandler) 
      self.SetSize((350, 250)) 
      self.Centre() 
      self.Show(True)
		
   def menuhandler(self, event): 
      id = event.GetId() 
      if id == wx.ID_NEW: 
         self.text.AppendText("new"+"\n")
			
ex = wx.App() 
Mywin(None,'MenuBar demo') 
ex.MainLoop() 