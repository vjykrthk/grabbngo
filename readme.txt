Table - Store
id - IntergerField
name - CharField
description - TextField
address - TextField
short_address - TextField
area - CharField
city - CharField
image - TextField
pickup_point - CharField
lat - DecimalField
long - DecimalField
is_open - BooleanField


Table - MainCategory
id - IntegerField
name - Charfield
description - TextField


Table - SubCategory
id - IntegerField
name - Charfield
description - TextField
main_category_id - ForeignKey(MainCategory - id) // can be null
store_id - ForeignKey(Store - id) // can be null


Table - Menu
id - IntegerField
name - CharField
description - TextField
isVegetarian - BooleanField
image - TextField
sub_category_id - Foreignkey(SubCategory - id)
price - FloatField


Table Customizer
id - IntegerField
description - TextField
menu_id - Foreignkey(Menu - id)
main_category_id - ForeignKey(MainCategory - id) // can be null
sub_category_id  - ForeignKey(SubCategory- id) // can be null
customizable_menu_id - Foreignkey(Menu - id)


Table AddOns
id - IntegerField
name - CharField
description - TextField
menu_id - Foreignkey(Menu - id)

Table AddOnItems
id - IntegerField
description - TextField
add_on_id - Foreignkey(AddOns id)
name - CharField
price  - FloatField
