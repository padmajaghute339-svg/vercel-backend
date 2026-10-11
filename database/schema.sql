-- ========================================================
-- HALDIRAM CINEMATIC EXPERIENCE — SUPABASE / POSTGRESQL SCHEMA
-- ========================================================

-- 1. Enable UUID Extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- 2. Categories
CREATE TABLE IF NOT EXISTS categories (
    id VARCHAR(50) PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    description TEXT
);

-- 3. Products
CREATE TABLE IF NOT EXISTS products (
    id VARCHAR(100) PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    hindi_name VARCHAR(200),
    tagline VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    long_description TEXT,
    category_id VARCHAR(50) REFERENCES categories(id) ON DELETE SET NULL,
    flavor_profile VARCHAR(50) DEFAULT 'crunchy',
    spice_level INT DEFAULT 1,
    crunch_index INT DEFAULT 90,
    is_bestseller BOOLEAN DEFAULT FALSE,
    image_key VARCHAR(100) NOT NULL,
    bg_theme VARCHAR(50) DEFAULT '#8B0000',
    accent_color VARCHAR(50) DEFAULT '#FFB703',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- 4. Product Variants
CREATE TABLE IF NOT EXISTS product_variants (
    id VARCHAR(100) PRIMARY KEY,
    product_id VARCHAR(100) REFERENCES products(id) ON DELETE CASCADE,
    weight VARCHAR(50) NOT NULL,
    price NUMERIC(10, 2) NOT NULL,
    original_price NUMERIC(10, 2),
    sku VARCHAR(100) UNIQUE NOT NULL,
    in_stock BOOLEAN DEFAULT TRUE,
    stock_quantity INT DEFAULT 100
);

-- 5. Users & Profiles
CREATE TABLE IF NOT EXISTS users (
    id VARCHAR(100) PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    email VARCHAR(200) UNIQUE NOT NULL,
    phone VARCHAR(50),
    role VARCHAR(50) DEFAULT 'customer',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- 6. Addresses
CREATE TABLE IF NOT EXISTS addresses (
    id VARCHAR(100) PRIMARY KEY,
    user_id VARCHAR(100) REFERENCES users(id) ON DELETE CASCADE,
    full_name VARCHAR(200) NOT NULL,
    street TEXT NOT NULL,
    city VARCHAR(100) NOT NULL,
    state VARCHAR(100) NOT NULL,
    pincode VARCHAR(20) NOT NULL,
    phone VARCHAR(50) NOT NULL
);

-- 7. Orders
CREATE TABLE IF NOT EXISTS orders (
    id VARCHAR(100) PRIMARY KEY,
    order_number VARCHAR(100) UNIQUE NOT NULL,
    user_id VARCHAR(100) REFERENCES users(id) ON DELETE SET NULL,
    status VARCHAR(50) DEFAULT 'confirmed',
    subtotal NUMERIC(10, 2) NOT NULL,
    discount NUMERIC(10, 2) DEFAULT 0.00,
    shipping NUMERIC(10, 2) DEFAULT 0.00,
    tax NUMERIC(10, 2) DEFAULT 0.00,
    total NUMERIC(10, 2) NOT NULL,
    payment_method VARCHAR(100) NOT NULL,
    tracking_number VARCHAR(100) NOT NULL,
    estimated_delivery VARCHAR(100) NOT NULL,
    shipping_full_name VARCHAR(200) NOT NULL,
    shipping_email VARCHAR(200) NOT NULL,
    shipping_phone VARCHAR(50) NOT NULL,
    shipping_street TEXT NOT NULL,
    shipping_city VARCHAR(100) NOT NULL,
    shipping_state VARCHAR(100) NOT NULL,
    shipping_pincode VARCHAR(20) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- 8. Order Items
CREATE TABLE IF NOT EXISTS order_items (
    id VARCHAR(100) PRIMARY KEY,
    order_id VARCHAR(100) REFERENCES orders(id) ON DELETE CASCADE,
    product_id VARCHAR(100) NOT NULL,
    variant_id VARCHAR(100) NOT NULL,
    product_name VARCHAR(200) NOT NULL,
    variant_weight VARCHAR(50) NOT NULL,
    price NUMERIC(10, 2) NOT NULL,
    quantity INT DEFAULT 1,
    image_key VARCHAR(100) NOT NULL
);

-- 9. Reviews
CREATE TABLE IF NOT EXISTS reviews (
    id VARCHAR(100) PRIMARY KEY,
    product_id VARCHAR(100) REFERENCES products(id) ON DELETE CASCADE,
    author_name VARCHAR(200) NOT NULL,
    rating INT DEFAULT 5,
    comment TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
