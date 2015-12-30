from gi.repository import Gtk

class TableWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="FACE RECOGNIZER")
        self.set_size_request(500, 300)

        table = Gtk.Table(3, 3, True)
        self.add(table)
        hbox = Gtk.Box(spacing=6)
        hbox1 = Gtk.Box(spacing=6)
        #table1 = Gtk.Table(6, 1, True)
        self.button11 = Gtk.Button(label="NORMAL")
        hbox.pack_start(self.button11, True, True, 0)
        self.button12 = Gtk.Button(label="HAPPY")
        hbox.pack_start(self.button12, True, True, 0)
        self.button13 = Gtk.Button(label="SURPRISED")
        hbox.pack_start(self.button13, True, True, 0)
        self.button14 = Gtk.Button(label="WINK")
        hbox.pack_start(self.button14, True, True, 0)
        self.button15 = Gtk.Button(label="SLEEPY")
        hbox.pack_start(self.button15, True, True, 0)
        self.button16 = Gtk.Button(label="SAD")
        hbox.pack_start(self.button16, True, True, 0)

        self.entry = Gtk.Entry()
        self.entry.set_text("Hello World")

        self.Entry1 = Gtk.Entry()
        self.Entry1.set_text("Enter your ID")
        
        button2 = Gtk.Button(label="Button 2")
        button3 = Gtk.Button(label="Button 3")
        button4 = Gtk.Button(label="Start Detector")
        button5 = Gtk.Button(label="Button 5")
        button6 = Gtk.Button(label="BarCode Detector")

        table.attach(self.Entry1, 0, 1, 0, 1)
        table.attach(hbox, 1, 3, 0, 1)
        table.attach(hbox1, 0, 1, 1, 2)
        table.attach(button5, 1, 2, 2, 3)
        table.attach(button4, 2, 3, 1, 3)
        #table.attach(button6, 2, 3, 2, 3)

win = TableWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()