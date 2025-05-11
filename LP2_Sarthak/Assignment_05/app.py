import streamlit as st
from nltk.chat.util import Chat, reflections

# Data
car_variants = {
    'Polo': ['Trendline', 'Comfortline', 'Highline', 'GT Line'],
    'Golf': ['Life', 'Style', 'R-Line', 'GTI', 'R'],
    'Tiguan': ['Trendline', 'Comfortline', 'Highline', 'R-Line', 'Allspace']
}

car_engines = {
    'Polo': ['1.0L MPI (75 HP)', '1.0L TSI (95 HP)', '1.0L TSI (110 HP)', '1.5L TSI (150 HP)'],
    'Golf': ['1.5L TSI (130 HP)', '1.5L eTSI Mild Hybrid (150 HP)', '2.0L TSI (245 HP)', '2.0L TSI (320 HP)'],
    'Tiguan': ['1.5L TSI (150 HP)', '2.0L TSI (190 HP)', '2.0L TSI (245 HP)', '2.0L TDI (150 HP)', '2.0L TDI (200 HP)']
}

car_transmissions = {
    'Polo': ['5-Speed Manual', '6-Speed Manual', '7-Speed DSG Automatic'],
    'Golf': ['6-Speed Manual', '7-Speed DSG Automatic'],
    'Tiguan': ['6-Speed Manual', '7-Speed DSG Automatic', '8-Speed Automatic']
}

cars = {
    'Polo': ['Compact hatchback', 'Starting from INR 9,00,000', 'Features: Touchscreen infotainment, LED headlights'],
    'Golf': ['Versatile hatchback', 'Starting from INR 25,00,000', 'Features: Digital cockpit, adaptive cruise control'],
    'Tiguan': ['Compact SUV', 'Starting from INR 42,00,000', 'Features: Panoramic sunroof, 4MOTION all-wheel drive']
}

patterns = [
    (r'hi|hello|hey', ['Hello! How can I assist you with Volkswagen cars today?']),
    (r'how are you', ['I am a bot, but I am always ready to help you with VW car info!']),
    (r'(.*) car(.*)', ['Here are the VW models: Polo, Golf, Tiguan. Which one interests you?']),
    (r'(.*) (model|models)', ['We have Polo, Golf, and Tiguan. Which would you like to know more about?']),
    (r'(.*) (specs|specifications)', [
        ''.join([f"\n{car}: {', '.join(specs)}" for car, specs in cars.items()])
    ]),
    (r'(.*) (features?)', [
        ''.join([f"\n{car}: {specs[2]}" for car, specs in cars.items()])
    ]),
    (r'(.*) (variants?)', [
        ''.join([f"\n{car}: {', '.join(variants)}" for car, variants in car_variants.items()])
    ]),
    (r'(.*) (engines?)', [
        ''.join([f"\n{car}: {', '.join(engines)}" for car, engines in car_engines.items()])
    ]),
    (r'(.*) (transmissions?)', [
        ''.join([f"\n{car}: {', '.join(trans)}" for car, trans in car_transmissions.items()])
    ]),
    (r'(.*) polo variant(.*)', [f"Polo variants: {', '.join(car_variants['Polo'])}."]),
    (r'(.*) golf variant(.*)', [f"Golf variants: {', '.join(car_variants['Golf'])}."]),
    (r'(.*) tiguan variant(.*)', [f"Tiguan variants: {', '.join(car_variants['Tiguan'])}."]),
    (r'(.*) polo engine(.*)', [f"Polo engines: {', '.join(car_engines['Polo'])}."]),
    (r'(.*) golf engine(.*)', [f"Golf engines: {', '.join(car_engines['Golf'])}."]),
    (r'(.*) tiguan engine(.*)', [f"Tiguan engines: {', '.join(car_engines['Tiguan'])}."]),
    (r'(.*) polo transmission(.*)', [f"Polo transmissions: {', '.join(car_transmissions['Polo'])}."]),
    (r'(.*) golf transmission(.*)', [f"Golf transmissions: {', '.join(car_transmissions['Golf'])}."]),
    (r'(.*) tiguan transmission(.*)', [f"Tiguan transmissions: {', '.join(car_transmissions['Tiguan'])}."]),
    (r'(.*) polo', [f"Polo: {', '.join(cars['Polo'])}. Ask about variants, engines, or transmissions."]),
    (r'(.*) golf', [f"Golf: {', '.join(cars['Golf'])}. Ask about variants, engines, or transmissions."]),
    (r'(.*) tiguan', [f"Tiguan: {', '.join(cars['Tiguan'])}. Ask about variants, engines, or transmissions."]),
    (r'(.*) price(.*)', ['Prices vary by variant. Want to book an appointment for detailed pricing?']),
    (r'(.*) test drive(.*)', ['We can arrange a test drive at your nearest dealer. Shall I help?']),
    (r'(.*) (book|schedule|appointment)', ['Sure! Please fill the appointment form below.']),
    (r'(.*) (bye|goodbye)', ['Thanks for chatting with Volkswagen! Drive safe!'])
]

bot = Chat(patterns, reflections)

st.title("🚗 Volkswagen ChatBot")

# Session state init
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'chat_active' not in st.session_state:
    st.session_state.chat_active = True
if 'appointment_triggered' not in st.session_state:
    st.session_state.appointment_triggered = False

def send_message():
    if not st.session_state.chat_active:
        return
    user_msg = st.session_state.user_input
    response = bot.respond(user_msg)
    st.session_state.chat_history.append(("You", user_msg))
    
    # Stop bot if goodbye
    if response and "goodbye" in response.lower():
        st.session_state.chat_history.append(("VW Bot", response))
        st.session_state.chat_active = False
    else:
        st.session_state.chat_history.append(("VW Bot", response if response else "Sorry, I didn't understand that."))

    # Trigger appointment form if needed
    if response and "appointment form" in response.lower():
        st.session_state.appointment_triggered = True

    st.session_state.user_input = ''  # Clear input

# Chat history
for sender, msg in st.session_state.chat_history:
    st.markdown(f"**{sender}**: {msg}")

# Input field (only if chat is active)
if st.session_state.chat_active:
    st.text_input("Ask something about Volkswagen cars...", key="user_input", on_change=send_message)
else:
    st.markdown("🛑 Chat ended. Refresh to start over.")

# Appointment form
if st.session_state.appointment_triggered:
    st.markdown("### 📅 Appointment Form")
    with st.form("appointment_form"):
        name = st.text_input("Name")
        contact = st.text_input("Contact Number")
        car_model = st.selectbox("Car Model", list(cars.keys()))
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.success("✅ Appointment request received! Our team will contact you soon.")
            st.session_state.appointment_triggered = False



# To run this app:
# 1. Install dependencies: pip install streamlit nltk
# 2. Download NLTK data: python -m nltk.downloader punkt
# 3. Save this code as app.py
# 4. Run: streamlit run app.py