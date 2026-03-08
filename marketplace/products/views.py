from django.shortcuts import render, redirect, get_object_or_404
from .models import Product

products = [
    {
        'id': 1,
        'name': 'Ethiopia Yirgacheffe',
        'price': 18.99,
        'stock_count': 35,
        'image': 'https://images.unsplash.com/photo-1447933601403-0c6688de566e?w=600&q=80',
        'origin': 'Ethiopia',
        'roast': 'Light',
        'description': 'Bright and floral with notes of jasmine, bergamot, and lemon. One of the world\'s most celebrated single-origin coffees, grown at high altitude in the Yirgacheffe region.',
    },
    {
        'id': 2,
        'name': 'Colombia Supremo',
        'price': 16.50,
        'stock_count': 58,
        'image': 'https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=600&q=80',
        'origin': 'Colombia',
        'roast': 'Medium',
        'description': 'Smooth and well-balanced with caramel sweetness, mild nuttiness, and a clean finish. Sourced from small family farms in the Huila and Nariño departments.',
    },
    {
        'id': 3,
        'name': 'Kenya AA',
        'price': 21.00,
        'stock_count': 22,
        'image': 'https://images.unsplash.com/photo-1559056199-641a0ac8b55e?w=600&q=80',
        'origin': 'Kenya',
        'roast': 'Medium-Light',
        'description': 'Bold and wine-like with blackcurrant, tomato, and grapefruit notes. Kenya AA is the largest screen-size grade, representing the best beans from the Nyeri highlands.',
    },
    {
        'id': 4,
        'name': 'Sumatra Mandheling',
        'price': 17.25,
        'stock_count': 0,
        'image': 'https://images.unsplash.com/photo-1510591509098-f4fdc6d0ff04?w=600&q=80',
        'origin': 'Indonesia',
        'roast': 'Dark',
        'description': 'Earthy, full-bodied, and complex with notes of dark chocolate, cedar, and herbs. Wet-hulled using the traditional Giling Basah method unique to Sumatra.',
    },
    {
        'id': 5,
        'name': 'Guatemala Antigua',
        'price': 15.75,
        'stock_count': 44,
        'image': 'https://images.unsplash.com/photo-1501339847302-ac426a4a7cbb?w=600&q=80',
        'origin': 'Guatemala',
        'roast': 'Medium',
        'description': 'Rich and velvety with brown sugar, dark chocolate, and a smoky finish. Grown in volcanic soil at 4,500–5,500 feet around the colonial city of Antigua.',
    },
    {
        'id': 6,
        'name': 'Brazil Santos',
        'price': 13.99,
        'stock_count': 80,
        'image': 'https://images.unsplash.com/photo-1544787219-7f47ccb76574?w=600&q=80',
        'origin': 'Brazil',
        'roast': 'Medium-Dark',
        'description': 'Low acidity with sweet nutty and milk chocolate flavors. Brazil Santos is the backbone of most espresso blends, prized for its consistency and perfect crema.',
    },
    {
        'id': 7,
        'name': 'Cold Brew Blend',
        'price': 22.00,
        'stock_count': 18,
        'image': 'https://images.unsplash.com/photo-1461023058943-07fcbe16d735?w=600&q=80',
        'origin': 'Blend',
        'roast': 'Dark',
        'description': 'Specially crafted for cold extraction. A bold blend of Brazilian and Guatemalan beans that delivers a smooth, chocolatey cold brew with zero bitterness.',
    },
    {
        'id': 8,
        'name': 'Pour Over Selection',
        'price': 24.50,
        'stock_count': 12,
        'image': 'https://images.unsplash.com/photo-1509042239860-f550ce710b93?w=600&q=80',
        'origin': 'Ethiopia & Colombia',
        'roast': 'Light',
        'description': 'A curated light roast blend designed for the pour-over method. Expect layered complexity — tropical fruit, honey, and a lingering floral sweetness in every cup.',
    },
]

def index(request):
    products = Product.objects.all()
    return render(request, 'products/index.html', {'products': products})

def show(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'products/show.html', {'product': product})

def delete(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect('products:index')
