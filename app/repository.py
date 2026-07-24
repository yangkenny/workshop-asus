from app.models import Product

PRODUCTS = [
    Product(id=1, name="Zenbook 14 OLED", category="Laptop", price=42900),
    Product(id=2, name="ROG Zephyrus G14", category="Gaming Laptop", price=62900),
    Product(id=3, name="ProArt P16", category="Creator Laptop", price=79900),
    Product(id=4, name="TUF Gaming A15", category="Gaming Laptop", price=38900),
    Product(id=5, name="ROG Ally X", category="Handheld", price=26900),
    Product(id=6, name="ProArt Display PA279CRV", category="Monitor", price=15900),
]


def list_products(
    q: str | None = None,
    sort_by: str | None = None,
    order: str = "asc",
    page: int = 1,
    page_size: int = 20,
) -> tuple[list[Product], int]:
    """List products with optional filtering, sorting, and pagination.
    
    Returns:
        Tuple of (paginated products, total count before pagination)
    """
    products = PRODUCTS.copy()
    
    # Filter by search query (case-insensitive partial match on name or category)
    if q:
        q_lower = q.lower()
        products = [
            p for p in products
            if q_lower in p.name.lower() or q_lower in p.category.lower()
        ]
    
    # Sort by specified field
    if sort_by:
        reverse = order == "desc"
        if sort_by == "name":
            products = sorted(products, key=lambda p: p.name, reverse=reverse)
        elif sort_by == "price":
            products = sorted(products, key=lambda p: p.price, reverse=reverse)
    
    # Calculate total before pagination
    total = len(products)
    
    # Apply pagination
    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size
    paginated_products = products[start_idx:end_idx]
    
    return paginated_products, total


def get_product(product_id: int) -> Product | None:
    return next((product for product in PRODUCTS if product.id == product_id), None)

