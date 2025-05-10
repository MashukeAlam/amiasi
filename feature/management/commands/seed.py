import json
import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from feature.models import Feature  # Adjust 'feature' to your app name

class Command(BaseCommand):
    help = 'Seed the Feature model with YouTube links for views, subscriptions, and likes'

    def handle(self, *args, **kwargs):
        # Initialize counters
        total_view_inserted = 0
        total_sub_inserted = 0
        total_like_inserted = 0
        duplicates_found = 0

        # Get all users or create test users if none exist
        users = User.objects.all()
        if not users:
            self.stdout.write("No users found. Creating test users...")
            for i in range(1, 6):
                User.objects.create_user(username=f'testuser{i}', password=f'testpass{i}123')
            users = User.objects.all()

        # Part 1: Seed youtube_view features from JSON file
        path = 'youtube_links_by_topic.txt'  # Path to your JSON file
        try:
            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except FileNotFoundError:
            self.stderr.write(f"❌ File not found: {path}")
            return

        topics = list(data.keys())
        default_user = users[0]  # Use first user for youtube_view features

        for topic in topics:
            links = data[topic]
            selected_links = random.sample(links, min(20, len(links)))  # Seed 20 per topic

            for link in selected_links:
                # Check for existing entries to avoid MultipleObjectsReturned
                existing_features = Feature.objects.filter(feature_name='youtube_view', link=link)
                if existing_features.count() > 1:
                    self.stderr.write(f"⚠️ Duplicate found: youtube_view, {link}. Skipping...")
                    duplicates_found += 1
                    continue
                elif existing_features.count() == 1:
                    total_view_inserted += 1
                    continue  # Entry exists, no need to create

                # Create new entry
                Feature.objects.create(
                    feature_name='youtube_view',
                    link=link,
                    reward=random.randint(2, 5),
                    user=default_user
                )
                total_view_inserted += 1

        # Part 2: Seed youtube_sub features with hardcoded YouTube channels
        youtube_channels = [
            {'name': 'T-Series', 'link': 'https://www.youtube.com/@tseries'},
            {'name': 'MrBeast', 'link': 'https://www.youtube.com/@MrBeast'},
            {'name': 'Cocomelon', 'link': 'https://www.youtube.com/@CoComelon'},
            {'name': 'SET India', 'link': 'https://www.youtube.com/@SETIndia'},
            {'name': 'Kids Diana Show', 'link': 'https://www.youtube.com/@KidsDianaShow'},
            {'name': 'PewDiePie', 'link': 'https://www.youtube.com/@PewDiePie'},
            {'name': 'Like Nastya', 'link': 'https://www.youtube.com/@LikeNastya'},
            {'name': 'Vlad and Niki', 'link': 'https://www.youtube.com/@VladandNiki'},
            {'name': 'Zee Music Company', 'link': 'https://www.youtube.com/@zeemusiccompany'},
            {'name': 'WWE', 'link': 'https://www.youtube.com/@WWE'},
            {'name': 'Sony SAB', 'link': 'https://www.youtube.com/@SonySAB'},
            {'name': 'BLACKPINK', 'link': 'https://www.youtube.com/@BLACKPINK'},
            {'name': 'ChuChu TV', 'link': 'https://www.youtube.com/@ChuChuTV'},
            {'name': 'Alan’s Universe', 'link': 'https://www.youtube.com/@Alans_Universe'},
            {'name': 'Zee TV', 'link': 'https://www.youtube.com/@zeetv'},
            {'name': 'Baby Shark - Pinkfong', 'link': 'https://www.youtube.com/@BabyShark'},
            {'name': '5-Minute Crafts', 'link': 'https://www.youtube.com/@5MinuteCraftsYouTube'},
            {'name': 'Justin Bieber', 'link': 'https://www.youtube.com/@justinbieber'},
            {'name': 'Dua Lipa', 'link': 'https://www.youtube.com/@DuaLipa'},
            {'name': 'Tasty', 'link': 'https://www.youtube.com/@tasty'},
        ]

        for channel in youtube_channels:
            # Check for existing entries to avoid MultipleObjectsReturned
            existing_features = Feature.objects.filter(feature_name='youtube_sub', link=channel['link'])
            if existing_features.count() > 1:
                self.stderr.write(f"⚠️ Duplicate found: youtube_sub, {channel['link']}. Skipping...")
                duplicates_found += 1
                continue
            elif existing_features.count() == 1:
                total_sub_inserted += 1
                continue  # Entry exists, no need to create

            # Create new entry
            Feature.objects.create(
                feature_name='youtube_sub',
                link=channel['link'],
                reward=random.randint(1, 10),
                user=random.choice(users)
            )
            total_sub_inserted += 1

        # Part 3: Seed youtube_like features with hardcoded YouTube videos
        youtube_videos = [
            {'name': 'Despacito', 'link': 'https://www.youtube.com/watch?v=kJQP7kiw5Fk'},
            {'name': 'Baby Shark Dance', 'link': 'https://www.youtube.com/watch?v=XqZsoesa55w'},
            {'name': 'Shape of You', 'link': 'https://www.youtube.com/watch?v=JGwWNGJdvx8'},
            {'name': 'See You Again', 'link': 'https://www.youtube.com/watch?v=RgKAFK5djSk'},
            {'name': 'Gangnam Style', 'link': 'https://www.youtube.com/watch?v=9bZkp7q19f0'},
            {'name': 'Uptown Funk', 'link': 'https://www.youtube.com/watch?v=OPf0YbXqDm0'},
            {'name': 'Blinding Lights', 'link': 'https://www.youtube.com/watch?v=4NRXx6U8ABQ'},
            {'name': 'Bohemian Rhapsody', 'link': 'https://www.youtube.com/watch?v=fJ9rUzIMcZQ'},
            {'name': 'Sweet Child O\' Mine', 'link': 'https://www.youtube.com/watch?v=1w7OgIMMRc4'},
            {'name': 'Perfect', 'link': 'https://www.youtube.com/watch?v=2Vv-BfVoq4g'},
            {'name': 'Thinking Out Loud', 'link': 'https://www.youtube.com/watch?v=lp-EO5I60KA'},
            {'name': 'Shake It Off', 'link': 'https://www.youtube.com/watch?v=nfWlot6h_JM'},
            {'name': 'Havana', 'link': 'https://www.youtube.com/watch?v=HCjNJDNzw8Y'},
            {'name': 'Roar', 'link': 'https://www.youtube.com/watch?v=CevxZvSJLk8'},
            {'name': 'Sorry', 'link': 'https://www.youtube.com/watch?v=fRh_vgS2dFE'},
            {'name': 'Bad Guy', 'link': 'https://www.youtube.com/watch?v=DyDfgMOUjCI'},
            {'name': 'Old Town Road', 'link': 'https://www.youtube.com/watch?v=r7qovpF4To0'},
            {'name': 'Dynamite', 'link': 'https://www.youtube.com/watch?v=gdZLi9oWNZg'},
            {'name': 'Levitating', 'link': 'https://www.youtube.com/watch?v=TUVcZfQe-Kw'},
            {'name': 'Drivers License', 'link': 'https://www.youtube.com/watch?v=ZmDBbnmKpqQ'},
        ]

        for video in youtube_videos:
            # Check for existing entries to avoid MultipleObjectsReturned
            existing_features = Feature.objects.filter(feature_name='youtube_like', link=video['link'])
            if existing_features.count() > 1:
                self.stderr.write(f"⚠️ Duplicate found: youtube_like, {video['link']}. Skipping...")
                duplicates_found += 1
                continue
            elif existing_features.count() == 1:
                total_like_inserted += 1
                continue  # Entry exists, no need to create

            # Create new entry
            Feature.objects.create(
                feature_name='youtube_like',
                link=video['link'],
                reward=random.randint(1, 5),
                user=random.choice(users)
            )
            total_like_inserted += 1

        # Output success message
        self.stdout.write(self.style.SUCCESS(
            f"✅ Seeded {total_view_inserted} YouTube view, {total_sub_inserted} YouTube subscription, "
            f"and {total_like_inserted} YouTube like Feature entries successfully!"
        ))
        if duplicates_found > 0:
            self.stderr.write(f"⚠️ Skipped {duplicates_found} duplicates. Consider cleaning up the database.")