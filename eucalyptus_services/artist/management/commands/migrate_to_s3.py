from django.core.management.base import BaseCommand
from django.core.files.storage import default_storage
from django.conf import settings
import os
from artist.models import Artist, Song

class Command(BaseCommand):
    help = 'Migrate existing media files to S3'

    def handle(self, *args, **options):
        self.stdout.write('Starting media migration to S3...')

        self.migrate_model_files(Artist, 'artist_logo')
        self.migrate_model_files(Song, 'artwork')

        self.stdout.write(self.style.SUCCESS('Media migration completed successfully!'))

    def migrate_model_files(self, model, field_name):
        for obj in model.objects.all():
            file_field = getattr(obj, field_name)
            if file_field and not file_field.name.startswith('http'):
                try:
                    local_path = os.path.join(settings.MEDIA_ROOT, file_field.name)
                    if os.path.exists(local_path):
                        with open(local_path, 'rb') as file:
                            s3_key = file_field.name
                            default_storage.save(s3_key, file)
                        self.stdout.write(f'Migrated {field_name} for {model.__name__} {obj.id}: {s3_key}')
                    else:
                        self.stdout.write(self.style.WARNING(f'File not found: {local_path}'))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f'Error migrating {field_name} for {model.__name__} {obj.id}: {str(e)}'))