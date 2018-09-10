Approach 1

Table - Store
Columns
id - IntergerField
name - CharField
address - TextField
short_address - TextField
image - TextField
pickup_point - CharField
lat - DecimalField
long - DecimalField
is_open - BooleanField


Table - MainCategory
id - IntegerField
name - Charfield
store_id - ForeignKey(Store - id)


Table - SubCategory
id - IntegerField
name - Charfield
parent_id - IntegerField // this can refer to main category primary key or stores primary key
type - Charfield // type can be two values 'store' or 'main_category'


Table - Menu
id - IntegerField
name - CharField
isVegetarian - BooleanField
image - TextField
sub_category_id - Foreignkey(SubCategory - id)
price - FloatField

Advantages
Get MainCategory items from Store table requires 1 jump

Disadvantages
SubCategory parent_id can reference to either stores primary id or main categories primary id so referential integrity is lost


Approach 2

Table - Store
Columns
id - IntergerField
name - CharField
address - TextField
short_address - TextField
image - TextField
pickup_point - CharField
lat - DecimalField
long - DecimalField
is_open - BooleanField


Table - MainCategory
id - IntegerField
name - Charfield


Table - SubCategory
id - IntegerField
name - Charfield
main_category_id - ForeignKey(MainCategory - id) // can be null
store_id - ForeignKey(Store - id) // can be null


Table - Menu
id - IntegerField
name - CharField
isVegetarian - BooleanField
image - TextField
sub_category_id - Foreignkey(SubCategory - id)
price - FloatField

Advantages
Get MainCategory items from Store table requires 2 jumps. Get sub categories from sub categories get main categories

Disadvantages
Refrential integrity is maintained in sub category table

Conclusion

I would go with Approach 2 since it maintains refrential integrity.









