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
    order: str = "asc",
) -> list[Product]:
    """Search and sort products.
    
    Args:
        query: Case-insensitive search query for name or category
        sort_by: Field to sort by (e.g., "price")
        order: Sort order ("asc" or "desc")
    
    Returns:
        Filtered and sorted list of products
    """
    results = PRODUCTS.copy()
    
    # Apply search filter
    if query:
        query_lower = query.lower()
        results = [
            p for p in results
            if query_lower in p.name.lower() or query_lower in p.category.lower()
        ]
    
    # Apply sorting
    if sort_by == "price":
        results.sort(key=lambda p: p.price, reverse=(order == "desc"))
    
    return results

