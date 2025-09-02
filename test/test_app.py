from app import index
from app import perulangan

def test_index():
	assert index() == "Hello, world!"

def test_perulangan():
	assert perulangan() == [1,2,3,4,5,6,7,8,9,10]
