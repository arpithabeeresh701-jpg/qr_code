import stream as st
import qrcode
from PIL import image
#page title
st.title("qrcode generator")
data =st.text_input("enter url")
 if st.button("generator qr"):
    if data:
        qr=qrcode.make(data)
        qr.save("gr.png")
        img=image.open("qr.png")
        st.image(img,caption="generated qrcode")
        with open ("qr.png","rb")as f:
           st.dowload_button("Download QR",f,file_name="qr.png")
   else:
       st.warning("please enter some text")

