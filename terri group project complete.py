import hashlib
import tkinter as tk
root=tk.Tk()
root.geometry("1200x100")
root.title("Robert, Matt, Jared, and Vlad's simple encryption application")
entrybox_var=tk.StringVar()
y=tk.StringVar()
y.set("encrypted ciphertext appears here")
console_label = tk.Label(root, textvariable=y)
entrybox_label = tk.Label(root, text = 'enter cleartext here')
entrybox_entry = tk.Entry(root, textvariable = entrybox_var)
#var1=hashlib.sha256()
entrybox=""

print(hashlib.algorithms_available)


def submit():
   
    entrybox_var.set("")
    print(entrybox)

def crypt(arg1):
    entrybox=entrybox_var.get()
    
    if(arg1==1):
        print("MD5 :")
        a=hashlib.md5()
        a.update(entrybox.encode('utf-8'))
        print(a.hexdigest())
        y.set(a.hexdigest())
    elif(arg1==2):
        print("SHA256 :")
        a=hashlib.sha256()
        a.update(entrybox.encode('utf-8'))
        print(a.hexdigest())
        y.set(a.hexdigest())    
    elif(arg1==3):
        print("SHA224 :")
        a=hashlib.sha224()
        a.update(entrybox.encode('utf-8'))
        print(a.hexdigest())
        y.set(a.hexdigest())
    elif (arg1==4):
        print("blake2b :")
        a=hashlib.blake2b()
        a.update(entrybox.encode('utf-8'))
        print(a.hexdigest())
        y.set(a.hexdigest())    


secretcowlevel=tk.Button(root,text = 'secret cow level', command =lambda:entrybox_var.set("moo moo moo"))

                             
btn_md5=tk.Button(root,text = 'md5', command =lambda: crypt(1))
btn_sha256=tk.Button(root,text = 'sha256', command = lambda:crypt(2))
btn_sha224=tk.Button(root,text = 'sha224', command = lambda:crypt(3))
btn_blake2b=tk.Button(root,text = 'blake2b', command = lambda:crypt(4))
sub_btn=tk.Button(root,text = 'clear', command =lambda: submit())
###########positioning##################
entrybox_label.grid(row=7,column=4)
entrybox_entry.grid(row=7,column=5)
btn_md5.grid(row=3,column=1)
btn_sha256.grid(row=3,column=2)
btn_sha224.grid(row=3,column=3)
btn_blake2b.grid(row=3,column=4)
secretcowlevel.grid(row=3,column=5)
sub_btn.grid(row=2,column=1)
console_label.grid(row=9,column=6, sticky="nesw")

root.mainloop()

#for algo in hashlib.algorithms_available:
    #a=hashlib.
    #a.update("clear text here")
    #print(a.digest())
#print(dir(hashlib))
