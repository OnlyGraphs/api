# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ingress_controller.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ingress_controller.proto',
  package='ingress_controller',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x18ingress_controller.proto\x12\x12ingress_controller\"\x14\n\x12UpdateIndexRequest\",\n\x10UpdateIndexReply\x12\x18\n\x10numberUrlUpdates\x18\x01 \x01(\x03\x32r\n\x11IngressController\x12]\n\x0bupdateIndex\x12&.ingress_controller.UpdateIndexRequest\x1a$.ingress_controller.UpdateIndexReply\"\x00\x62\x06proto3'
)




_UPDATEINDEXREQUEST = _descriptor.Descriptor(
  name='UpdateIndexRequest',
  full_name='ingress_controller.UpdateIndexRequest',
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
  serialized_start=48,
  serialized_end=68,
)


_UPDATEINDEXREPLY = _descriptor.Descriptor(
  name='UpdateIndexReply',
  full_name='ingress_controller.UpdateIndexReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='numberUrlUpdates', full_name='ingress_controller.UpdateIndexReply.numberUrlUpdates', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=70,
  serialized_end=114,
)

DESCRIPTOR.message_types_by_name['UpdateIndexRequest'] = _UPDATEINDEXREQUEST
DESCRIPTOR.message_types_by_name['UpdateIndexReply'] = _UPDATEINDEXREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UpdateIndexRequest = _reflection.GeneratedProtocolMessageType('UpdateIndexRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEINDEXREQUEST,
  '__module__' : 'ingress_controller_pb2'
  # @@protoc_insertion_point(class_scope:ingress_controller.UpdateIndexRequest)
  })
_sym_db.RegisterMessage(UpdateIndexRequest)

UpdateIndexReply = _reflection.GeneratedProtocolMessageType('UpdateIndexReply', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEINDEXREPLY,
  '__module__' : 'ingress_controller_pb2'
  # @@protoc_insertion_point(class_scope:ingress_controller.UpdateIndexReply)
  })
_sym_db.RegisterMessage(UpdateIndexReply)



_INGRESSCONTROLLER = _descriptor.ServiceDescriptor(
  name='IngressController',
  full_name='ingress_controller.IngressController',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=116,
  serialized_end=230,
  methods=[
  _descriptor.MethodDescriptor(
    name='updateIndex',
    full_name='ingress_controller.IngressController.updateIndex',
    index=0,
    containing_service=None,
    input_type=_UPDATEINDEXREQUEST,
    output_type=_UPDATEINDEXREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_INGRESSCONTROLLER)

DESCRIPTOR.services_by_name['IngressController'] = _INGRESSCONTROLLER

# @@protoc_insertion_point(module_scope)
