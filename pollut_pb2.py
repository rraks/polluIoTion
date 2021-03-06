# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pollut.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pollut.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x0cpollut.proto\"I\n\tpollution\x12\r\n\x05PM2_5\x18\x01 \x01(\x05\x12\x12\n\nNOISELEVEL\x18\x02 \x01(\x02\x12\x0b\n\x03\x43O2\x18\x03 \x01(\x05\x12\x0c\n\x04PM10\x18\x04 \x01(\x05')
)




_POLLUTION = _descriptor.Descriptor(
  name='pollution',
  full_name='pollution',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='PM2_5', full_name='pollution.PM2_5', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='NOISELEVEL', full_name='pollution.NOISELEVEL', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='CO2', full_name='pollution.CO2', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='PM10', full_name='pollution.PM10', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=16,
  serialized_end=89,
)

DESCRIPTOR.message_types_by_name['pollution'] = _POLLUTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

pollution = _reflection.GeneratedProtocolMessageType('pollution', (_message.Message,), dict(
  DESCRIPTOR = _POLLUTION,
  __module__ = 'pollut_pb2'
  # @@protoc_insertion_point(class_scope:pollution)
  ))
_sym_db.RegisterMessage(pollution)


# @@protoc_insertion_point(module_scope)
