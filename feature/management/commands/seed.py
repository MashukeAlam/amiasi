import json
import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from feature.models import Feature

class Command(BaseCommand):
    help = 'Seed the Feature model with YouTube links from a JSON file'

    def handle(self, *args, **kwargs):
        path = 'youtube_links_by_topic.txt'  # Path to your JSON file
        try:
            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except FileNotFoundError:
            self.stderr.write(f"❌ File not found: {path}")
            return

        topics = list(data.keys())
        total_inserted = 0

        # Pick a default user (or adjust if multi-user context)
        user = User.objects.first()
        if not user:
            self.stderr.write("❌ No users found. Create a user first.")
            return

        for topic in topics:
            links = data[topic]
            selected_links = random.sample(links, min(20, len(links)))  # Seed 20 per topic

            for link in selected_links:
                Feature.objects.create(
                    feature_name='youtube_view',
                    link=link,
                    reward=random.randint(2, 5),  # Optional: vary reward
                    user=user
                )
                total_inserted += 1

        self.stdout.write(self.style.SUCCESS(f"✅ Seeded {total_inserted} Feature entries successfully!"))
