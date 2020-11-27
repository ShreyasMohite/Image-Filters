from tkinter import *
from PIL import Image
import tkinter.messagebox
from PIL import ImageTk
from PIL import *
from tkinter import filedialog
import threading
from tkinter.ttk import Combobox
from PIL import ImageFilter





class Img_filter:
    def __init__(self,root):
        self.root=root
        self.root.title("Image filter")
        self.root.geometry("500x400")
        self.root.iconbitmap("logo328.ico")
        self.root.resizable(0,0)


        save=StringVar()
        color=StringVar()
        fil=StringVar()



        def browse():           
            global filename
            global photo_image
            file_path = filedialog.askopenfilename(title = "Select file",filetypes = (("Jpeg files","*.jpg"),("png files","*.png"),("all files","*.*"))) 
            filename =file_path
            self.original = Image.open(file_path)
            resized = self.original.resize((355,160),Image.ANTIALIAS)
            self.image = ImageTk.PhotoImage(resized)
            photo_image=Label(firstframe,image=self.image,bd=2)
            photo_image.place(x=65,y=65)





        def convert():
            try:
                if len(filename)!=0:
                    if save.get()!="":
                        if color.get()!="Select Color":
                            if fil.get()!="Select Filter":
                                if fil.get()=='BLUR':
                                    image_file = Image.open(filename)
                                    image_file = image_file.convert(color.get())
                                    im1 = image_file.filter(ImageFilter.BLUR)
                                    im1.save("{}.png".format(save.get()))
                                    tkinter.messagebox.showinfo("Great","Image created successfully")

                                if fil.get()=='CONTOUR':
                                    image_file = Image.open(filename)
                                    image_file = image_file.convert(color.get())
                                    im1 = image_file.filter(ImageFilter.CONTOUR)
                                    im1.save("{}.png".format(save.get()))
                                    tkinter.messagebox.showinfo("Great","Image created successfully")

                                if fil.get()=='DETAIL':
                                    image_file = Image.open(filename)
                                    image_file = image_file.convert(color.get())
                                    im1 = image_file.filter(ImageFilter.DETAIL)
                                    im1.save("{}.png".format(save.get()))
                                    tkinter.messagebox.showinfo("Great","Image created successfully")

                                if fil.get()=='EDGE_ENHANCE':
                                    image_file = Image.open(filename)
                                    image_file = image_file.convert(color.get())
                                    im1 = image_file.filter(ImageFilter.EDGE_ENHANCE)
                                    im1.save("{}.png".format(save.get()))
                                    tkinter.messagebox.showinfo("Great","Image created successfully")

                                if fil.get()=='EDGE_ENHANCE_MORE':
                                    image_file = Image.open(filename)
                                    image_file = image_file.convert(color.get())
                                    im1 = image_file.filter(ImageFilter.EDGE_ENHANCE_MORE)
                                    im1.save("{}.png".format(save.get()))
                                    tkinter.messagebox.showinfo("Great","Image created successfully")

                                if fil.get()=='EMBOSS':
                                    image_file = Image.open(filename)
                                    image_file = image_file.convert(color.get())
                                    im1 = image_file.filter(ImageFilter.EMBOSS)
                                    im1.save("{}.png".format(save.get()))
                                    tkinter.messagebox.showinfo("Great","Image created successfully")

                                if fil.get()=='FIND_EDGES':
                                    image_file = Image.open(filename)
                                    image_file = image_file.convert(color.get())
                                    im1 = image_file.filter(ImageFilter.FIND_EDGES)
                                    im1.save("{}.png".format(save.get()))
                                    tkinter.messagebox.showinfo("Great","Image created successfully")

                                if fil.get()=='SHARPEN':
                                    image_file = Image.open(filename)
                                    image_file = image_file.convert(color.get())
                                    im1 = image_file.filter(ImageFilter.SHARPEN)
                                    im1.save("{}.png".format(save.get()))
                                    tkinter.messagebox.showinfo("Great","Image created successfully")

                                if fil.get()=='SMOOTH':
                                    image_file = Image.open(filename)
                                    image_file = image_file.convert(color.get())
                                    im1 = image_file.filter(ImageFilter.SMOOTH)
                                    im1.save("{}.png".format(save.get()))
                                    tkinter.messagebox.showinfo("Great","Image created successfully")

                                if fil.get()=='SMOOTH_MORE':
                                    image_file = Image.open(filename)
                                    image_file = image_file.convert(color.get())
                                    im1 = image_file.filter(ImageFilter.SMOOTH_MORE)
                                    im1.save("{}.png".format(save.get()))
                                    tkinter.messagebox.showinfo("Great","Image created successfully")

                            else:
                                tkinter.messagebox.showerror("Error","Please Select the filter")
                        else:
                            tkinter.messagebox.showerror("Error","Please Select the filter")

                    else:
                        tkinter.messagebox.showerror("Error","Please Enter Save Name")
                else:
                    tkinter.messagebox.showerror("Error","Please Select Image")
            except Exception as e:
                tkinter.messagebox.showerror("Error",e)

        def thread_convert():
            t=threading.Thread(target=convert)
            t.start()
        




        def on_enter1(e):
            but_convert_ascii['background']="black"
            but_convert_ascii['foreground']="cyan"  
        def on_leave1(e):
            but_convert_ascii['background']="SystemButtonFace"
            but_convert_ascii['foreground']="SystemButtonText"
                           

        def on_enter2(e):
            but_clear['background']="black"
            but_clear['foreground']="cyan"  
        def on_leave2(e):
            but_clear['background']="SystemButtonFace"
            but_clear['foreground']="SystemButtonText"

        def on_enter3(e):
            but_Browse['background']="black"
            but_Browse['foreground']="cyan"  
        def on_leave3(e):
            but_Browse['background']="SystemButtonFace"
            but_Browse['foreground']="SystemButtonText"





        def clear():
            save.set("")
            photo_image.config(image="")
            lab_success.config(text="")
            fil.set("Select Filter")
            color.set("Select Color")


