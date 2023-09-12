from django.core.management.base import BaseCommand
# from myapp2.models import User
from ...models import Author, Post


class Command(BaseCommand):
    help = "Get post by author id best."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Author ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        posts = Post.objects.filter(author__pk=pk)
        intro = f'All posts\n'
        text = '\n'.join(post.content for post in posts)
        self.stdout.write(f'{intro}{text}')
