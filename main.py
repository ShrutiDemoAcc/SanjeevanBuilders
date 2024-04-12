import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title="My Homepage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
FileUrl = load_lottieurl("https://lottie.host/16c2863d-2ee6-4699-979e-a9cb1a0d723b/6lLOKzEUVf.json")
Img_contact_form = Image.open("ima\output.png")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>" , unsafe_allow_html=True)

local_css("roorDir/style.css")

st.subheader("Hi, I am Sagar Patil from Kolhapur, Maharashtra :wave:")
st.title("Builder, Contractor, Constructor, Consultor, Designer, Planner")
st.write(" Construction of row house, Bunglows, Houses, Shops, Godowns and many more services for your lovely dwelling place.")
    #st.writer("[learn more > ] (instagram.com)")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("what I do?")
        st.write("##")
        st.write(
            """
            We specialize in all aspects of home and commercial, construction
            including new builds, renovation, remodels, repairs.
            
            We pride ourselves on providing quality workmanship, excellent customer service
            and at best pricing.
            
            
            WE PLAN BETTER, 
                           WE BUILD BETTER....
            """
        )
        st.write("to be updated links here of Twitter,FB, instagram")

    with right_column:
        st_lottie(FileUrl, height=300, key = None)

#lottie file
#https://lottie.host/16c2863d-2ee6-4699-979e-a9cb1a0d723b/6lLOKzEUVf.json


with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(Img_contact_form)
        #insert image


    with text_column:
        st.subheader("This is my recently completed project...")
        st.write(
            """
            Address: Kolhapur, Maharashtra.
            
            Requirement:1BHK
            
            
            Status:Done:) 
            
            """
        )

with st.container():
    st.write("---")
    st.header("get in touch with me!")
    st.write("##")
    #go to formsubmit.co
    # contact_form =(
    # """
    # <form action="https://formsubmit.co/shrutipatil2204@gmail.com" method="POST">
    #  <input type="text" name="name" placeholder="Your name" required>
    #  <input type="email" name="email" placeholder=Email email" required>
    #  <textarea name="message" placeholder="Your message here" required></textarea>
    #
    #  <button type="submit">Send</button>
    # </form>
    # <form action="https://formsubmit.co/shrutipatil2204@gmail.com" method="POST">
    #     <input type="hidden" name="_captcha" value="false">
    #     <input type="text" name="name" placeholder="Your name" required>
    #     <input type="email" name="email" placeholder="Your email" required>
    #     <textarea name="message" placeholder="Your message here" required></textarea>
    #     <button type="submit">Send</button>
    # </form>
    # """
    # )
    contact_form = """
        <form action="https://formsubmit.co/patil.sagar18995@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st.empty()


#change theme https://blog.streamlit.io/introducing-theming/


