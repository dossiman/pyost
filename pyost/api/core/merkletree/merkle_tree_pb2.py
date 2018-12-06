# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: core/merkletree/merkle_tree.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='core/merkletree/merkle_tree.proto',
  package='merkletree',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n!core/merkletree/merkle_tree.proto\x12\nmerkletree\"\x9b\x01\n\nMerkleTree\x12\x11\n\thash_list\x18\x01 \x03(\x0c\x12\x37\n\thash2_idx\x18\x02 \x03(\x0b\x32$.merkletree.MerkleTree.Hash2IdxEntry\x12\x10\n\x08leaf_num\x18\x03 \x01(\x05\x1a/\n\rHash2IdxEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\"\x9a\x01\n\rTXRMerkleTree\x12\"\n\x02mt\x18\x01 \x01(\x0b\x32\x16.merkletree.MerkleTree\x12\x36\n\x07tx2_txr\x18\x02 \x03(\x0b\x32%.merkletree.TXRMerkleTree.Tx2TxrEntry\x1a-\n\x0bTx2TxrEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\x62\x06proto3')
)




_MERKLETREE_HASH2IDXENTRY = _descriptor.Descriptor(
  name='Hash2IdxEntry',
  full_name='merkletree.MerkleTree.Hash2IdxEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='merkletree.MerkleTree.Hash2IdxEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='merkletree.MerkleTree.Hash2IdxEntry.value', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=158,
  serialized_end=205,
)

_MERKLETREE = _descriptor.Descriptor(
  name='MerkleTree',
  full_name='merkletree.MerkleTree',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hash_list', full_name='merkletree.MerkleTree.hash_list', index=0,
      number=1, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hash2_idx', full_name='merkletree.MerkleTree.hash2_idx', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='leaf_num', full_name='merkletree.MerkleTree.leaf_num', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_MERKLETREE_HASH2IDXENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=50,
  serialized_end=205,
)


_TXRMERKLETREE_TX2TXRENTRY = _descriptor.Descriptor(
  name='Tx2TxrEntry',
  full_name='merkletree.TXRMerkleTree.Tx2TxrEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='merkletree.TXRMerkleTree.Tx2TxrEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='merkletree.TXRMerkleTree.Tx2TxrEntry.value', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=317,
  serialized_end=362,
)

_TXRMERKLETREE = _descriptor.Descriptor(
  name='TXRMerkleTree',
  full_name='merkletree.TXRMerkleTree',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mt', full_name='merkletree.TXRMerkleTree.mt', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tx2_txr', full_name='merkletree.TXRMerkleTree.tx2_txr', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TXRMERKLETREE_TX2TXRENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=208,
  serialized_end=362,
)

_MERKLETREE_HASH2IDXENTRY.containing_type = _MERKLETREE
_MERKLETREE.fields_by_name['hash2_idx'].message_type = _MERKLETREE_HASH2IDXENTRY
_TXRMERKLETREE_TX2TXRENTRY.containing_type = _TXRMERKLETREE
_TXRMERKLETREE.fields_by_name['mt'].message_type = _MERKLETREE
_TXRMERKLETREE.fields_by_name['tx2_txr'].message_type = _TXRMERKLETREE_TX2TXRENTRY
DESCRIPTOR.message_types_by_name['MerkleTree'] = _MERKLETREE
DESCRIPTOR.message_types_by_name['TXRMerkleTree'] = _TXRMERKLETREE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MerkleTree = _reflection.GeneratedProtocolMessageType('MerkleTree', (_message.Message,), dict(

  Hash2IdxEntry = _reflection.GeneratedProtocolMessageType('Hash2IdxEntry', (_message.Message,), dict(
    DESCRIPTOR = _MERKLETREE_HASH2IDXENTRY,
    __module__ = 'core.merkletree.merkle_tree_pb2'
    # @@protoc_insertion_point(class_scope:merkletree.MerkleTree.Hash2IdxEntry)
    ))
  ,
  DESCRIPTOR = _MERKLETREE,
  __module__ = 'core.merkletree.merkle_tree_pb2'
  # @@protoc_insertion_point(class_scope:merkletree.MerkleTree)
  ))
_sym_db.RegisterMessage(MerkleTree)
_sym_db.RegisterMessage(MerkleTree.Hash2IdxEntry)

TXRMerkleTree = _reflection.GeneratedProtocolMessageType('TXRMerkleTree', (_message.Message,), dict(

  Tx2TxrEntry = _reflection.GeneratedProtocolMessageType('Tx2TxrEntry', (_message.Message,), dict(
    DESCRIPTOR = _TXRMERKLETREE_TX2TXRENTRY,
    __module__ = 'core.merkletree.merkle_tree_pb2'
    # @@protoc_insertion_point(class_scope:merkletree.TXRMerkleTree.Tx2TxrEntry)
    ))
  ,
  DESCRIPTOR = _TXRMERKLETREE,
  __module__ = 'core.merkletree.merkle_tree_pb2'
  # @@protoc_insertion_point(class_scope:merkletree.TXRMerkleTree)
  ))
_sym_db.RegisterMessage(TXRMerkleTree)
_sym_db.RegisterMessage(TXRMerkleTree.Tx2TxrEntry)


_MERKLETREE_HASH2IDXENTRY._options = None
_TXRMERKLETREE_TX2TXRENTRY._options = None
# @@protoc_insertion_point(module_scope)