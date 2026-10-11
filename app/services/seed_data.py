from sqlalchemy.orm import Session
from backend.app.models.models import Category, Product, ProductVariant, User, Address

def seed_database(db: Session):
    # Check if categories already seeded
    if db.query(Category).first():
        return

    # Seed Categories
    categories = [
        Category(id="all", name="All Specialties", description="Complete royal collection"),
        Category(id="namkeen", name="Namkeen & Savories", description="Acoustic Bikaneri crunch savories"),
        Category(id="sweets", name="Traditional Sweets", description="Pure Desi Ghee artisanal mithai"),
        Category(id="chips-savories", name="Chips & Crackers", description="Crisp lentil and potato crackers"),
        Category(id="cookies", name="Bakery & Cookies", description="Heritage tea-time cookies"),
        Category(id="gift-boxes", name="Festive Gift Boxes", description="Celebration royal brass and keepsake hampers"),
    ]
    db.add_all(categories)
    db.commit()

    # Seed Products and Variants
    products_data = [
        {
            "id": "aloo-bhujia-royal",
            "name": "Royal Aloo Bhujia",
            "hindi_name": "शाही आलू भुजिया",
            "tagline": "Mint-infused potato & moth bean sev with signature spices",
            "category_id": "namkeen",
            "flavor_profile": "crunchy",
            "description": "Crisp strings made from fresh mountain potatoes, stone-ground moth flour, and royal mint.",
            "long_description": "Crafted following the sacred 1937 Bikaner recipe, our Royal Aloo Bhujia balances potato softness with explosive crunch.",
            "spice_level": 3,
            "crunch_index": 98,
            "is_bestseller": True,
            "image_key": "aloo-bhujia",
            "bg_theme": "#8B0000",
            "accent_color": "#FFB703",
            "variants": [
                {"id": "ab-200", "weight": "200g Pouch", "price": 110.0, "original_price": 130.0, "sku": "CC-AB-200"},
                {"id": "ab-400", "weight": "400g Family Pack", "price": 210.0, "original_price": 250.0, "sku": "CC-AB-400"},
                {"id": "ab-1000", "weight": "1kg Mega Feast", "price": 490.0, "original_price": 580.0, "sku": "CC-AB-1000"},
            ]
        },
        {
            "id": "bikaneri-bhujia-classic",
            "name": "Heritage Bikaneri Bhujia",
            "hindi_name": "बीकानेरी भुजिया",
            "tagline": "The timeless GI-tagged classic with sharp black pepper bite",
            "category_id": "namkeen",
            "flavor_profile": "spicy",
            "description": "Sun-baked desert moth dal flour extruded into fine golden threads with black pepper.",
            "long_description": "Bikaner's desert winds and arid climate are woven into every strand of this authentic recipe.",
            "spice_level": 4,
            "crunch_index": 99,
            "is_bestseller": True,
            "image_key": "bikaneri-bhujia",
            "bg_theme": "#7A0000",
            "accent_color": "#FF6B00",
            "variants": [
                {"id": "bb-200", "weight": "200g Pouch", "price": 125.0, "original_price": 145.0, "sku": "CC-BB-200"},
                {"id": "bb-400", "weight": "400g Classic Box", "price": 240.0, "original_price": 280.0, "sku": "CC-BB-400"},
                {"id": "bb-1000", "weight": "1kg Tin Canister", "price": 560.0, "original_price": 650.0, "sku": "CC-BB-1000"},
            ]
        },
        {
            "id": "royal-kaju-katli",
            "name": "Royal Shahi Kaju Katli",
            "hindi_name": "शाही काजू कतली",
            "tagline": "Fine Goan cashews delicately sheeted with pure silver vark",
            "category_id": "sweets",
            "flavor_profile": "sweet",
            "description": "Silky diamond prisms of pure Goan cashews and organic cane syrup.",
            "long_description": "We select only grade W180 king cashews, slowly cooked in copper cauldrons with pure silver leaf.",
            "spice_level": 1,
            "crunch_index": 15,
            "is_bestseller": True,
            "image_key": "kaju-katli",
            "bg_theme": "#1B3B2B",
            "accent_color": "#FFD700",
            "variants": [
                {"id": "kk-250", "weight": "250g Gift Tray", "price": 360.0, "original_price": 420.0, "sku": "CC-KK-250"},
                {"id": "kk-500", "weight": "500g Regal Box", "price": 690.0, "original_price": 800.0, "sku": "CC-KK-500"},
                {"id": "kk-1000", "weight": "1kg Festive Hamper", "price": 1350.0, "original_price": 1550.0, "sku": "CC-KK-1000"},
            ]
        },
        {
            "id": "gulab-jamun-desighee",
            "name": "Desi Ghee Gulab Jamun",
            "hindi_name": "देसी घी गुलाब जामुन",
            "tagline": "Soft khoya pearls infused with saffron and green cardamom nectar",
            "category_id": "sweets",
            "flavor_profile": "sweet",
            "description": "Golden-fried khoya dumplings bathed in fragrant damask rose and Kashmiri saffron syrup.",
            "long_description": "Simmered gently in 100% pure Danedar Desi Ghee at low heat until amber skin forms around pillowy core.",
            "spice_level": 1,
            "crunch_index": 5,
            "is_bestseller": False,
            "image_key": "gulab-jamun",
            "bg_theme": "#5C1D1D",
            "accent_color": "#FFB703",
            "variants": [
                {"id": "gj-500", "weight": "500g Sealed Tin", "price": 240.0, "original_price": 280.0, "sku": "CC-GJ-500"},
                {"id": "gj-1000", "weight": "1kg Feast Canister", "price": 440.0, "original_price": 520.0, "sku": "CC-GJ-1000"},
            ]
        },
        {
            "id": "moong-dal-crispy",
            "name": "Golden Fried Moong Dal",
            "hindi_name": "मूंग दाल नमकीन",
            "tagline": "Sun-soaked yellow lentils fried to a golden airy crunch",
            "category_id": "namkeen",
            "flavor_profile": "crunchy",
            "description": "Split yellow mung lentils flash-fried with pink rock salt to light perfection.",
            "long_description": "High in plant protein and undeniably addictive without greasy residue.",
            "spice_level": 1,
            "crunch_index": 94,
            "is_bestseller": False,
            "image_key": "moong-dal",
            "bg_theme": "#C88A00",
            "accent_color": "#FFFDF7",
            "variants": [
                {"id": "md-200", "weight": "200g Pouch", "price": 95.0, "original_price": 110.0, "sku": "CC-MD-200"},
                {"id": "md-400", "weight": "400g Duo Pack", "price": 180.0, "original_price": 210.0, "sku": "CC-MD-400"},
            ]
        }
    ]

    for p in products_data:
        variants = p.pop("variants")
        prod = Product(**p)
        db.add(prod)
        db.flush()
        for v in variants:
            var = ProductVariant(product_id=prod.id, **v)
            db.add(var)

    # Seed Admin User
    admin = User(
        id="usr_admin",
        name="Chief Confectioner (Admin)",
        email="admin@crunchycraft.com",
        phone="+91 98290 12345",
        role="admin"
    )
    db.add(admin)

    db.commit()
