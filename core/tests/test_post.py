import pytest
from core.factories.post_factory import PostFactory

@pytest.mark.django_db
def test_post_creation_with_factory():
    post = PostFactory()
    
    assert post.id is not None
    assert isinstance(post.title, str)
    print(f"\nPost gerado: {post.title} por {post.author.username}")