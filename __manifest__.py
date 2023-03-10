{
    'name': 'Product Grade POS',
    'version': '16.0.1.0.0',
    'depends': [
        'base',
        'point_of_sale',
    ],
    'data': [
        'views/product_product.xml',
    ],
    'assets': {
        'point_of_sale.assets': [
            '/product_grade_pos/static/src/js/product.js',
            '/product_grade_pos/static/src/xml/point_of_sale.xml',
            '/product_grade_pos/static/src/xml/order_reciept.xml',
        ],
    },
}
