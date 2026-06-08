import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:
    western_genre = Genre.objects.create(name="Western")
    action_genre = Genre.objects.create(name="Action")
    dramma_genre = Genre.objects.create(name="Dramma")
    actor_klooney = Actor.objects.create(first_name="George", last_name="Klooney")
    actor_reaves = Actor.objects.create(first_name="Kianu", last_name="Reaves")
    actress_keegan = Actor.objects.create(first_name="Scarlett", last_name="Keegan")
    actor_will_smith = Actor.objects.create(first_name="Will", last_name="Smith")
    actor_jaden_smith = Actor.objects.create(first_name="Jaden", last_name="Smith")
    actress_johansson = Actor.objects.create(first_name="Scarlett", last_name="Johansson")

    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(first_name="Kianu").update(first_name="Keanu", last_name="Reeves")

    action_genre.delete()
    actress_scarlett = Actor.objects.filter(first_name="Scarlett")
    actress_scarlett.delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
