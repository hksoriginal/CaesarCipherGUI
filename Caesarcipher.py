from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import string
import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)


class caesar:
    def __init__(self, root):
        self.root = root
        self.root.geometry("950x800")
        self.root.title("Ceasar Cipher GUI")
        self.root.iconbitmap('cc.ico')
        

        alphabets = string.ascii_lowercase + string.ascii_lowercase
        # deleting text box content
        def delete_dec():
            dec_text_box.delete("1.0","end")
            d_shift.delete("0","end")
            decrypted_text_box.delete("1.0","end")
        def delete_enc():
            plain_text_box.delete("1.0","end")
            e_shift.delete("0","end")
            cipher_text_box.delete("1.0","end")

        # getting text for encryption
        def get_text_encrypt():
            plain_text = list((plain_text_box.get("1.0", END)).lower())
            # print(type(e_shift.get()))
            if (len(plain_text) < 2):
                messagebox.showerror("Warning!", "Nothing to Encrypt")
            else:
                try:
                    encrypt(plain_text, int(e_shift.get()))
                except:
                    messagebox.showerror("ERROR", "Only letters are allowed")

         # getting text for decryption       
        def get_text_decrypt():
            plain_text_d = list((dec_text_box.get("1.0", END)).lower())
            
            if (len(plain_text_d) < 2):
                messagebox.showerror("Warning!", "Nothing to Decrypt")
            else:
                try:
                    decrypt(plain_text_d, int(d_shift.get()))
                except:
                    messagebox.showerror("ERROR", "Only letters are allowed")

        # encryption function

        def encrypt(plain_text, shift_enc):
                shift_enc = int(shift_enc)
                
                for i in range(len(plain_text)-1):
                    if plain_text[i] == ' ':
                        plain_text[i] == ' '
                    else:
                        new_letter = alphabets.index(plain_text[i])+shift_enc
                        plain_text[i] = alphabets[new_letter]
                    encrypted = (''.join(map(str, plain_text)))
                cipher_text_box.insert("1.0", encrypted)
                

        # Decryption Function
        def decrypt(plain_text_d, shift_dec):
            shift_dec = int(shift_dec)
            for i in range(len(plain_text_d)-1):
                if plain_text_d[i] == ' ':
                    plain_text_d[i] == ' '
                else:
                    new_letter = alphabets.index(plain_text_d[i])-shift_dec
                    plain_text_d[i] = alphabets[new_letter]
                decrypted = (''.join(map(str, plain_text_d)))
            decrypted_text_box.insert("1.0", decrypted)
            
            

        # background
        background = Image.open('bg.png')
        background = background.resize((950, 800), Image.ANTIALIAS)
        self.ph_img = ImageTk.PhotoImage(background)
        label_bg = Label(self.root, image=self.ph_img)
        label_bg.place(x=0, y=0, width=950, height=800)

        # logo
        logo = Image.open('8.png')
        logo = logo.resize((360, 100), Image.ANTIALIAS)
        self.logo_img = ImageTk.PhotoImage(logo)
        label_logo = Label(self.root, image=self.logo_img, bd=0)
        label_logo.place(x=0, y=0, width=360, height=100)

        # encryption
        
        e_shift = Entry(root, justify=CENTER,font=("Comfortaa", 12, "bold"))
        e_shift.place(x=150, y=430, width=200, height=50)

        enc = Label(root, text="Encryption", fg="white", bg="#0071BC",
                    font=("Comfortaa", 17, "bold"), relief="groove")
        enc.place(x=100, y=140, width=300, height=50)

        plain_text_box = Text(root, width=300, bd=3,
                              font=("Comfortaa", 12, "bold"))
        plain_text_box.place(x=100, y=200, width=300, height=200)

        cipher_text_box = Text(root, width=300, bd=3,
                               font=("Comfortaa", 12, "bold"))
        cipher_text_box.place(x=100, y=510, width=300, height=200)
       

        
        e_img = Image.open('enc.png')
        e_img = e_img.resize((50, 50), Image.ANTIALIAS)
        self.e_img = ImageTk.PhotoImage(e_img)
        e_enc = Button(root, image=self.e_img, bd=1, cursor="hand2",command=get_text_encrypt)
        e_enc.place(x=100, y=430, width=50, height=50)

        clr_img_en = Image.open('12.png')#clear button
        clr_img_en = clr_img_en.resize((50, 50), Image.ANTIALIAS)
        self.clr_img_en = ImageTk.PhotoImage(clr_img_en)
        e_clr = Button(root, image=self.clr_img_en, bd=1, cursor="hand2" ,command=delete_enc)
        e_clr.place(x=350, y=430, width=50, height=50)
       

        

        # decryption
        dec = Label(root, text="Decryption", fg="white", bg="#39B54A",
                    font=("Comfortaa", 17, "bold"), relief="groove")
        dec.place(x=520, y=140, width=300, height=50)

        dec_text_box = Text(root, width=300, bd=3, font=(
            "Comfortaa", 12, "bold"))
        dec_text_box.place(x=520, y=200, width=300, height=200)

        decrypted_text_box = Text(root, width=300, bd=3,
                                  font=("Comfortaa", 12, "bold"))
        decrypted_text_box.place(x=520, y=510, width=300, height=200)
        

        
        d_shift = Entry(root, justify=CENTER,font=("Comfortaa", 12, "bold"))
        d_shift.place(x=570, y=430, width=200, height=50)

        d_img = Image.open('dec.png')
        d_img = d_img.resize((50, 50), Image.ANTIALIAS)
        self.d_img = ImageTk.PhotoImage(d_img)
        d_dec = Button(root, image=self.d_img, bd=1, cursor="hand2" ,command=get_text_decrypt)
        d_dec.place(x=520, y=430, width=50, height=50)

        clr_img = Image.open('13.png')#clear button
        clr_img = clr_img.resize((50, 50), Image.ANTIALIAS)
        self.clr_img = ImageTk.PhotoImage(clr_img)
        d_clr = Button(root, image=self.clr_img, bd=1, cursor="hand2" ,command=delete_dec)
        d_clr.place(x=770, y=430, width=50, height=50)
       

        # ___________________________________

        


if __name__ == '__main__':
    root = Tk()
    obj = caesar(root)
    messagebox.showinfo("Welcome","Hi,\nThis Caesar Cipher GUI is developed by hksoriginal")
    root.resizable(False, False)
    root.mainloop()
