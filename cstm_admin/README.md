# Customizing ADMIN
1. Register models in admin.py
2. Make migrations
3. Create superuser
4. Add string representation to Models:
  ```
  class Customer(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)

    def __str__(self):
      return self.first_name + ' ' + self.last_name
  ```
  * It will show in admin/ customers as First Name and Last Name instead of Customer object.
  * W/o string representation:  
  ![cstm_obj](cstm_obj.png)
  * With string representation:
  ![customers](customers.png)

# ADMIN Templates
