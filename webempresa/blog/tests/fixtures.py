import pytest

from blog.models import Category, Post


@pytest.fixture
def crear_category():
    genera, _ = Category.objects.get_or_create(name='General')
    desayuno, _ = Category.objects.get_or_create(name='Desayuno')
    merienda, _ = Category.objects.get_or_create(name='Merienda')

    return genera, desayuno, merienda


@pytest.fixture
def crear_post(crear_category):
    genera, desayuno, merienda = crear_category

    post_1 = Post.objects.get_or_create(title='Soy el post numero 1', content='Desde la api -post numero 1',
                                        author='David',
                                        category=desayuno,)

    return post_1
