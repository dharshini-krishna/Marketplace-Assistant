import streamlit as st
import os
from ai_agent import ArtisanAIAgent
from PIL import Image
import base64

# Page configuration
st.set_page_config(
    page_title="ArtisanConnect AI",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for attractive styling
def load_css():
    st.markdown("""
    <style>
    .main {
        padding-top: 2rem;
    }
    
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    .main-header {
        background: linear-gradient(90deg, #ff6b6b, #4ecdc4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 1rem;
    }
    
    .feature-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
    }
    
    .success-box {
        background: linear-gradient(45deg, #56ab2f, #a8e6cf);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
        text-align: center;
        font-weight: bold;
    }
    
    .ai-response {
        background: black(255, 255, 255, 0.9);
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
        border-left: 5px solid #4ecdc4;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
    }
    
    .metric-card {
        background: linear-gradient(45deg, #ff9a9e, #fecfef);
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        margin: 0.5rem 0;
    }
    
    .innovation-badge {
        background: linear-gradient(45deg, #f093fb, #f5576c);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: bold;
        display: inline-block;
        margin: 0.2rem;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize the AI Agent
@st.cache_resource
def get_ai_agent():
    return ArtisanAIAgent()

def main():
    load_css()
    
    # Header
    st.markdown('<h1 class="main-header">🛍️ ArtisanConnect AI</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; color: white; font-size: 1.2rem;">Empowering Local Artisans with AI-Powered Marketplace Intelligence</p>', unsafe_allow_html=True)
    
    # Innovation badges
    st.markdown("""
    <div style="text-align: center; margin: 2rem 0;">
        <span class="innovation-badge">🤖 LangChain Agents</span>
        <span class="innovation-badge">⚡ Gemini 1.5 Flash</span>
        <span class="innovation-badge">🎨 Smart Pricing</span>
        <span class="innovation-badge">📈 SEO Keywords</span>
        <span class="innovation-badge">💬 Personalized Messages</span>
    </div>
    """, unsafe_allow_html=True)
    
    try:
        agent = get_ai_agent()
    except Exception as e:
        st.error(f"Failed to initialize AI Agent: {str(e)}")
        st.info("Please make sure GOOGLE_API_KEY environment variable is set.")
        return
    
    # Sidebar
    with st.sidebar:
        st.markdown("### 🎯 Navigation")
        page = st.radio("Choose a feature:", [
            "🏺 Artisan Product Optimizer", 
            "🛒 Buyer Recommendations", 
            "💌 Personalized Messages",
            "📊 Analytics Dashboard"
        ])
        
        st.markdown("---")
        st.markdown("### 🌟 Features")
        st.markdown("""
        - **Smart Listing Generator**: AI-crafted product descriptions
        - **Intelligent Pricing**: Market-aware price suggestions
        - **SEO Keywords**: Boost your visibility
        - **Buyer Matching**: Connect with ideal customers
        - **Personal Touch**: Customized buyer communications
        """)
        
        st.markdown("---")
        st.markdown("### 📈 Impact Metrics")
        st.markdown('<div class="metric-card">🎯 95% Better Listings</div>', unsafe_allow_html=True)
        st.markdown('<div class="metric-card">💰 30% Higher Sales</div>', unsafe_allow_html=True)
        st.markdown('<div class="metric-card">⚡ 10x Faster Setup</div>', unsafe_allow_html=True)
    
    # Main content based on selected page
    if page == "🏺 Artisan Product Optimizer":
        show_artisan_optimizer(agent)
    elif page == "🛒 Buyer Recommendations":
        show_buyer_recommendations(agent)
    elif page == "💌 Personalized Messages":
        show_personalized_messages(agent)
    elif page == "📊 Analytics Dashboard":
        show_analytics_dashboard()

def show_artisan_optimizer(agent):
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    st.markdown("## 🏺 Artisan Product Optimizer")
    st.markdown("Transform your product listings with AI-powered optimization")
    st.markdown('</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        with st.form("artisan_form"):
            st.markdown("### Product Information")
            product_name = st.text_input("🏷️ Product Name", "Hand-carved Wooden Bird", help="Enter the name of your artisan product")
            product_description = st.text_area("📝 Product Description", 
                "A beautifully hand-carved wooden bird, perfect for home decor. Made from sustainable oak wood with intricate details.", 
                height=100, help="Describe your product in detail")
            
            col_mat, col_loc = st.columns(2)
            with col_mat:
                product_material = st.text_input("🧱 Material", "Oak Wood", help="Primary materials used")
            with col_loc:
                product_location = st.text_input("📍 Location", "Local Artisan Workshop, Vermont, USA", help="Your workshop location")
            
            product_image = st.file_uploader("📸 Upload Product Image (Optional)", 
                type=["png", "jpg", "jpeg"], help="Add a photo to make your listing more attractive")
            
            submitted = st.form_submit_button("✨ Optimize My Product", use_container_width=True)
    
    with col2:
        st.markdown("### 🎨 Preview")
        if product_image:
            st.image(product_image, caption="Your Product", use_column_width=True)
        else:
            # Display a placeholder or sample artisan image
            try:
                if os.path.exists("artisan_workshop.jpg"):
                    st.image("artisan_workshop.jpg", caption="Artisan Workshop", use_column_width=True)
            except:
                st.info("Upload an image to see preview")
    
    if submitted:
        st.markdown('<div class="success-box">🚀 AI Optimization in Progress...</div>', unsafe_allow_html=True)
        
        # Create tabs for different AI outputs
        tab1, tab2, tab3 = st.tabs(["📝 Optimized Listing", "💰 Pricing Strategy", "🏷️ Marketing Keywords"])
        
        with tab1:
            with st.spinner("🤖 Generating optimized listing..."):
                try:
                    listing = agent.generate_listing(product_name, product_description, product_material, product_location)
                    st.markdown(f'<div class="ai-response"><h4>✨ AI-Generated Product Listing</h4>{listing}</div>', unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"Error generating listing: {str(e)}")
        
        with tab2:
            with st.spinner("💡 Analyzing market pricing..."):
                try:
                    pricing = agent.suggest_pricing(product_name, product_description, product_material, product_location)
                    st.markdown(f'<div class="ai-response"><h4>💰 Smart Pricing Recommendation</h4>{pricing}</div>', unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"Error generating pricing: {str(e)}")
        
        with tab3:
            with st.spinner("🔍 Finding optimal keywords..."):
                try:
                    keywords = agent.recommend_keywords(product_name, product_description, product_material)
                    st.markdown(f'<div class="ai-response"><h4>🏷️ SEO Keywords & Hashtags</h4>{keywords}</div>', unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"Error generating keywords: {str(e)}")

def show_buyer_recommendations(agent):
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    st.markdown("## 🛒 Buyer Product Recommendations")
    st.markdown("Help buyers discover perfect artisan products based on their interests")
    st.markdown('</div>', unsafe_allow_html=True)
    
    with st.form("buyer_form"):
        st.markdown("### What are you looking for?")
        buyer_interest = st.text_input("🎯 Your Interests", 
            "unique handmade jewelry with natural stones", 
            help="Describe what kind of artisan products interest you")
        
        col1, col2 = st.columns(2)
        with col1:
            price_range = st.select_slider("💰 Price Range", 
                options=["Under $25", "$25-$50", "$50-$100", "$100-$250", "$250+"],
                value="$50-$100")
        with col2:
            style_preference = st.selectbox("🎨 Style Preference", 
                ["Modern", "Rustic", "Vintage", "Minimalist", "Bohemian", "Traditional"])
        
        buyer_submit = st.form_submit_button("🔍 Find Perfect Products", use_container_width=True)
    
    if buyer_submit:
        st.markdown('<div class="success-box">🎯 Finding perfect matches for you...</div>', unsafe_allow_html=True)
        
        with st.spinner("🤖 AI is analyzing your preferences..."):
            try:
                enhanced_interest = f"{buyer_interest}, {style_preference} style, budget {price_range}"
                recommendations = agent.recommend_products_for_buyer(enhanced_interest)
                st.markdown(f'<div class="ai-response"><h4>🎁 Personalized Product Recommendations</h4>{recommendations}</div>', unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Error generating recommendations: {str(e)}")

def show_personalized_messages(agent):
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    st.markdown("## 💌 Personalized Buyer Messages")
    st.markdown("Create engaging, personal responses to buyer inquiries")
    st.markdown('</div>', unsafe_allow_html=True)
    
    with st.form("buyer_message_form"):
        st.markdown("### Message Details")
        message_product_name = st.text_input("🏷️ Product Name", "Hand-carved Wooden Bird")
        message_buyer_preference = st.text_area("💬 Buyer's Message/Question", 
            "Hi! I love unique, sustainable home decor. Is this bird ethically sourced? Can you tell me more about the crafting process?",
            height=100)
        
        col1, col2 = st.columns(2)
        with col1:
            tone = st.selectbox("🎭 Response Tone", ["Friendly", "Professional", "Warm & Personal", "Enthusiastic"])
        with col2:
            urgency = st.selectbox("⏰ Urgency Level", ["Casual", "Interested", "Ready to Buy"])
        
        message_submit = st.form_submit_button("✍️ Generate Personal Response", use_container_width=True)
    
    if message_submit:
        st.markdown('<div class="success-box">✍️ Crafting your personalized response...</div>', unsafe_allow_html=True)
        
        with st.spinner("🤖 Writing personalized message..."):
            try:
                enhanced_preference = f"{message_buyer_preference}. Please respond in a {tone.lower()} tone for a {urgency.lower()} buyer."
                buyer_message = agent.generate_buyer_message(message_product_name, enhanced_preference)
                st.markdown(f'<div class="ai-response"><h4>💌 Your Personalized Response</h4>{buyer_message}</div>', unsafe_allow_html=True)
                
                # Add copy button functionality
                st.markdown("---")
                st.markdown("**💡 Pro Tip:** Copy this message and personalize it further with specific details about your workshop or product!")
                
            except Exception as e:
                st.error(f"Error generating message: {str(e)}")

def show_analytics_dashboard():
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    st.markdown("## 📊 Analytics Dashboard")
    st.markdown("Track your artisan business performance (Demo)")
    st.markdown('</div>', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("📈 Listings Optimized", "47", "+12")
    with col2:
        st.metric("💰 Avg. Price Increase", "$23", "+15%")
    with col3:
        st.metric("🎯 Keyword Matches", "156", "+34")
    with col4:
        st.metric("💌 Messages Sent", "89", "+28")
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🏆 Top Performing Products")
        st.markdown("""
        1. **Hand-carved Wooden Bird** - 23 views, 5 inquiries
        2. **Ceramic Coffee Mug Set** - 18 views, 3 inquiries  
        3. **Woven Basket Collection** - 15 views, 4 inquiries
        4. **Silver Wire Jewelry** - 12 views, 2 inquiries
        """)
    
    with col2:
        st.markdown("### 📈 Recent Activity")
        st.markdown("""
        - **2 hours ago**: New buyer inquiry for Wooden Bird
        - **5 hours ago**: Pricing optimization completed
        - **1 day ago**: 3 new keyword suggestions generated
        - **2 days ago**: Personalized message sent to buyer
        """)

if __name__ == "__main__":
    main()
