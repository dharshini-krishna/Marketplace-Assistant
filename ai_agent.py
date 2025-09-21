import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Load environment variables
load_dotenv()

class ArtisanAIAgent:
    def __init__(self):
        # Ensure the API key is set as an environment variable
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY environment variable not set. Please check your .env file or environment variables.")
        
        self.llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7, google_api_key=api_key)

    def generate_listing(self, product_name, description, material, location):
        """Generate an optimized product listing using AI"""
        prompt_template = PromptTemplate(
            input_variables=["product_name", "description", "material", "location"],
            template=(
                "You are an expert copywriter for artisan products with deep knowledge of marketplace optimization. "
                "Create an attractive, SEO-friendly, and emotionally compelling product listing for the following item:\n\n"
                "Product Name: {product_name}\n"
                "Description: {description}\n"
                "Material: {material}\n"
                "Location: {location}\n\n"
                "Your listing should include:\n"
                "1. A catchy, SEO-optimized title\n"
                "2. An engaging product description (200-300 words) that highlights:\n"
                "   - Unique craftsmanship and artisan story\n"
                "   - Quality of materials and sustainability\n"
                "   - Emotional appeal and use cases\n"
                "   - Care instructions or special features\n"
                "3. A compelling call-to-action\n\n"
                "Write in a warm, authentic tone that connects with buyers who value handmade, unique items."
            )
        )
        chain = LLMChain(llm=self.llm, prompt=prompt_template)
        return chain.run(product_name=product_name, description=description, material=material, location=location)

    def suggest_pricing(self, product_name, description, material, location):
        """Suggest intelligent pricing based on multiple factors"""
        prompt_template = PromptTemplate(
            input_variables=["product_name", "description", "material", "location"],
            template=(
                "As a marketplace pricing expert specializing in artisan products, analyze the following item "
                "and provide a comprehensive pricing recommendation:\n\n"
                "Product Name: {product_name}\n"
                "Description: {description}\n"
                "Material: {material}\n"
                "Location: {location}\n\n"
                "Consider these factors in your analysis:\n"
                "- Material costs and quality\n"
                "- Time and skill required for craftsmanship\n"
                "- Market demand for similar items\n"
                "- Uniqueness and artistic value\n"
                "- Target customer segment\n"
                "- Geographic market considerations\n\n"
                "Provide:\n"
                "1. A specific price range (e.g., $45-65)\n"
                "2. A recommended optimal price point\n"
                "3. Brief justification for the pricing\n"
                "4. Tips for pricing strategy (premium vs. competitive positioning)"
            )
        )
        chain = LLMChain(llm=self.llm, prompt=prompt_template)
        return chain.run(product_name=product_name, description=description, material=material, location=location)

    def recommend_keywords(self, product_name, description, material):
        """Generate SEO keywords and hashtags for marketing"""
        prompt_template = PromptTemplate(
            input_variables=["product_name", "description", "material"],
            template=(
                "As an SEO and digital marketing expert for artisan marketplaces, generate comprehensive "
                "keyword recommendations for the following product:\n\n"
                "Product Name: {product_name}\n"
                "Description: {description}\n"
                "Material: {material}\n\n"
                "Generate:\n"
                "1. 10-12 primary SEO keywords (2-4 words each) for search optimization\n"
                "2. 8-10 social media hashtags for Instagram/Facebook\n"
                "3. 5-6 long-tail keywords for niche targeting\n"
                "4. 3-4 trending/seasonal keywords if applicable\n\n"
                "Focus on terms that buyers actually search for, including:\n"
                "- Product category terms\n"
                "- Material and technique terms\n"
                "- Style and aesthetic terms\n"
                "- Gift and occasion terms\n"
                "- Handmade/artisan terms\n\n"
                "Format as organized lists with clear categories."
            )
        )
        chain = LLMChain(llm=self.llm, prompt=prompt_template)
        return chain.run(product_name=product_name, description=description, material=material)

    def generate_buyer_message(self, product_name, buyer_preference):
        """Generate personalized messages for buyer inquiries"""
        prompt_template = PromptTemplate(
            input_variables=["product_name", "buyer_preference"],
            template=(
                "You are a skilled artisan responding to a potential buyer inquiry. Write a warm, "
                "professional, and personalized message that builds trust and encourages purchase.\n\n"
                "Product: {product_name}\n"
                "Buyer's Message/Preference: {buyer_preference}\n\n"
                "Your response should:\n"
                "1. Address their specific questions or concerns\n"
                "2. Share relevant details about your craftsmanship process\n"
                "3. Highlight what makes this piece special\n"
                "4. Build personal connection and trust\n"
                "5. Include a gentle call-to-action\n"
                "6. Offer additional assistance\n\n"
                "Keep the tone authentic, knowledgeable, and enthusiastic about your craft. "
                "Make the buyer feel valued and excited about the purchase."
            )
        )
        chain = LLMChain(llm=self.llm, prompt=prompt_template)
        return chain.run(product_name=product_name, buyer_preference=buyer_preference)

    def recommend_products_for_buyer(self, buyer_interest):
        """Recommend products based on buyer preferences"""
        prompt_template = PromptTemplate(
            input_variables=["buyer_interest"],
            template=(
                "As an AI marketplace curator specializing in artisan products, provide personalized "
                "product recommendations for a buyer with the following interests:\n\n"
                "Buyer Interests: {buyer_interest}\n\n"
                "Recommend 4-5 specific types of artisan products that would appeal to this buyer. "
                "For each recommendation, provide:\n"
                "1. Product type/category\n"
                "2. Why it matches their interests\n"
                "3. Key features they'd appreciate\n"
                "4. Approximate price range\n"
                "5. Where they might use/display it\n\n"
                "Focus on unique, handcrafted items that align with their stated preferences. "
                "Consider complementary items that work well together. "
                "Make recommendations feel personal and thoughtful."
            )
        )
        chain = LLMChain(llm=self.llm, prompt=prompt_template)
        return chain.run(buyer_interest=buyer_interest)

    def analyze_market_trends(self, product_category):
        """Analyze market trends for a product category (bonus feature)"""
        prompt_template = PromptTemplate(
            input_variables=["product_category"],
            template=(
                "As a market research analyst for artisan products, provide insights on current "
                "trends and opportunities for the following category:\n\n"
                "Product Category: {product_category}\n\n"
                "Analyze:\n"
                "1. Current market demand and trends\n"
                "2. Popular styles and materials\n"
                "3. Price point opportunities\n"
                "4. Seasonal considerations\n"
                "5. Target customer demographics\n"
                "6. Marketing channel recommendations\n\n"
                "Provide actionable insights for artisans in this category."
            )
        )
        chain = LLMChain(llm=self.llm, prompt=prompt_template)
        return chain.run(product_category=product_category)
