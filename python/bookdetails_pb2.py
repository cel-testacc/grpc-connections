# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bookdetails.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x62ookdetails.proto\"@\n\x0f\x42ookDetailsData\x12\x0e\n\x06\x61uthor\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0e\n\x06quotes\x18\x03 \x01(\t\"$\n\x12\x42ookDetailsRequest\x12\x0e\n\x06\x61uthor\x18\x01 \x01(\t\"<\n\x13\x42ookDetailsResponse\x12%\n\x0b\x62ookDetails\x18\x01 \x03(\x0b\x32\x10.BookDetailsData2J\n\x0b\x42ookDetails\x12;\n\x0eGetBookDetails\x12\x13.BookDetailsRequest\x1a\x14.BookDetailsResponseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bookdetails_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BOOKDETAILSDATA._serialized_start=21
  _BOOKDETAILSDATA._serialized_end=85
  _BOOKDETAILSREQUEST._serialized_start=87
  _BOOKDETAILSREQUEST._serialized_end=123
  _BOOKDETAILSRESPONSE._serialized_start=125
  _BOOKDETAILSRESPONSE._serialized_end=185
  _BOOKDETAILS._serialized_start=187
  _BOOKDETAILS._serialized_end=261
# @@protoc_insertion_point(module_scope)
