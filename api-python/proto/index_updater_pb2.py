# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/index_updater.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19proto/index_updater.proto\x12\x0cindex_update\"\x98\x01\n\x12IndexUpdateRequest\x12\x0e\n\x06\x64omain\x18\x01 \x01(\t\x12\x14\n\x0c\x61rticleTitle\x18\x02 \x01(\t\x12\x17\n\x0flastUpdatedDate\x18\x03 \x01(\t\x12\x18\n\x10preprocessedText\x18\x04 \x03(\t\x12\x11\n\ttextLinks\x18\x05 \x03(\t\x12\x16\n\x0etextCategories\x18\x06 \x03(\t\"\x15\n\x13IndexUpdateResponse2e\n\x0bIndexUpdate\x12V\n\rupdateArticle\x12 .index_update.IndexUpdateRequest\x1a!.index_update.IndexUpdateResponse\"\x00\x62\x06proto3')



_INDEXUPDATEREQUEST = DESCRIPTOR.message_types_by_name['IndexUpdateRequest']
_INDEXUPDATERESPONSE = DESCRIPTOR.message_types_by_name['IndexUpdateResponse']
IndexUpdateRequest = _reflection.GeneratedProtocolMessageType('IndexUpdateRequest', (_message.Message,), {
  'DESCRIPTOR' : _INDEXUPDATEREQUEST,
  '__module__' : 'proto.index_updater_pb2'
  # @@protoc_insertion_point(class_scope:index_update.IndexUpdateRequest)
  })
_sym_db.RegisterMessage(IndexUpdateRequest)

IndexUpdateResponse = _reflection.GeneratedProtocolMessageType('IndexUpdateResponse', (_message.Message,), {
  'DESCRIPTOR' : _INDEXUPDATERESPONSE,
  '__module__' : 'proto.index_updater_pb2'
  # @@protoc_insertion_point(class_scope:index_update.IndexUpdateResponse)
  })
_sym_db.RegisterMessage(IndexUpdateResponse)

_INDEXUPDATE = DESCRIPTOR.services_by_name['IndexUpdate']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _INDEXUPDATEREQUEST._serialized_start=44
  _INDEXUPDATEREQUEST._serialized_end=196
  _INDEXUPDATERESPONSE._serialized_start=198
  _INDEXUPDATERESPONSE._serialized_end=219
  _INDEXUPDATE._serialized_start=221
  _INDEXUPDATE._serialized_end=322
# @@protoc_insertion_point(module_scope)
