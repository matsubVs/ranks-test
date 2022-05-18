import stripe
stripe.api_key = "sk_test_51L0UHYEPpILM5IwCVzkBiaERmX8frQ1GGut9Im6Us5JGWIMd1eJHQdT4SKTaODypLgx6jAouMBgLvna9GKCvBiFE00Pf4kXP9a"

session = stripe.checkout.Session.create(
  success_url="https://cdek-work.ru/",
  cancel_url="https://cdek-work.ru/",
  line_items=[
    {
	    'price_data': {
		    'currency': 'RUB',
		    'product_data': {
				'name': 'T-shirt',
			    'description': 'sd',
		    },
		    'unit_amount': 1000000,
	    },
        'quantity': 1,
    },
  ],
	discounts=[{
            'coupon': 'UY9Ta7x0',
        }],
	tax_id_collection={
		'enabled': True,
	},
  mode="payment",
)

print(session)
