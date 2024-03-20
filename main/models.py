from django.db import models

# Category modeli - Online do'kon toifalarini ifodalaydi
class Category(models.Model):
    name = models.CharField(max_length=100)  # Toifa nomi
    description = models.TextField()         # Toifa tavsifi



# Product modeli - Do'kondagi mahsulotlarni ifodalaydi
class Product(models.Model):
    name = models.CharField(max_length=100)                          # Mahsulot nomi
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Mahsulot toifasi
    description = models.TextField()                                  # Mahsulot tavsifi
    price = models.DecimalField(max_digits=10, decimal_places=2)      # Mahsulot narxi
    quantity_available = models.PositiveIntegerField(default=0)      # Mavjud mahsulotlar soni


# Cart modeli - Foydalanuvchining savatini ifodalaydi
class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Savatdagi mahsulot
    quantity = models.PositiveIntegerField(default=1)               # Mahsulotlar soni savatda


# Order modeli - Buyurtmalarni ifodalaydi
class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)           # Buyurtma uchun savat
    order_date = models.DateTimeField(auto_now_add=True)               # Buyurtma sanasi
    customer_name = models.CharField(max_length=100)                   # Xaridorning ismi
    customer_address = models.TextField()                              # Xaridorning manzili
    customer_phone = models.CharField(max_length=20)                    # Xaridorning telefon raqami
    payment_method = models.CharField(max_length=50)                   # To'lov usuli
    order_status = models.CharField(max_length=50, default='Pending')  # Buyurtma holati
