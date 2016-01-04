from gi.repository import Gtk
import face_functions
import face_recognizer
import face_functions

class TableWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="FACE RECOGNIZER")
        self.set_size_request(500, 300)

        table = Gtk.Table(6, 3, True)
        self.add(table)
        hbox = Gtk.Box(spacing=6)
        self.button11 = Gtk.Button(label="NORMAL")
        hbox.pack_start(self.button11, True, True, 0)
        self.button11.connect("clicked", self.on_normal_clicked)
        self.button12 = Gtk.Button(label="HAPPY")
        hbox.pack_start(self.button12, True, True, 0)
        self.button12.connect("clicked", self.on_happy_clicked)
        self.button13 = Gtk.Button(label="SURPRISED")
        hbox.pack_start(self.button13, True, True, 0)
        self.button13.connect("clicked", self.on_surprised_clicked)
        self.button14 = Gtk.Button(label="WINK")
        hbox.pack_start(self.button14, True, True, 0)
        self.button14.connect("clicked", self.on_wink_clicked)
        self.button15 = Gtk.Button(label="SLEEPY")
        hbox.pack_start(self.button15, True, True, 0)
        self.button15.connect("clicked", self.on_sleepy_clicked)
        self.button16 = Gtk.Button(label="SAD")
        hbox.pack_start(self.button16, True, True, 0)
        self.button16.connect("clicked", self.on_sad_clicked)

        self.entry = Gtk.Entry()
        self.entry.set_text("Hello World")

        self.Entry1 = Gtk.Entry()
        self.Entry1.set_text("Enter your ID")
        
        
        button2 = Gtk.Button(label="BARCODE")
        button2.connect("clicked", self.on_barcode_clicked,"face_functions")
        button5 = Gtk.Button(label="SNAP")
        button5.connect("clicked", self.on_snap_clicked)
        button4 = Gtk.Button(label="Start Detector")
        button4.connect("clicked", self.on_start_clicked)
        self.label1 = Gtk.Label("Code token")
        self.label2 = Gtk.Label("Snap token")
        self.label3 = Gtk.Label("YES/NO")
        label4 = Gtk.Label("Admin Menu")
        label5 = Gtk.Label("User Menu")

        table.attach(self.Entry1, 0, 1, 1, 2)
        table.attach(hbox, 1, 3, 1, 2)
        table.attach(button2, 1, 2, 3, 4)
        table.attach(button5, 1, 2, 4, 5)
        table.attach(button4, 2, 3, 3, 6)
        table.attach(self.label1, 0, 1, 3, 4)
        table.attach(self.label2, 0, 1, 4, 5)
        table.attach(self.label3, 0, 2, 5, 6)
        table.attach(label4, 0, 3, 0, 1)
        table.attach(label5, 0, 3, 2, 3)
        
    def on_barcode_clicked(self, button,temp):
        print("")
    def on_snap_clicked(self, button):
        if (face_functions.take_picture("./tempSnap/subject"+".temp.png") == True):
            self.label2.set_markup("SNAP TOKEN")
        else:
            self.label2.set_text("Try again")
         
    def on_start_clicked(self, button):
        print("\"Click me\" button was clicked") 
        
        
    def on_normal_clicked(self, button): 
        face_functions.take_picture("./Database/subject"+self.Entry1.get_text()+".normal.png")
    def on_happy_clicked(self, button):
        face_functions.take_picture("./Database/subject"+self.Entry1.get_text()+".happy.png")
    def on_surprised_clicked(self, button):
        face_functions.take_picture("./Database/subject"+self.Entry1.get_text()+".surprised.png")
    def on_wink_clicked(self, button):
        face_functions.take_picture("./Database/subject"+self.Entry1.get_text()+".wink.png")
    def on_sleepy_clicked(self, button):
        face_functions.take_picture("./Database/subject"+self.Entry1.get_text()+".sleepy.png")
    def on_sad_clicked(self, button):
        face_functions.take_picture("./Database/subject"+self.Entry1.get_text()+".sad.png") 
 

win = TableWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()