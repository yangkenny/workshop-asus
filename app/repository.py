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


def search_and_filter_products(
    query: str | None = None,
    sort_by: str | None = None,
    order: str = "asc",
    page: int = 1,
    page_size: int = 20,
) -> tuple[list[Product], int]:
    """
    Search, filter, sort, and paginate products.

    Returns a tuple of (items, total) where total is the count before pagination.
    """
    products = PRODUCTS.copy()

    # Filter by search query
    if query:
        query_lower = query.lower()
        products = [
            p
            for p in products
            if query_lower in p.name.lower() or query_lower in p.category.lower()
        ]

    # Count total before pagination
    total = len(products)

    # Sort
    if sort_by:
        reverse = order == "desc"
        if sort_by == "name":
            products.sort(key=lambda p: p.name, reverse=reverse)
        elif sort_by == "price":
            products.sort(key=lambda p: p.price, reverse=reverse)

    # Paginate
    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size
    paginated_products = products[start_idx:end_idx]

    return paginated_products, total

