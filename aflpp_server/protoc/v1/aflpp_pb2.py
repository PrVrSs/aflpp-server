# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protoc/v1/aflpp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15protoc/v1/aflpp.proto\x12\x08\x61\x66lpp.v1\"\'\n\x06Server\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\"V\n\x0cStartRequest\x12\x0e\n\x06\x62inary\x18\x01 \x01(\x0c\x12\x13\n\x0b\x62inary_args\x18\x02 \x01(\t\x12\x12\n\naflpp_args\x18\x03 \x01(\t\x12\r\n\x05seeds\x18\x04 \x03(\x0c\" \n\rStartResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"\r\n\x0bStopRequest\"\x1f\n\x0cStopResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x32|\n\x05\x41\x46LPP\x12:\n\x05start\x12\x16.aflpp.v1.StartRequest\x1a\x17.aflpp.v1.StartResponse\"\x00\x12\x37\n\x04stop\x12\x15.aflpp.v1.StopRequest\x1a\x16.aflpp.v1.StopResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protoc.v1.aflpp_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_SERVER']._serialized_start=35
  _globals['_SERVER']._serialized_end=74
  _globals['_STARTREQUEST']._serialized_start=76
  _globals['_STARTREQUEST']._serialized_end=162
  _globals['_STARTRESPONSE']._serialized_start=164
  _globals['_STARTRESPONSE']._serialized_end=196
  _globals['_STOPREQUEST']._serialized_start=198
  _globals['_STOPREQUEST']._serialized_end=211
  _globals['_STOPRESPONSE']._serialized_start=213
  _globals['_STOPRESPONSE']._serialized_end=244
  _globals['_AFLPP']._serialized_start=246
  _globals['_AFLPP']._serialized_end=370
# @@protoc_insertion_point(module_scope)
