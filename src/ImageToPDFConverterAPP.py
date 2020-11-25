from PIL import Image
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


class ImageToPDFConverterAPP:

    def __init__(self):
        super().__init__()
        self.root = tk.Tk()

        self.canvas1 = tk.Canvas(self.root, width=300, height=300,
                                 bg='grey85', relief='raised')
        self.canvas1.pack()

        self.label1 = tk.Label(
            self.root, text='Images to PDF', bg='grey85')
        self.label1.config(font=('helvetica', 20))
        self.canvas1.create_window(150, 60, window=self.label1)

        self.images_list = list()

        self.browseButton = tk.Button(text="     Select Files     ", command=self.getFiles,
                                      bg='DarkOrchid', fg='white', font=('helvetica', 12, 'bold'))
        self.canvas1.create_window(150, 130, window=self.browseButton)

        self.saveAsButton = tk.Button(text='Convert to PDF', command=self.convertToPdf,
                                      bg='DarkOrchid', fg='white', font=('helvetica', 12, 'bold'))
        self.canvas1.create_window(150, 180, window=self.saveAsButton)

        ##############

        self.root.mainloop()

    def getFiles(self):

        try:
            import_file_path = filedialog.askopenfilenames()
            print(import_file_path)
            self.images_list = list()
            for eachFile in import_file_path:
                image = Image.open(eachFile)
                self.images_list.append(image.convert('RGB'))

        except Exception as e:
            print(e)
            messagebox.showinfo(
                "error", "Something went wrong...! Try again..")

    ##################

    def convertToPdf(self):

        try:
            if len(self.images_list) > 0:
                export_file_path = filedialog.asksaveasfilename(
                    defaultextension='.pdf')
                self.images_list[0].save(export_file_path, save_all=True,
                                         append_images=self.images_list[1:])
                # set the images_list to empty list again
                self.images_list = list()
                print("PDF generated successfully...🔑✔✔😎")
            else:
                messagebox.showinfo("error", "Please select images to convert")
        except Exception as e:
            print(e)


def runImageToPDFConverterApp():
    ImageToPDFConverterAPP()


if __name__ == "__main__":
    a = ImageToPDFConverterAPP()
