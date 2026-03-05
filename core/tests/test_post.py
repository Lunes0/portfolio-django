import pytest
from core.factories.post_factory import PostFactory


@pytest.mark.django_db
def test_post_creation_with_factory():
    post = PostFactory()

    assert post.id is not None
    assert isinstance(post.title, str)
    assert post.image.name is not None
    assert "jpg" in post.image.name or "png" in post.image.name

    print(f"\nPost gerado: {post.title} por {post.author.username}")
    print(f"\nPost com imagem criado: {post.title}")
    print(f"Caminho da imagem: {post.image.url}")
