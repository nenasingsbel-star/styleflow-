import streamlit as st
from datetime import datetime, timedelta
import base64
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="StyleFlow - Fashion Planner",
    page_icon="👗",
    layout="wide",
    initial_sidebar_state="collapsed"
)
# Custom CSS for pink theme and styling
st.markdown("""
<style>
    /* Import Pacifico font */
    @import url('https://fonts.googleapis.com/css2?family=Pacifico&display=swap');
    
    /* Global styling */
    .stApp {
        background: linear-gradient(180deg, #fce7f3 0%, #ffffff 100%);
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Custom title styling */
    .main-title {
        font-family: 'Pacifico', cursive;
        font-size: 3rem;
        background: linear-gradient(135deg, #ec4899, #f9a8d4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    
    .subtitle {
        text-align: center;
        color: #831843;
        opacity: 0.8;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
    
    /* Welcome screen styling */
    .welcome-container {
        background: linear-gradient(180deg, #fce7f3 0%, white 100%);
        padding: 3rem;
        border-radius: 2rem;
        text-align: center;
        box-shadow: 0 10px 40px rgba(236, 72, 153, 0.2);
    }
    
    .welcome-icon {
        font-size: 5rem;
        margin-bottom: 1rem;
    }
    
    .welcome-title {
        font-family: 'Pacifico', cursive;
        font-size: 2rem;
        color: #831843;
        margin-bottom: 1rem;
    }
    
    .welcome-text {
        color: #831843;
        opacity: 0.7;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }
    
    /* Button styling */
    .stButton>button {
        background: linear-gradient(135deg, #ec4899, #f9a8d4);
        color: white;
        border: none;
        padding: 1rem 3rem;
        border-radius: 2rem;
        font-size: 1.1rem;
        font-weight: 700;
        box-shadow: 0 10px 30px rgba(236, 72, 153, 0.4);
        width: 100%;
    }
    
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 15px 40px rgba(236, 72, 153, 0.5);
    }
    
    /* Option card styling */
    .option-card {
        background: linear-gradient(135deg, #fce7f3, #fbcfe8);
        border-radius: 1.5rem;
        padding: 1.5rem;
        margin-bottom: 1rem;
        box-shadow: 0 5px 20px rgba(236, 72, 153, 0.2);
        cursor: pointer;
        transition: all 0.3s;
    }
    
    .option-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(236, 72, 153, 0.3);
    }
    
    .option-title {
        font-size: 1.3rem;
        font-weight: 700;
        color: #831843;
        margin-bottom: 0.3rem;
    }
    
    .option-desc {
        font-size: 0.9rem;
        color: #831843;
        opacity: 0.7;
    }
    
    /* Day card styling */
    .day-card {
        background: white;
        border-radius: 1rem;
        padding: 1.5rem;
        border: 2px solid transparent;
        margin-bottom: 1rem;
        transition: all 0.3s;
    }
    
    .day-card:hover {
        border-color: #ec4899;
        transform: scale(1.02);
    }
    
    /* Upload zone styling */
    .upload-zone {
        border: 2px dashed #f9a8d4;
        border-radius: 1rem;
        padding: 2rem;
        text-align: center;
        background: #fce7f3;
        margin: 1rem 0;
    }
    
    /* Header styling */
    .page-header {
        background: linear-gradient(135deg, #ec4899, #f9a8d4);
        color: white;
        padding: 1.5rem;
        border-radius: 1rem;
        margin-bottom: 2rem;
    }
    
    .page-header h2 {
        color: white;
        margin: 0;
    }
    
    /* Accessory button styling */
    .accessory-btn {
        background: #fbcfe8;
        border: 2px solid #f9a8d4;
        padding: 0.75rem 1.25rem;
        border-radius: 0.75rem;
        margin: 0.25rem;
        display: inline-block;
        cursor: pointer;
    }
    
    /* Section styling */
    .section-container {
        background: #fce7f3;
        border-radius: 1.5rem;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
    }
    
    .section-title {
        font-size: 1.3rem;
        font-weight: 700;
        color: #831843;
        margin-bottom: 1rem;
    }
    
    /* Sparkle animation */
    @keyframes sparkle {
        0%, 100% { opacity: 1; transform: scale(1) rotate(0deg); }
        50% { opacity: 0.5; transform: scale(1.2) rotate(180deg); }
    }
    
    .sparkle {
        animation: sparkle 2s ease-in-out infinite;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'welcome'
if 'occasion_type' not in st.session_state:
    st.session_state.occasion_type = None
if 'outfits' not in st.session_state:
    st.session_state.outfits = {}
if 'wardrobe' not in st.session_state:
    st.session_state.wardrobe = []
if 'events' not in st.session_state:
    st.session_state.events = []

# Navigation functions
def go_to_page(page, occasion_type=None):
    st.session_state.page = page
    if occasion_type:
        st.session_state.occasion_type = occasion_type
    st.rerun()

# Welcome Screen
def welcome_screen():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div class="welcome-container">
            <div class="welcome-icon">✨👗💖</div>
            <h1 class="welcome-title">Welcome to the World of Fashion</h1>
            <p class="welcome-text">Make convenience good for you</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Get Started ✨", key="get_started"):
            go_to_page('occasion_select')

# Occasion Selection Screen
def occasion_selection_screen():
    st.markdown('<h1 class="main-title">Fashion World ✨</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Your Personal Style Companion</p>', unsafe_allow_html=True)
    
    st.markdown('<div class="page-header"><h2>What are you using this app for? 👗</h2></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="option-card">
            <div class="option-title">Everyday</div>
            <div class="option-desc">Plan your weekly outfits</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Select Everyday", key="everyday", use_container_width=True):
            go_to_page('weekly_planner', 'everyday')
        
        st.markdown("""
        <div class="option-card">
            <div class="option-title">Both</div>
            <div class="option-desc">Everything combined</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Select Both", key="both", use_container_width=True):
            go_to_page('weekly_planner', 'both')
    
    with col2:
        st.markdown("""
        <div class="option-card">
            <div class="option-title">Special Occasions</div>
            <div class="option-desc">Dates, events & parties</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Select Special Occasions", key="special", use_container_width=True):
            go_to_page('occasion_types', 'special')
        
        st.markdown("""
        <div class="option-card">
            <div class="option-title">Other</div>
            <div class="option-desc">Customize your needs</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Select Other", key="other", use_container_width=True):
            go_to_page('custom_occasion', 'other')

# Weekly Planner Screen
def weekly_planner_screen():
    st.markdown('<div class="page-header"><h2>📅 Weekly Planner</h2><p>Plan your looks</p></div>', unsafe_allow_html=True)
    
    if st.button("← Back", key="back_from_weekly"):
        go_to_page('occasion_select')
    
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    day_abbr = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    
    for i, (day, abbr) in enumerate(zip(days, day_abbr)):
        st.markdown(f"""
        <div class="day-card">
            <div style="display: flex; align-items: center; justify-content: space-between;">
                <div style="display: flex; align-items: center;">
                    <div style="width: 3rem; height: 3rem; background: #fce7f3; border-radius: 0.75rem; 
                         display: flex; align-items: center; justify-content: center; font-weight: 700; 
                         color: #ec4899; margin-right: 1rem;">{abbr}</div>
                    <div>
                        <h3 style="margin: 0; color: #831843;">{day}</h3>
                        <p style="margin: 0; font-size: 0.8rem; color: #831843; opacity: 0.6;">
                            {'Outfit planned' if f'{day}' in st.session_state.outfits else 'Plan your look'}
                        </p>
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns([3, 1])
        with col1:
            outfit_file = st.file_uploader(f"Upload outfit for {day}", type=['jpg', 'jpeg', 'png'], key=f"outfit_{day}")
            if outfit_file:
                st.session_state.outfits[day] = outfit_file
                st.image(outfit_file, caption=f"{day}'s Outfit", use_container_width=True)
        
        with col2:
            st.markdown("**Accessories:**")
            st.checkbox("👜 Bag", key=f"bag_{day}")
            st.checkbox("👠 Shoes", key=f"shoes_{day}")
            st.checkbox("💍 Jewelry", key=f"jewelry_{day}")
        
        st.markdown("---")

# Special Occasion Types Screen
def occasion_types_screen():
    st.markdown('<div class="page-header"><h2>⭐ Special Occasion</h2><p>What kind of occasion?</p></div>', unsafe_allow_html=True)
    
    if st.button("← Back", key="back_from_occasion_types"):
        go_to_page('occasion_select')
    
    col1, col2 = st.columns(2)
    
    occasions = [
        ("🍷 Dinner Date", "Romantic evening out"),
        ("🎉 Party / Event", "Celebrations & gatherings"),
        ("🌃 Evening Outing", "Night on the town"),
        ("✨ Other Occasion", "Specify your event")
    ]
    
    for i, (title, desc) in enumerate(occasions):
        with col1 if i % 2 == 0 else col2:
            st.markdown(f"""
            <div class="option-card">
                <div style="text-align: center; padding: 1rem;">
                    <div style="font-size: 3rem; margin-bottom: 0.5rem;">{title.split()[0]}</div>
                    <div class="option-title">{' '.join(title.split()[1:])}</div>
                    <div class="option-desc">{desc}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"Select {title}", key=f"occasion_{i}", use_container_width=True):
                go_to_page('special_occasion_planner', title)

# Special Occasion Planner Screen
def special_occasion_planner_screen():
    occasion = st.session_state.occasion_type
    st.markdown(f'<div class="page-header"><h2>{occasion}</h2><p>{datetime.now().strftime("%A, %b %d")}</p></div>', unsafe_allow_html=True)
    
    if st.button("← Back", key="back_from_special"):
        go_to_page('occasion_types')
    
    # Outfit Upload Section
    st.markdown("""
    <div class="section-container">
        <div class="section-title">📸 Your Outfit</div>
    </div>
    """, unsafe_allow_html=True)
    
    outfit_file = st.file_uploader("Upload your outfit photo", type=['jpg', 'jpeg', 'png'], key="special_outfit")
    if outfit_file:
        st.image(outfit_file, caption="Your Outfit", use_container_width=True)
    
    selfie_file = st.file_uploader("Upload your photo (optional)", type=['jpg', 'jpeg', 'png'], key="selfie")
    if selfie_file:
        st.image(selfie_file, caption="Looking Fabulous!", use_container_width=True)
    
    # Accessories Section
    st.markdown("""
    <div class="section-container">
        <div class="section-title">⭐ Accessories</div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.checkbox("👜 Handbag", key="handbag")
    with col2:
        st.checkbox("👠 Heels", key="heels")
    with col3:
        st.checkbox("💍 Jewelry", key="jewelry")
    with col4:
        st.checkbox("💄 Makeup", key="makeup")
    
    # Notes Section
    st.markdown("""
    <div class="section-container">
        <div class="section-title">📝 Notes & Styling Tips</div>
    </div>
    """, unsafe_allow_html=True)
    
    notes = st.text_area("Add styling notes, fit adjustments, or weather considerations", height=100)
    
    # Save Button
    if st.button("Save & Set Reminder ✨", key="save_outfit", use_container_width=True):
        st.success("✅ Outfit saved successfully! Reminder set.")

# Custom Occasion Screen
def custom_occasion_screen():
    st.markdown('<div class="page-header"><h2>✨ Custom Occasion</h2><p>Tell us more</p></div>', unsafe_allow_html=True)
    
    if st.button("← Back", key="back_from_custom"):
        go_to_page('occasion_select')
    
    st.markdown("""
    <div class="section-container">
        <div class="section-title">What's the occasion? 🎯</div>
    </div>
    """, unsafe_allow_html=True)
    
    occasion_name = st.text_input("", placeholder="e.g., Sports outing, Brunch with friends...")
    
    st.markdown("""
    <div class="section-container">
        <div class="section-title">When is it? 📅</div>
    </div>
    """, unsafe_allow_html=True)
    
    occasion_date = st.date_input("Select date", min_value=datetime.now())
    
    st.markdown("""
    <div class="section-container">
        <div class="section-title">Suggested Styles</div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.button("👟 Sporty", key="style_sporty", use_container_width=True)
    with col2:
        st.button("👕 Casual", key="style_casual", use_container_width=True)
    with col3:
        st.button("👗 Chic", key="style_chic", use_container_width=True)
    with col4:
        st.button("🎩 Formal", key="style_formal", use_container_width=True)
    
    if st.button("Continue to Outfit Planning 💖", key="continue_custom", use_container_width=True):
        if occasion_name:
            go_to_page('special_occasion_planner', occasion_name)
        else:
            st.warning("Please enter an occasion name")

# Main app routing
def main():
    if st.session_state.page == 'welcome':
        welcome_screen()
    elif st.session_state.page == 'occasion_select':
        occasion_selection_screen()
    elif st.session_state.page == 'weekly_planner':
        weekly_planner_screen()
    elif st.session_state.page == 'occasion_types':
        occasion_types_screen()
    elif st.session_state.page == 'special_occasion_planner':
        special_occasion_planner_screen()
    elif st.session_state.page == 'custom_occasion':
        custom_occasion_screen()

if __name__ == "__main__":
    main()