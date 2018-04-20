#!/usr/bin/env python
import os
from distutils.core import setup, Extension
sources = [
    'src/python/core.c',
    'src/libwshash/io.c',
    'src/libwshash/internal.c',
    'src/libwshash/sha3.c']
if os.name == 'nt':
    sources += [
        'src/libwshash/util_win32.c',
        'src/libwshash/io_win32.c',
        'src/libwshash/mmap_win32.c',
    ]
else:
    sources += [
        'src/libwshash/io_posix.c'
    ]
depends = [
    'src/libwshash/wshash.h',
    'src/libwshash/compiler.h',
    'src/libwshash/data_sizes.h',
    'src/libwshash/endian.h',
    'src/libwshash/wshash.h',
    'src/libwshash/io.h',
    'src/libwshash/fnv.h',
    'src/libwshash/internal.h',
    'src/libwshash/sha3.h',
    'src/libwshash/util.h',
]
pywshash = Extension('pywshash',
                     sources=sources,
                     depends=depends,
                     extra_compile_args=["-Isrc/", "-std=gnu99", "-Wall"])

setup(
    name='pywshash',
    author="Matthew Wampler-Doty",
    author_email="matthew.wampler.doty@gmail.com",
    license='GPL',
    version='0.1.23',
    url='https://github.com/wiseplat/wshash',
    download_url='https://github.com/wiseplat/wshash/tarball/v23',
    description=('Python wrappers for wshash, the wiseplat proof of work'
                 'hashing function'),
    ext_modules=[pywshash],
)
