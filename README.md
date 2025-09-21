# 🛍️ ArtisanConnect AI - Marketplace Assistant for Local Artisans

**ArtisanConnect AI** is an innovative marketplace assistant that empowers local artisans with AI-powered tools to optimize their product listings, get intelligent pricing suggestions, generate SEO keywords, and create personalized buyer communications.

## ✨ Features

- **🏺 Smart Product Listing Generator**: AI-crafted, compelling product descriptions
- **💰 Intelligent Pricing Advisor**: Market-aware price recommendations
- **🏷️ SEO Keyword Optimizer**: Boost visibility with targeted keywords
- **🛒 Buyer Recommendation Engine**: Match buyers with perfect products
- **💌 Personalized Message Generator**: Create engaging buyer communications
- **📊 Analytics Dashboard**: Track performance metrics (demo)

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Google API Key for Gemini 1.5 Flash

### Installation

1. **Extract the project files**
   ```bash
   unzip ArtisanConnect_AI.zip
   cd ArtisanConnect_AI
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your Google API Key**
   
   ```
   Or create a `.env` file:
   ```
   GOOGLE_API_KEY=your_api_key_here
   
   ```

6. **Run the application**
   ```bash
   streamlit run app.py
   ```

7. **Open your browser** to `http://localhost:8501`

## 🎯 How to Use

### For Artisans:
1. Navigate to **"🏺 Artisan Product Optimizer"**
2. Fill in your product details
3. Upload a product image (optional)
4. Click **"✨ Optimize My Product"**
5. Get AI-generated listing, pricing, and keywords

### For Buyers:
1. Go to **"🛒 Buyer Recommendations"**
2. Describe your interests and preferences
3. Get personalized product suggestions

### For Customer Service:
1. Use **"💌 Personalized Messages"** 
2. Enter buyer's question/preference
3. Generate warm, engaging responses

## 🏗️ Architecture

- **Frontend**: Streamlit with custom CSS styling
- **AI Engine**: LangChain + Google Gemini 1.5 Flash
- **Core Features**: Specialized AI agents for different tasks
- **Design**: Modern glassmorphism UI with gradient backgrounds

## 🌟 Innovation Highlights

- **Multi-Agent System**: Specialized AI agents for different marketplace tasks
- **Context-Aware Responses**: Personalized based on buyer preferences and product details
- **Visual Appeal**: Modern UI with artisan-themed backgrounds and smooth animations
- **Real-time Processing**: Instant AI-powered optimizations
- **Scalable Architecture**: Easy to extend with additional features

## 📁 Project Structure

```
ArtisanConnect_AI/
├── app.py                 # Main Streamlit application
├── ai_agent.py           # Core AI agent with LangChain
├── requirements.txt      # Python dependencies
├── README.md            # This file
├── artisan_workshop.jpg # Background image
└── pottery_workshop.webp # Additional background image
```

## 🔧 Technical Details

- **LangChain Integration**: Uses LangChain for structured AI interactions
- **Gemini 1.5 Flash**: Google's latest language model for fast, accurate responses
- **Streamlit Framework**: Interactive web interface with custom styling
- **Modular Design**: Separate components for easy maintenance and extension

## 🎨 UI Features

- **Glassmorphism Design**: Modern, translucent interface elements
- **Gradient Backgrounds**: Beautiful color transitions
- **Responsive Layout**: Works on desktop and mobile
- **Interactive Elements**: Smooth animations and hover effects
- **Professional Typography**: Clear, readable fonts with proper hierarchy

## 🚀 Future Enhancements

- **Image Analysis**: AI-powered product image optimization
- **Market Trends**: Real-time market analysis and trends
- **Multi-language Support**: Support for international artisans
- **Integration APIs**: Connect with popular marketplace platforms
- **Advanced Analytics**: Detailed performance tracking and insights

## 📞 Support

For questions or issues, please refer to the code comments or create an issue in the project repository.

---

**Built with ❤️ for local artisans worldwide**