#==========================frame=================================================#

        mainframe=Frame(self.root,width=500,height=400,relief="ridge",bd=3)
        mainframe.place(x=0,y=0)

        firstframe=Frame(mainframe,width=493,height=350,relief="ridge",bd=3,bg="black")
        firstframe.place(x=0,y=0)

        secondframe=Frame(mainframe,width=493,height=45,relief="ridge",bd=3)
        secondframe.place(x=0,y=350)

#===========================firstframe==================================================#
        
        but_Browse=Button(firstframe,text="Browse",width=15,font=('times new roman',12),cursor="hand2",command=browse)
        but_Browse.place(x=170,y=10)
        but_Browse.bind("<Enter>",on_enter3)
        but_Browse.bind("<Leave>",on_leave3)


        global photo_image
        self.original = Image.open("C:/Users/SHREYAS/Desktop/shreyas python/img_ascii/black.png")
        resized = self.original.resize((355,160),Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(resized)
        #bglab=Label(F1,image=self.image,bd=2).place(x=0,y=0)
        photo_image=Label(firstframe,image=self.image,bd=2)
        photo_image.place(x=65,y=65)



        lab_save=Label(firstframe,text="Save As Name",font=('times new roman',12),bg="black",fg="white")
        lab_save.place(x=30,y=250)

        ent_save=Entry(firstframe,width=30,font=('times new roman',12),relief="ridge",bd=3,textvariable=save)
        ent_save.place(x=170,y=250)

        lab_success=Label(firstframe,text="",font=('times new roman',12),bg="black",fg="white")
        lab_success.place(x=120,y=300)

        lab_please_filter=Label(firstframe,text="Please Select Filter",font=('times new roman',12),bg="black",fg="white")
        lab_please_filter.place(x=30,y=300)

        colo=['L','1']
        colo_combo=Combobox(firstframe,values=colo,font=('arial',10),width=14,state="readonly",textvariable=color)
        colo_combo.set("Select Color")
        colo_combo.place(x=170,y=300)

        filters=['BLUR','CONTOUR','DETAIL','EDGE_ENHANCE',\
                 'EDGE_ENHANCE_MORE','EMBOSS','FIND_EDGES',\
                 'SHARPEN','SMOOTH','SMOOTH_MORE']
        filters_combo=Combobox(firstframe,values=filters,font=('arial',10),width=14,state="readonly",textvariable=fil)
        filters_combo.set("Select Filter")
        filters_combo.place(x=300,y=300)


    

#=========================secondframe==================================================#
        but_convert_ascii=Button(secondframe,width=18,text="Convert Image",font=('times new roman',12),cursor="hand2",command=thread_convert)
        but_convert_ascii.place(x=40,y=5)
        but_convert_ascii.bind("<Enter>",on_enter1)
        but_convert_ascii.bind("<Leave>",on_leave1)

        but_clear=Button(secondframe,width=18,text="Clear",font=('times new roman',12),cursor="hand2",command=clear)
        but_clear.place(x=270,y=5)
        but_clear.bind("<Enter>",on_enter2)
        but_clear.bind("<Leave>",on_leave2)



        


   





if __name__ == "__main__":
    root=Tk()
    Img_filter(root)
    root.mainloop()
