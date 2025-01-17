from django.db import models

class Resource(models.Model):
    # Resource name
    name = models.CharField(max_length=200)  # Name of the resource

    # Type of resource (e.g., equipment, personnel, supplies)
    resource_type = models.CharField(
        max_length=100,
        choices=[
            ('equipment', 'Equipment'),
            ('personnel', 'Personnel'),
            ('supplies', 'Supplies'),
        ]
    )

    # Quantity of the resource
    quantity = models.PositiveIntegerField()

    # Location of the resource
    location = models.CharField(max_length=200)

    # Status of the resource
    status = models.CharField(
        max_length=100,
        choices=[
            ('available', 'Available'),
            ('in_use', 'In Use'),
            ('under_maintenance', 'Under Maintenance'),
        ]
    )

    # Timestamps for creation and last update
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name  # String representation of the resource
