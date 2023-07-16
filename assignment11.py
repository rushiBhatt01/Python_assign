import tkinter as tk
import webbrowser as wb



def subform():
    selection=var.get()
    
    if selection=="Instagram Ads":
        url="https://help.instagram.com/561062241952036"
    elif selection=="YT Ads":
        url="https://support.google.com/youtube/thread/202433711/frequently-asked-questions?hl=en"
    elif selection=="SnapChat Ads":
        url="https://help.snapchat.com/hc/en-us/articles/7012357237396-Frequently-Asked-Privacy-Questions"
    elif selection=="Flipkart Shopping Ads":
        url="https://seller.flipkart.com/sell-online/faq"
    else:
        pass
    
    wb.open_new(url)

window=tk.Tk(className="Course Enquiry Form")
label=tk.Label(window, text="Where did you hear about us?")
label.grid()

var=tk.StringVar()

options=["Instagram Ads", "YT Ads", "SnapChat Ads","Flipkart Shopping Ads"]
dropdown=tk.OptionMenu(window, var, *options)

dropdown.grid()

sub_but=tk.Button(window, text="Submit", command=subform)
sub_but.grid()

window.mainloop()

