from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template(
        "index.html",
        name="Orbis",
        tagline="Motion That Makes Brands Unforgettable",
        subtitle="Your product's story — told in one powerful minute",
        spots_left="Currently online",
        projects=[
            {
                "title": "Stripe",
                "description": "Product motion concept",
                "youtube_id": "s82W9mpqdN8",
                "category": "Product launch",
                "accent": "#7c3cff",
            },
            {
                "title": "TaskFlow",
                "description": "SaaS workflow animation",
                "youtube_id": "9HjeLE5JYGc",
                "category": "SaaS motion",
                "accent": "#39d98a",
            },
            {
                "title": "Spotify",
                "description": "Brand motion concept",
                "youtube_id": "5kyONWP88yc",
                "category": "Brand concept",
                "accent": "#1ed760",
            },
        ],
        faqs=[
            {
                "question": "What services do you offer?",
                "answer": "High-end motion design for brands that want clarity and impact. I create product launch videos, explainers, demos, short-form reels, VSLs, and keynote visuals—combining clean UI motion with strong storytelling to make ideas impossible to ignore.",
            },
            {
                "question": "How long does a project usually take?",
                "answer": "Most builds take 3–7 days, depending on how much content you provide and any custom sections you want added. I keep the process smooth, fast, and collaborative.",
            },
            {
                "question": "Is there a limit to revisions during the process?",
                "answer": "No compromises. We offer unlimited revisions at every stage—we'll keep refining your video until it's exactly how you want it.",
            },
            {
                "question": "How do payments work?",
                "answer": "To keep things simple, I send a quick invoice to get started. Once that's paid, I begin working right away and keep you updated through the entire process. I accept crypto, PayPal, Stripe invoices, and bank transfer.",
            },
        ],
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)
