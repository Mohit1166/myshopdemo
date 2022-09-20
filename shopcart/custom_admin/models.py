

from email.policy import default
from django.db import models
from django.contrib.auth.models import Group
from django.contrib.auth.models import User

class Configuration(models.Model):
    conf_key=models.CharField(max_length=45)
    conf_value=models.CharField(max_length=100)
    created_by=models.IntegerField()
    date=models.DateTimeField(auto_now_add=True)
    modify_by=models.IntegerField()
    modify_date=models.DateTimeField(auto_now=True)
    modify_status=models.BooleanField()
    class Meta:
        verbose_name="Configuration"
        verbose_name_plural="Configuration"


class Cms(models.Model):
    title=models.CharField(max_length=255)
    content=models.TextField()
    meta_title=models.TextField()
    meta_description=models.TextField()
    meta_keywords=models.TextField()
    created_by=models.IntegerField()
    created_by_date=models.DateTimeField(auto_now_add=True)
    modify_by=models.IntegerField()
    modify_date=models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name="Cms"
        verbose_name_plural="Cms"


class Banners(models.Model):
     Name=models.CharField(max_length=50, unique=True)
     banner_path=models.ImageField(blank=True, upload_to='Product_Images')
     status_bit=models.BooleanField()
     class Meta:
         db_table ="custom_admin_banners"
         verbose_name="Banners"
         verbose_name_plural="Banners"

class Email(models.Model):
    title=models.CharField(max_length=45)
    subject=models.CharField(max_length=255)
    content=models.TextField()
    created_by=models.IntegerField()
    created_date=models.DateTimeField(auto_now_add=True)
    modify_by=models.IntegerField()
    modify_date=models.DateTimeField(auto_now=True)
    class Meta:
         verbose_name="Emails"
         verbose_name_plural="Emails"


class Contacts(models.Model):
    name=models.CharField(max_length=45)
    email=models.EmailField()
    contact_no=models.CharField(max_length=45)
    message=models.TextField()
    note_admin=models.TextField()
    created_by=models.IntegerField()
    created_date=models.DateTimeField(auto_now_add=True)
    modify_by=models.IntegerField()
    modify_date=models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name="Contacts"
        verbose_name_plural="Contacts"
        

class Category(models.Model):
    name=models.CharField(max_length=100)
    parent_id=models.ForeignKey("self",null=True,blank=True,on_delete=models.CASCADE)
    created_by=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True,related_name='Category_create_by')
    created_date=models.DateTimeField(auto_now_add=True)
    modify_by=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True,related_name='Category_modified_by')
    modify_date=models.DateTimeField(auto_now=True)
    modify_status=models.BooleanField()
    class Meta:
        verbose_name="Category"
        verbose_name_plural="Category"
        
    def __str__(self):
        return self.name
        
class Products(models.Model):
      name=models.CharField(max_length=100)
      sku=models.CharField(max_length=100)
      short_description=models.CharField(max_length=100)
      long_description=models.TextField()
      price=models.FloatField()
      special_price=models.FloatField()
      from_special_price=models.DateField(auto_now=True)
      to_special_price=models.DateField(auto_now=True)
      modify_status=models.BooleanField()
      quantity=models.IntegerField()
      meta_title=models.CharField(max_length=45)   
      meta_desc=models.TextField()
      meta_keywords=models.TextField()
      created_by=models.IntegerField(default=1)
      #created_by = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True,related_name='created_by')
      created_date=models.DateTimeField(auto_now_add=True)
      modify_by=models.IntegerField(default=1)
      #modify_by = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True,related_name='modify_by')
      modify_date=models.DateTimeField(auto_now=True)
      is_featured=models.BooleanField()
      class Meta:
          verbose_name="Products"
          verbose_name_plural="Products"

      def __str__(self):
          return self.name

class ProductsCategory(models.Model):
    # product_id=models.IntegerField()
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    # category_id=models.IntegerField()
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    class Meta:
        verbose_name="ProductsCategory"
        verbose_name_plural="ProductsCategory"

    # def __str__(self):
    #     return self.product_id

class ProductsImages(models.Model):
    image=models.ImageField(upload_to='Product_Images',default='')
    modify_status=models.BooleanField()
    created_by=models.IntegerField()
    created_date=models.DateTimeField(auto_now_add=True)
    modify_by=models.IntegerField(default=1)
    modify_date=models.DateTimeField(auto_now=True)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    class Meta:
        verbose_name="ProductsImages"
        verbose_name_plural="ProductsImages"

  

class ProductAttributes(models.Model):
     name=models.CharField(max_length=45)
     created_by=models.IntegerField()
     created_date=models.DateTimeField(auto_now_add=True)
     modify_by=models.IntegerField()
     modify_date=models.DateTimeField(auto_now=True)
     class Meta:
        verbose_name="ProductAttributes"
        verbose_name_plural="ProductAttributes"
 
 
            
