# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protoc/health.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13protoc/health.proto\x12\x05\x61\x63rux\"%\n\x12HealthCheckRequest\x12\x0f\n\x07service\x18\x01 \x01(\t\"\xa0\x01\n\x13HealthCheckResponse\x12\x38\n\x06status\x18\x01 \x01(\x0e\x32(.acrux.HealthCheckResponse.ServingStatus\"O\n\rServingStatus\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07SERVING\x10\x01\x12\x0f\n\x0bNOT_SERVING\x10\x02\x12\x13\n\x0fSERVICE_UNKNOWN\x10\x03\x32\x8a\x01\n\x06Health\x12>\n\x05\x43heck\x12\x19.acrux.HealthCheckRequest\x1a\x1a.acrux.HealthCheckResponse\x12@\n\x05Watch\x12\x19.acrux.HealthCheckRequest\x1a\x1a.acrux.HealthCheckResponse0\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protoc.health_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_HEALTHCHECKREQUEST']._serialized_start=30
  _globals['_HEALTHCHECKREQUEST']._serialized_end=67
  _globals['_HEALTHCHECKRESPONSE']._serialized_start=70
  _globals['_HEALTHCHECKRESPONSE']._serialized_end=230
  _globals['_HEALTHCHECKRESPONSE_SERVINGSTATUS']._serialized_start=151
  _globals['_HEALTHCHECKRESPONSE_SERVINGSTATUS']._serialized_end=230
  _globals['_HEALTH']._serialized_start=233
  _globals['_HEALTH']._serialized_end=371
# @@protoc_insertion_point(module_scope)
