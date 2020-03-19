"""
For creating C++ templates. 
Write the code string in 
`code` variable and specify
data types in string arguments.
"""
data_types = [
    'bool',
    'short',
    'unsigned short',
    'int',
    'unsigned int',
    'long',
    'unsigned long',
    'long long',
    'unsigned long long',
    'float',
    'double',
    'long double'
]

code = ("template class TensorCPU<%s>;")

for dt in data_types:
    print(code%(dt))
