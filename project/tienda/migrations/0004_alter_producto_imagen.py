# tienda/migrations/0003_alter_producto_imagen.py

from django.db import migrations, models

def set_default_images(apps, schema_editor):
    Producto = apps.get_model('tienda', 'Producto')
    default_image_path = 'productos/default.jpg'  # Cambia esto al path de tu imagen por defecto

    for producto in Producto.objects.filter(imagen__isnull=True):
        producto.imagen = default_image_path
        producto.save()

class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_producto_imagen'),  # Asegúrate de que esta es la migración anterior correcta
    ]

    operations = [
        migrations.RunPython(set_default_images),
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(upload_to='productos/', null=False, blank=False),
        ),
    ]
