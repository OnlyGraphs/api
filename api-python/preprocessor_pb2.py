# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: preprocessor.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='preprocessor.proto',
  package='preprocessor',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x12preprocessor.proto\x12\x0cpreprocessor\"b\n\x13PreprocessorRequest\x12\x0f\n\x07rawText\x18\x01 \x01(\t\x12:\n\x11processingOptions\x18\x02 \x01(\x0b\x32\x1f.preprocessor.ProcessingOptions\"\xb2\x01\n\x11ProcessingOptions\x12>\n\x13tokenisationOptions\x18\x01 \x01(\x0b\x32!.preprocessor.TokenisationOptions\x12\x10\n\x08\x66oldCase\x18\x02 \x01(\x08\x12\x17\n\x0fremoveStopWords\x18\x03 \x01(\x08\x12\x32\n\rnormalisation\x18\x04 \x01(\x0e\x32\x1b.preprocessor.Normalisation\"\x98\x01\n\x13TokenisationOptions\x12\x15\n\rremoveNumbers\x18\x01 \x01(\x08\x12\x19\n\x11removeCoordinates\x18\x02 \x01(\x08\x12\x13\n\x0bremoveDates\x18\x03 \x01(\x08\x12\x1f\n\x17removeSpecialCharacters\x18\x04 \x01(\x08\x12\x19\n\x11removePunctuation\x18\x05 \x01(\x08\"4\n\x18PreprocessorTextResponse\x12\x18\n\x10preprocessedText\x18\x01 \x03(\t*:\n\rNormalisation\x12\x08\n\x04None\x10\x00\x12\x0c\n\x08Stemming\x10\x01\x12\x11\n\rLemmatisation\x10\x02\x32m\n\x0cPreprocessor\x12]\n\x0epreprocessText\x12!.preprocessor.PreprocessorRequest\x1a&.preprocessor.PreprocessorTextResponse\"\x00\x62\x06proto3'
)

_NORMALISATION = _descriptor.EnumDescriptor(
  name='Normalisation',
  full_name='preprocessor.Normalisation',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='None', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Stemming', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Lemmatisation', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=526,
  serialized_end=584,
)
_sym_db.RegisterEnumDescriptor(_NORMALISATION)

Normalisation = enum_type_wrapper.EnumTypeWrapper(_NORMALISATION)
globals()['None'] = 0
Stemming = 1
Lemmatisation = 2



_PREPROCESSORREQUEST = _descriptor.Descriptor(
  name='PreprocessorRequest',
  full_name='preprocessor.PreprocessorRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='rawText', full_name='preprocessor.PreprocessorRequest.rawText', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='processingOptions', full_name='preprocessor.PreprocessorRequest.processingOptions', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=36,
  serialized_end=134,
)


_PROCESSINGOPTIONS = _descriptor.Descriptor(
  name='ProcessingOptions',
  full_name='preprocessor.ProcessingOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tokenisationOptions', full_name='preprocessor.ProcessingOptions.tokenisationOptions', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='foldCase', full_name='preprocessor.ProcessingOptions.foldCase', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='removeStopWords', full_name='preprocessor.ProcessingOptions.removeStopWords', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='normalisation', full_name='preprocessor.ProcessingOptions.normalisation', index=3,
      number=4, type=14, cpp_type=8, label=1,
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
  serialized_start=137,
  serialized_end=315,
)


_TOKENISATIONOPTIONS = _descriptor.Descriptor(
  name='TokenisationOptions',
  full_name='preprocessor.TokenisationOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='removeNumbers', full_name='preprocessor.TokenisationOptions.removeNumbers', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='removeCoordinates', full_name='preprocessor.TokenisationOptions.removeCoordinates', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='removeDates', full_name='preprocessor.TokenisationOptions.removeDates', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='removeSpecialCharacters', full_name='preprocessor.TokenisationOptions.removeSpecialCharacters', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='removePunctuation', full_name='preprocessor.TokenisationOptions.removePunctuation', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=318,
  serialized_end=470,
)


_PREPROCESSORTEXTRESPONSE = _descriptor.Descriptor(
  name='PreprocessorTextResponse',
  full_name='preprocessor.PreprocessorTextResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='preprocessedText', full_name='preprocessor.PreprocessorTextResponse.preprocessedText', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=472,
  serialized_end=524,
)

_PREPROCESSORREQUEST.fields_by_name['processingOptions'].message_type = _PROCESSINGOPTIONS
_PROCESSINGOPTIONS.fields_by_name['tokenisationOptions'].message_type = _TOKENISATIONOPTIONS
_PROCESSINGOPTIONS.fields_by_name['normalisation'].enum_type = _NORMALISATION
DESCRIPTOR.message_types_by_name['PreprocessorRequest'] = _PREPROCESSORREQUEST
DESCRIPTOR.message_types_by_name['ProcessingOptions'] = _PROCESSINGOPTIONS
DESCRIPTOR.message_types_by_name['TokenisationOptions'] = _TOKENISATIONOPTIONS
DESCRIPTOR.message_types_by_name['PreprocessorTextResponse'] = _PREPROCESSORTEXTRESPONSE
DESCRIPTOR.enum_types_by_name['Normalisation'] = _NORMALISATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PreprocessorRequest = _reflection.GeneratedProtocolMessageType('PreprocessorRequest', (_message.Message,), {
  'DESCRIPTOR' : _PREPROCESSORREQUEST,
  '__module__' : 'preprocessor_pb2'
  # @@protoc_insertion_point(class_scope:preprocessor.PreprocessorRequest)
  })
_sym_db.RegisterMessage(PreprocessorRequest)

ProcessingOptions = _reflection.GeneratedProtocolMessageType('ProcessingOptions', (_message.Message,), {
  'DESCRIPTOR' : _PROCESSINGOPTIONS,
  '__module__' : 'preprocessor_pb2'
  # @@protoc_insertion_point(class_scope:preprocessor.ProcessingOptions)
  })
_sym_db.RegisterMessage(ProcessingOptions)

TokenisationOptions = _reflection.GeneratedProtocolMessageType('TokenisationOptions', (_message.Message,), {
  'DESCRIPTOR' : _TOKENISATIONOPTIONS,
  '__module__' : 'preprocessor_pb2'
  # @@protoc_insertion_point(class_scope:preprocessor.TokenisationOptions)
  })
_sym_db.RegisterMessage(TokenisationOptions)

PreprocessorTextResponse = _reflection.GeneratedProtocolMessageType('PreprocessorTextResponse', (_message.Message,), {
  'DESCRIPTOR' : _PREPROCESSORTEXTRESPONSE,
  '__module__' : 'preprocessor_pb2'
  # @@protoc_insertion_point(class_scope:preprocessor.PreprocessorTextResponse)
  })
_sym_db.RegisterMessage(PreprocessorTextResponse)



_PREPROCESSOR = _descriptor.ServiceDescriptor(
  name='Preprocessor',
  full_name='preprocessor.Preprocessor',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=586,
  serialized_end=695,
  methods=[
  _descriptor.MethodDescriptor(
    name='preprocessText',
    full_name='preprocessor.Preprocessor.preprocessText',
    index=0,
    containing_service=None,
    input_type=_PREPROCESSORREQUEST,
    output_type=_PREPROCESSORTEXTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_PREPROCESSOR)

DESCRIPTOR.services_by_name['Preprocessor'] = _PREPROCESSOR

# @@protoc_insertion_point(module_scope)
