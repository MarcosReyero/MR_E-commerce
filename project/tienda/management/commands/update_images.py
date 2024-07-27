# create a custom management command
# in tienda/management/commands/update_images.py
from django.core.management.base import BaseCommand
from tienda.models import Producto

class Command(BaseCommand):
    help = 'Update existing products with default image'

    def handle(self, *args, **kwargs):
        default_image_path = 'path/to/default/image.jpg'  # Cambia esto al path de tu imagen por defecto

        for producto in Producto.objects.filter(imagen__isnull=True):
            producto.imagen = default_image_path
            producto.save()

        self.stdout.write(self.style.SUCCESS('Successfully updated products with default image'))
