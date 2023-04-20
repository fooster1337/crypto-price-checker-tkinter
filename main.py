from tkinter import *
from PIL import Image, ImageTk
import requests as fiola
root = Tk()

#crypto_name = root.StringVar()

def windowico():
    image = Image.open(r'bitcoin.png')
    ph = ImageTk.PhotoImage(image)
    root.wm_iconphoto(True, ph)

class Crypto:

    def __init__(self):
        self.crypto_name = StringVar()
        self.currency = StringVar()
        self.api = "https://api.coingecko.com/api/v3/simple/price?ids={}&vs_currencies={}"

    def crypto(self):
        try:

            get = Toplevel(root)
            get.geometry('200x100')
            req = fiola.get(self.api.format(self.crypto_name.get(), self.currency.get())).json()
            #getprice = cg.get_price(ids=self.crypto_name.get(), vs_currencies='usd')
            a = Label(get, text=f"Current Price : {self.crypto_name.get()}").pack()
            if req:
                getprice = req[self.crypto_name.get()][self.currency.get()]
                Label(get, text=f"{self.currency.get().upper()} : {getprice}").pack()
            else: Label(get, text="Coin/Currency Not Found").pack()

        except Exception as e: print(e); pass

    def main(self):
        blank = " "
        root.title(95*blank+"CryptoCurrency Checker")
        text = Entry(root, width=50, justify=CENTER, bg="blue", fg="white")
        text.insert(0, "CryptoCurrency Price Checker")
        text.pack(padx=50, pady=50)
        c = Label(root, justify=CENTER, fg="black", text="Enter Crypto Name", width=17, bg="yellow").pack()
        crypto = Entry(root, textvariable=self.crypto_name).pack()
        c = Label(root, justify=CENTER, fg="black", text="Enter Currency", width=17, bg="yellow").pack()
        currency = Entry(root, textvariable=self.currency).pack()
        #crypto.pack()
        confirm = Button(root, text='check', command=self.crypto)
        confirm.pack(side='top', padx=10, pady=10)
        

if __name__ == '__main__':
    root.geometry("800x600")
    windowico()
    Crypto().main()
    root.mainloop()
