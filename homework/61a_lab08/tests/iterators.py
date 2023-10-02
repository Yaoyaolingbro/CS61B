test = {
  'name': 'Iterators',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> s = [1, 2, 3, 4]
          >>> t = iter(s)
          >>> next(s)
          Error
          >>> next(t)
          1
          >>> next(t)
          2
          >>> iter(s)
          Iterator
          >>> next(iter(s))
          1
          >>> next(iter(t))
          3
          >>> next(iter(s))
          1
          >>> next(iter(t))
          4
          >>> next(t)
          StopIteration
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> r = range(6)
          >>> r_iter = iter(r)
          >>> next(r_iter)
          7c2ddff07764c87227f4781f812caaa6
          # locked
          >>> [x + 1 for x in r]
          0c410dd19a8d0a28b3a24c56a9aabcee
          # locked
          >>> [x + 1 for x in r_iter]
          6375edda2e779f242ebb2e412da9e646
          # locked
          >>> next(r_iter)
          9b1c2bbd843829a055e5c1f4c81ee0ac
          # locked
          >>> list(range(-2, 4))   # Converts an iterable into a list
          3ceafa2e318cfa0f14d141faeda625de
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> map_iter = map(lambda x : x + 10, range(5))
          >>> next(map_iter)
          8be8039fce6ea3657f1a0a9143efa89d
          # locked
          >>> next(map_iter)
          65c7a6b2333beaaa4b87d5098965051a
          # locked
          >>> list(map_iter)
          120a1fd7e4e4d1126fc8dca6566516df
          # locked
          >>> for e in filter(lambda x : x % 2 == 0, range(1000, 1008)):
          ...     print(e)
          6812c36ce75fc0b1c442b1d56b8c98f1
          cfb302bc8dbdc7c3966ea71fce1fbec7
          3af14832fca7935c586fc6d9c315db16
          31fa8a7bbf5b8b2fc6fc6af2ceb961d4
          # locked
          >>> [x + y for x, y in zip([1, 2, 3], [4, 5, 6])]
          96f62c367d50ef7d7bc709af99261a94
          # locked
          >>> for e in zip([10, 9, 8], range(3)):
          ...   print(tuple(map(lambda x: x + 2, e)))
          1907e1cea9ea1c3cdff7ae484bbcb8d2
          a082e97edaad9eb45979d4fba2461abc
          227a49e36e48a29783c5dcf9b8539837
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
