from gi.repository import Gtk
import face_functions
import face_recognizer
import barcode
import string
import os.path

class TableWindow(Gtk.Window):
    

    def __init__(self):
        Gtk.Window.__init__(self, title="FACE RECOGNIZER")
        self.set_size_request(500, 300)

        table = Gtk.Table(6, 3, True)
        self.add(table)
        hbox = Gtk.Box(spacing=6)
        self.take_picture_normal = Gtk.Button(label="NORMAL")
        hbox.pack_start(self.take_picture_normal, True, True, 0)
        self.take_picture_normal.connect("clicked", self.on_normal_clicked)
        self.take_picture_happy = Gtk.Button(label="HAPPY")
        hbox.pack_start(self.take_picture_happy, True, True, 0)
        self.take_picture_happy.connect("clicked", self.on_happy_clicked)
        self.take_picture_surprised = Gtk.Button(label="SURPRISED")
        hbox.pack_start(self.take_picture_surprised, True, True, 0)
        self.take_picture_surprised.connect("clicked", self.on_surprised_clicked)
        self.take_picture_wink = Gtk.Button(label="WINK")
        hbox.pack_start(self.take_picture_wink, True, True, 0)
        self.take_picture_wink.connect("clicked", self.on_wink_clicked)
        self.take_picture_sleepy = Gtk.Button(label="SLEEPY")
        hbox.pack_start(self.take_picture_sleepy, True, True, 0)
        self.take_picture_sleepy.connect("clicked", self.on_sleepy_clicked)
        self.take_picture_sad = Gtk.Button(label="SAD")
        hbox.pack_start(self.take_picture_sad, True, True, 0)
        self.take_picture_sad.connect("clicked", self.on_sad_clicked)

        self.Entry_ID = Gtk.Entry()
        self.Entry_ID.set_text("Enter your ID")
        
        Detection_Button = Gtk.Button(label="Start Detector")
        Detection_Button.connect("clicked", self.on_start_clicked)
        Label_Admin = Gtk.Label("Admin Menu")
        Label_User = Gtk.Label("User Menu")

        table.attach(self.Entry_ID, 0, 1, 1, 2)
        table.attach(hbox, 1, 3, 1, 2)
        table.attach(Detection_Button, 0, 3, 3, 6)
        table.attach(Label_Admin, 0, 3, 0, 1)
        table.attach(Label_User, 0, 3, 2, 3)
         
    def on_start_clicked(self, button):
        self.recognizer = face_recognizer.train_recognizer("./Database")
        img = face_functions.snap()
        predicted,conf = face_recognizer.recognize_face(self.recognizer, img)
        if(predicted==-1 or conf>50):
            message = Gtk.MessageDialog(self, 0, Gtk.MessageType.WARNING,Gtk.ButtonsType.CANCEL, "Face not recognized.")
            message.run()
            message.destroy()
            return
        
        message = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,Gtk.ButtonsType.CANCEL, "Face recognized!")
        message.format_secondary_text("Recognized as subject "+str(predicted)+" with a doubt rating of "+str(conf))
        message.run()
        message.destroy()

        d_barcode = barcode.get_barcode(img)
        if (len(d_barcode)>0): d_barcode=self.trim_barcode(d_barcode[0])
        message = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,Gtk.ButtonsType.CANCEL, "Barcode Detection")
        
        print(predicted)
        print("Barcode data found in this picture: " + str(d_barcode))
        if (len(d_barcode)==0):
            message.format_secondary_text("Barcode not detected.")
        elif (int(predicted)==int(d_barcode)):
            message.format_secondary_text("Barcode detected:" + d_barcode + "\nMatches with face.")
        else:
            message.format_secondary_text("Barcode detected:" + d_barcode + "\nDoes not match face.")
        message.run()
        message.destroy()
        #print("\"Click me\" button was clicked") 
    
    def id_is_valid(self):
        text = self.Entry_ID.get_text()
        if len(text)!=7:
            error_message = Gtk.MessageDialog(self, 0, Gtk.MessageType.ERROR,Gtk.ButtonsType.CANCEL, "ID must be exactly 7 digits long!")
            error_message.run()
            error_message.destroy()
            return False
        for ch in text:
            if(ch not in string.digits):
                error_message = Gtk.MessageDialog(self, 0, Gtk.MessageType.ERROR,Gtk.ButtonsType.CANCEL, "ID must contain numbers only!")
                error_message.run()
                error_message.destroy()
                return False
        return True
    
    def trim_barcode(self, barcode):
        return barcode[:7]
        
    def on_normal_clicked(self, button): 
        if(self.id_is_valid()): 
            face_functions.take_picture("./Database/subject"+self.Entry_ID.get_text()+".normal.png")
            if(os.path.isfile("./Database/subject"+self.Entry_ID.get_text()+".normal.png")):
                message = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,Gtk.ButtonsType.OK, "Picture taken")
                message.run()
                message.destroy()
            else:
                message = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,Gtk.ButtonsType.OK, "Error saving file - try again!")
                message.run()
                message.destroy()
    def on_happy_clicked(self, button):
        if(self.id_is_valid()): 
            face_functions.take_picture("./Database/subject"+self.Entry_ID.get_text()+".happy.png")
            if(os.path.isfile("./Database/subject"+self.Entry_ID.get_text()+".happy.png")):
                message = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,Gtk.ButtonsType.OK, "Picture taken")
                message.run()
                message.destroy()
            else:
                message = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,Gtk.ButtonsType.OK, "Error saving file - try again!")
                message.run()
                message.destroy()
    def on_surprised_clicked(self, button):
        if(self.id_is_valid()): 
            face_functions.take_picture("./Database/subject"+self.Entry_ID.get_text()+".surprised.png")
            if(os.path.isfile("./Database/subject"+self.Entry_ID.get_text()+".surprised.png")):
                message = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,Gtk.ButtonsType.OK, "Picture taken")
                message.run()
                message.destroy()
            else:
                message = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,Gtk.ButtonsType.OK, "Error saving file - try again!")
                message.run()
                message.destroy()
    def on_wink_clicked(self, button):
        if(self.id_is_valid()): 
            face_functions.take_picture("./Database/subject"+self.Entry_ID.get_text()+".wink.png")
            if(os.path.isfile("./Database/subject"+self.Entry_ID.get_text()+".wink.png")):
                message = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,Gtk.ButtonsType.OK, "Picture taken")
                message.run()
                message.destroy()
            else:
                message = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,Gtk.ButtonsType.OK, "Error saving file - try again!")
                message.run()
                message.destroy()
    def on_sleepy_clicked(self, button):
        if(self.id_is_valid()): 
            face_functions.take_picture("./Database/subject"+self.Entry_ID.get_text()+".sleepy.png")
            if(os.path.isfile("./Database/subject"+self.Entry_ID.get_text()+".sleepy.png")):
                message = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,Gtk.ButtonsType.OK, "Picture taken")
                message.run()
                message.destroy()
            else:
                message = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,Gtk.ButtonsType.OK, "Error saving file - try again!")
                message.run()
                message.destroy()
    def on_sad_clicked(self, button):
        if(self.id_is_valid()): 
            face_functions.take_picture("./Database/subject"+self.Entry_ID.get_text()+".sad.png") 
            if(os.path.isfile("./Database/subject"+self.Entry_ID.get_text()+".sad.png")):
                message = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,Gtk.ButtonsType.OK, "Picture taken")
                message.run()
                message.destroy()
            else:
                message = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,Gtk.ButtonsType.OK, "Error saving file - try again!")
                message.run()
                message.destroy()

win = TableWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()