class ProductsAttributesValues(models.Model):
    product_attribute=models.ForeignKey(ProductAttributes, on_delete=models.CASCADE)
    attribute_value=models.CharField(max_length=45)
    created_by=models.IntegerField()
    created_date=models.DateTimeField(auto_now_add=True)
    modify_by=models.IntegerField()
    modify_date=models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name="ProductAttributesValues"
        verbose_name_plural="ProductAttributesValues"

class ProductsAsscos(models.Model):
    Product_id=models.IntegerField()
    Products_attri_id=models.ForeignKey(ProductAttributes,on_delete=models.CASCADE)
    Products_value_attri=models.ForeignKey("self",on_delete=models.CASCADE)
    class Meta:
        verbose_name="ProductsAsscos"
        verbose_name_plural="ProductsAsscos"


class User(models.Model):
    Firstname=models.CharField(max_length=45)
    Lastname=models.CharField(max_length=45)
    email=models.EmailField()
    password=models.CharField(max_length=45)
    status=models.BooleanField()
    created_date=models.DateTimeField(auto_now_add=True)
    Manager="M"
    Customer="C"
    Admin="A"
    choose_user=[(Manager,"Manager"),(Customer,"Customer"),(Admin,"Admin")]
    field = models.ForeignKey(Group,on_delete=models.CASCADE,related_name="user_group")
    user=models.CharField(max_length=2,choices=choose_user,)
    # fb_token=models.CharField(max_length=100)
    # twitter_token=models.CharField(max_length=100)
    # google_token=models.CharField(max_length=100)
    # registration_method=models.BooleanField()
    class Meta:
        verbose_name="User"
        verbose_name_plural="User"
    
class UserWishList(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    product_id=models.IntegerField()
    class Meta:
        verbose_name="UserWishList"
        verbose_name_plural="UserWishList"
    
class UserAddress(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    address_1=models.CharField(max_length=100)
    address_2=models.CharField(max_length=100)
    city=models.CharField(max_length=45)
    state=models.CharField(max_length=45)
    country=models.CharField(max_length=45)
    zipcode=models.CharField(max_length=45)
    class Meta:
        verbose_name="UserAddress"
        verbose_name_plural="UserAddress"

class Coupons(models.Model):
    Code=models.CharField(max_length=45)
    percent=models.FloatField()
    created_by=models.IntegerField()
    created_date=models.DateTimeField(auto_now_add=True)
    modify_by=models.IntegerField()
    modify_date=models.DateTimeField(auto_now=True)
    no_of_uses=models.IntegerField()
    class Meta:
        verbose_name="Coupons"
        verbose_name_plural="Coupons"

class CouponsUsed(models.Model):
    user_id=models.IntegerField()
    order_id=models.IntegerField()
    created_date=models.DateTimeField(auto_now_add=True)
    coupons_id=models.ForeignKey(Coupons,on_delete=models.CASCADE)
    class Meta:
        verbose_name="CouponsUsed"
        verbose_name_plural="CouponsUsed"

class PaymentGateway(models.Model):
    name=models.CharField(max_length=45)
    created_by=models.IntegerField()
    created_date=models.DateTimeField(auto_now_add=True)
    modify_by=models.IntegerField()
    modify_date=models.DateTimeField(auto_now=True)
    class Meta:

        verbose_name="PaymentGateway"
        verbose_name_plural="PaymentGateway"

class OrderDetails(models.Model):
    order_id = models.IntegerField()
    product_id = models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    amount = models.FloatField()


    class Meta:
        verbose_name = "OrderDetails"
        verbose_name_plural = "OrderDetails"


class UserOrder(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    shipping_method = models.IntegerField()
    AWB_NO =models.CharField(max_length=100)
    payment_gateway = models.ForeignKey(PaymentGateway,on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now=True)
    status = models.BooleanField()
    grand_total = models.FloatField()
    shipping_charges = models.FloatField()
    coupon_id = models.ForeignKey(Coupons,on_delete=models.CASCADE)
    billing_address_1 = models.CharField(max_length=100)
    billing_address_2 = models.CharField(max_length=100)
    billing_city = models.CharField(max_length=100)
    billing_state = models.CharField(max_length=100)
    billing_country = models.CharField(max_length=100)
    billing_zipcode = models.CharField(max_length=100)
    shipping_address_1 = models.CharField(max_length=100)
    shipping_address_2 = models.CharField(max_length=100)
    shipping_city = models.CharField(max_length=100)
    shipping_state = models.CharField(max_length=100)
    shipping_country = models.CharField(max_length=100)
    shipping_zipcode = models.CharField(max_length=100)

    class Meta:
        verbose_name = "UserOrder"
        verbose_name_plural = "UserOrder"



    





    









      
