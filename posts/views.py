"""Posts views."""

# Django
from django.http import HttpResponse

# utilities
from datetime import datetime

POSTS = [
    dict(
        name='Mont Blac',
        user='Yesica Cortes',
        timestamp=datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        picture='https://picsum.photos/200/200/?image=1036',
    ),
    dict(
        name='Via Láctea',
        user='C. Vander',
        timestamp=datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        picture='https://picsum.photos/200/200/?image=903',
    ),
    dict(
        name='Nuevo auditorio',
        user='Thespianartist',
        timestamp=datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        picture='https://picsum.photos/200/200/?image=1076',
    )
]


def list_posts(request):
    """List existing post."""
    content = []
    for post in POSTS:
        content.append("""
            <p><strong>{name}</strong></p>
            <p><small>{user} - <i> {timestamp}</i></small></p>
            <figure><img src="{picture}"/></figure>
        """.format(**post))
    return HttpResponse('<br>'.join(content))
