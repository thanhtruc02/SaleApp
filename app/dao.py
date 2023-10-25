def load_categories():
    return[{
        'id' : '1',
        'name' : 'Mobile'
    }, {
        'id' : '2',
        'name' : 'Tablet'
    }]

def load_products(kw=None):
    products = [{
        'id' : 1,
        'name' : 'iPhone 12',
        'price' : 20000000,
        'image': 'https://vtv1.mediacdn.vn/2019/10/10/photo-1-15706463929181755249740.jpg'
    }, {
        'id' : 2,
        'name' : 'iPhone 12',
        'price' : 20000000,
        'image': 'https://vtv1.mediacdn.vn/2019/10/10/photo-1-15706463929181755249740.jpg'
    }, {
        'id' : 3,
        'name' : 'iPhone 12',
        'price' : 20000000,
        'image': 'https://vtv1.mediacdn.vn/2019/10/10/photo-1-15706463929181755249740.jpg'
    }, {
        'id' : 1,
        'name' : 'iPhone 12',
        'price' : 20000000,
        'image': 'https://vtv1.mediacdn.vn/2019/10/10/photo-1-15706463929181755249740.jpg'
    }, {
        'id' : 4,
        'name' : 'Samsung',
        'price' : 15000000,
        'image': 'https://vtv1.mediacdn.vn/2019/10/10/photo-1-15706463929181755249740.jpg'
    }, {
        'id' : 1,
        'name' : 'iPhone 12',
        'price' : 20000000,
        'image': 'https://vtv1.mediacdn.vn/2019/10/10/photo-1-15706463929181755249740.jpg'
    }, {
        'id' : 1,
        'name' : 'iPhone 12',
        'price' : 20000000,
        'image': 'https://vtv1.mediacdn.vn/2019/10/10/photo-1-15706463929181755249740.jpg'
    }, {
        'id' : 1,
        'name' : 'iPhone 12',
        'price' : 20000000,
        'image': 'https://vtv1.mediacdn.vn/2019/10/10/photo-1-15706463929181755249740.jpg'
    },  {
        'id' : 1,
        'name' : 'iPhone 12',
        'price' : 20000000,
        'image': 'https://vtv1.mediacdn.vn/2019/10/10/photo-1-15706463929181755249740.jpg'
    }, {
        'id' : 1,
        'name' : 'iPhone 12',
        'price' : 20000000,
        'image': 'https://vtv1.mediacdn.vn/2019/10/10/photo-1-15706463929181755249740.jpg'
    }, {
        'id' : 1,
        'name' : 'iPhone 12',
        'price' : 20000000,
        'image': 'https://vtv1.mediacdn.vn/2019/10/10/photo-1-15706463929181755249740.jpg'
    }, {
        'id' : 1,
        'name' : 'iPhone 12',
        'price' : 20000000,
        'image': 'https://vtv1.mediacdn.vn/2019/10/10/photo-1-15706463929181755249740.jpg'
    }, {
        'id' : 1,
        'name' : 'iPhone 12',
        'price' : 20000000,
        'image': 'https://vtv1.mediacdn.vn/2019/10/10/photo-1-15706463929181755249740.jpg'
    }, {
        'id' : 1,
        'name' : 'iPhone 12',
        'price' : 20000000,
        'image': 'https://vtv1.mediacdn.vn/2019/10/10/photo-1-15706463929181755249740.jpg'
    },{
        'id' : 1,
        'name' : 'iPhone 12',
        'price' : 20000000,
        'image': 'https://vtv1.mediacdn.vn/2019/10/10/photo-1-15706463929181755249740.jpg'
    }, {
        'id' : 1,
        'name' : 'Samsung',
        'price' : 15000000,
        'image': 'https://vtv1.mediacdn.vn/2019/10/10/photo-1-15706463929181755249740.jpg'
    }, {
        'id' : 1,
        'name' : 'Samsung',
        'price' : 15000000,
        'image': 'https://vtv1.mediacdn.vn/2019/10/10/photo-1-15706463929181755249740.jpg'
    }]
    
    if kw:
        products =  [p for p in products if p['name'].find(kw) >= 0]
    return products