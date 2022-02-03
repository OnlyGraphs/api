# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wiki_search.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='wiki_search.proto',
  package='wiki_search',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11wiki_search.proto\x12\x0bwiki_search\"\x13\n\x11\x43heckIndexRequest\"4\n\x0f\x43heckIndexReply\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x10\n\x08\x65rr_code\x18\x02 \x01(\t2[\n\nWikiSearch\x12M\n\x0bupdateIndex\x12\x1e.wiki_search.CheckIndexRequest\x1a\x1c.wiki_search.CheckIndexReply\"\x00\x62\x06proto3'
)




_CHECKINDEXREQUEST = _descriptor.Descriptor(
  name='CheckIndexRequest',
  full_name='wiki_search.CheckIndexRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=34,
  serialized_end=53,
)


_CHECKINDEXREPLY = _descriptor.Descriptor(
  name='CheckIndexReply',
  full_name='wiki_search.CheckIndexReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='wiki_search.CheckIndexReply.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='err_code', full_name='wiki_search.CheckIndexReply.err_code', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=55,
  serialized_end=107,
)

DESCRIPTOR.message_types_by_name['CheckIndexRequest'] = _CHECKINDEXREQUEST
DESCRIPTOR.message_types_by_name['CheckIndexReply'] = _CHECKINDEXREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CheckIndexRequest = _reflection.GeneratedProtocolMessageType('CheckIndexRequest', (_message.Message,), {
  'DESCRIPTOR' : _CHECKINDEXREQUEST,
  '__module__' : 'wiki_search_pb2'
  # @@protoc_insertion_point(class_scope:wiki_search.CheckIndexRequest)
  })
_sym_db.RegisterMessage(CheckIndexRequest)

CheckIndexReply = _reflection.GeneratedProtocolMessageType('CheckIndexReply', (_message.Message,), {
  'DESCRIPTOR' : _CHECKINDEXREPLY,
  '__module__' : 'wiki_search_pb2'
  # @@protoc_insertion_point(class_scope:wiki_search.CheckIndexReply)
  })
_sym_db.RegisterMessage(CheckIndexReply)



_WIKISEARCH = _descriptor.ServiceDescriptor(
  name='WikiSearch',
  full_name='wiki_search.WikiSearch',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=109,
  serialized_end=200,
  methods=[
  _descriptor.MethodDescriptor(
    name='updateIndex',
    full_name='wiki_search.WikiSearch.updateIndex',
    index=0,
    containing_service=None,
    input_type=_CHECKINDEXREQUEST,
    output_type=_CHECKINDEXREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_WIKISEARCH)

DESCRIPTOR.services_by_name['WikiSearch'] = _WIKISEARCH

# @@protoc_insertion_point(module_scope)
