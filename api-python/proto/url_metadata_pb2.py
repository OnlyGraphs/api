# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/url_metadata.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18proto/url_metadata.proto\x12\x0curl_metadata\":\n\x12UrlMetadataRequest\x12\x0e\n\x06\x64omain\x18\x01 \x01(\t\x12\x14\n\x0c\x61rticleTitle\x18\x02 \x01(\t\"2\n\x17lastUpdatedDateResponse\x12\x17\n\x0flastIndexedDate\x18\x01 \x01(\t2r\n\x0bUrlMetadata\x12\x63\n\x16getLastUpdatedDateTime\x12 .url_metadata.UrlMetadataRequest\x1a%.url_metadata.lastUpdatedDateResponse\"\x00\x62\x06proto3')



_URLMETADATAREQUEST = DESCRIPTOR.message_types_by_name['UrlMetadataRequest']
_LASTUPDATEDDATERESPONSE = DESCRIPTOR.message_types_by_name['lastUpdatedDateResponse']
UrlMetadataRequest = _reflection.GeneratedProtocolMessageType('UrlMetadataRequest', (_message.Message,), {
  'DESCRIPTOR' : _URLMETADATAREQUEST,
  '__module__' : 'proto.url_metadata_pb2'
  # @@protoc_insertion_point(class_scope:url_metadata.UrlMetadataRequest)
  })
_sym_db.RegisterMessage(UrlMetadataRequest)

lastUpdatedDateResponse = _reflection.GeneratedProtocolMessageType('lastUpdatedDateResponse', (_message.Message,), {
  'DESCRIPTOR' : _LASTUPDATEDDATERESPONSE,
  '__module__' : 'proto.url_metadata_pb2'
  # @@protoc_insertion_point(class_scope:url_metadata.lastUpdatedDateResponse)
  })
_sym_db.RegisterMessage(lastUpdatedDateResponse)

_URLMETADATA = DESCRIPTOR.services_by_name['UrlMetadata']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _URLMETADATAREQUEST._serialized_start=42
  _URLMETADATAREQUEST._serialized_end=100
  _LASTUPDATEDDATERESPONSE._serialized_start=102
  _LASTUPDATEDDATERESPONSE._serialized_end=152
  _URLMETADATA._serialized_start=154
  _URLMETADATA._serialized_end=268
# @@protoc_insertion_point(module_scope)
