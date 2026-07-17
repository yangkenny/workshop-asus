from app.models import Product

PRODUCTS = [
    Product(id=1, name="Zenbook 14 OLED", category="Laptop", price=42900),
    Product(id=2, name="ROG Zephyrus G14", category="Gaming Laptop", price=62900),
    Product(id=3, name="ProArt P16", category="Creator Laptop", price=79900),
    Product(id=4, name="TUF Gaming A15", category="Gaming Laptop", price=38900),
    Product(id=5, name="ROG Ally X", category="Handheld", price=26900),
    Product(id=6, name="ProArt Display PA279CRV", category="Monitor", price=15900),
]


def list_products() -> list[Product]:
    return PRODUCTS.copy()


def get_product(product_id: int) -> Product | None:
    return next((product for product in PRODUCTS if product.id == product_id), None)


def search_products(
    query: str | None = None,
    sort_by: str | None = None,
    sort_order: str = "asc",
    page: int = 1,
    page_size: int = 20,
) -> tuple[list[Product], int]:
    """Search and sort products with pagination.
    
    Returns:
        Tuple of (paginated_products, total_count_before_pagination)
    """
    # Start with all products
    results = PRODUCTS.copy()
    
    # Apply search filter
    if query:
        query_lower = query.lower()
        results = [
            p for p in results
            if query_lower in p.name.lower() or query_lower in p.category.lower()
        ]
    
    # Calculate total before pagination
    total = len(results)
    
    # Apply sorting
    if sort_by == "name":
        results.sort(key=lambda p: p.name, reverse=(sort_order == "desc"))
    elif sort_by == "price":
        results.sort(key=lambda p: p.price, reverse=(sort_order == "desc"))
    
    # Apply pagination
    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size
    paginated = results[start_idx:end_idx]
    
    return paginated, total

