import pytest
from ..factories.post_factory import PostFactory
from ..serializers.post_serializer import PostSerializer


@pytest.mark.django_db
def test_post_serializer_valid_data():
    post = PostFactory()

    serializer = PostSerializer(post)
    data = serializer.data

    assert data["title"] == post.title
    assert data["slug"] == post.slug
    assert data["author"] == post.author.username
    assert "image" in data
    assert data["status"] == 1


@pytest.mark.django_db
def test_post_serializer_fields_content():
    post = PostFactory(title="Teste de Serializer", content="Conteúdo específico")
    serializer = PostSerializer(post)

    expected_fields = {
        "id",
        "title",
        "slug",
        "author",
        "content",
        "image",
        "created_on",
        "status",
    }

    assert set(serializer.data.keys()) == expected_fields
    assert serializer.data["title"] == "Teste de Serializer"
