# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ingress_controller.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18ingress_controller.proto\x12\x12ingress_controller\"\x14\n\x12UpdateIndexRequest\",\n\x10UpdateIndexReply\x12\x18\n\x10numberUrlUpdates\x18\x01 \x01(\x03\x32r\n\x11IngressController\x12]\n\x0bupdateIndex\x12&.ingress_controller.UpdateIndexRequest\x1a$.ingress_controller.UpdateIndexReply\"\x00\x62\x06proto3')



_UPDATEINDEXREQUEST = DESCRIPTOR.message_types_by_name['UpdateIndexRequest']
_UPDATEINDEXREPLY = DESCRIPTOR.message_types_by_name['UpdateIndexReply']
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

_INGRESSCONTROLLER = DESCRIPTOR.services_by_name['IngressController']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _UPDATEINDEXREQUEST._serialized_start=48
  _UPDATEINDEXREQUEST._serialized_end=68
  _UPDATEINDEXREPLY._serialized_start=70
  _UPDATEINDEXREPLY._serialized_end=114
  _INGRESSCONTROLLER._serialized_start=116
  _INGRESSCONTROLLER._serialized_end=230
# @@protoc_insertion_point(module_scope)