import pytest

test_data=[
    (b''),
    (os.urandom(8 * 1024)),
    (b'0' * 8 * 1024),
    (bytearray(b'')),
    (bytearray(os.urandom(8 * 1024))),
]
if sys.version_info > (2, 7):
    test_data += [
        (memoryview(b'')),
        (memoryview(os.urandom(8 * 1024)))
    ]

@pytest.fixture(
    params=test_data,
    ids=[
        'data' + str(i) for i in range(len(test_data))
    ]
)
def data(request):
    return request.param

@pytest.fixture(
    params=[
        (
            {
                'store_size': True
            }
        ),
        (
            {
                'store_size': False
            }
        ),
    ]
)
def store_size(request):
    return request.param

@pytest.fixture(
    params=[
        (
            {
                'return_bytearray': True
            }
        ),
        (
            {
                'return_bytearray': False
            }
        ),
    ]
)
def return_bytearray(request):
    return request.param

@pytest.fixture
def c_return_bytearray(return_bytearray):
    return return_bytearray

@pytest.fixture
def d_return_bytearray(return_bytearray):
    return return_bytearray

@pytest.fixture(
    params=[
        ('fast', None)
    ] + [
        ('fast', {'acceleration': s}) for s in range(10)
    ] + [
        ('high_compression', None)
    ] + [
        ('high_compression', {'compression': s}) for s in range(17)
    ] + [
        (None, None)
    ]
)
def mode(request):
    return request.param
