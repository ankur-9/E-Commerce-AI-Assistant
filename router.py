import logging
logging.getLogger("LiteLLM").setLevel(logging.ERROR)
from semantic_router import Route
from semantic_router.encoders import HuggingFaceEncoder
from semantic_router.routers import SemanticRouter


encoder = HuggingFaceEncoder(model_name="sentence-transformers/all-MiniLM-L6-v2")

faq = Route(
    name="faq",
    utterances=[
        "What is the return policy of the products?",
        "Do I get discount with the HDFC credit card?",
        "How can I track my order?",
        "What payment methods are accepted?",
        "How long does it take to process a refund?",
        "What happens if I receive a damaged or defective item?",
        "Can I return a defective product?",
        "What is your policy on damaged goods?",
        "How do I raise a complaint about a faulty product?",
        "What is the exchange policy?",
        "How do I cancel my order?",
        "Is cash on delivery available?",
        "How do I contact customer support?",
        "When will my order be delivered?",
        "Can I change my delivery address?",

    ],
score_threshold=0.35
)

sql = Route(
    name="sql",
    utterances=[
        "I want to buy nike shoes that have 50% discount",
        "Are there any shoes under 3000?",
        "Do you have formal shoes in size 9?",
        "Are there any Puma shoes on sale?",
        "What is the price of Puma running shoes",
        "I want to buy PS5 games under 4000",
        "Are there any PS5 games on sale?",
        "What is the price of PS5 dualsense controller?"
    ],
)

router = SemanticRouter(encoder=encoder, routes=[faq,sql], auto_sync="local")
# rl.set_threshold(0.3)

if __name__ == "__main__":
    faq_result = router("What's your policy on defective products?")
    sql_result = router("PS5 games in price range 3000 to 5000")

    print(f"FAQ Route -> {faq_result.name} (Score: {faq_result.similarity_score})")
    print(f"SQL Route -> {sql_result.name} (Score: {sql_result.similarity_score})")