# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.ads.google_ads.v2.proto.resources import keyword_plan_ad_group_pb2 as google_dot_ads_dot_googleads__v2_dot_proto_dot_resources_dot_keyword__plan__ad__group__pb2
from google.ads.google_ads.v2.proto.services import keyword_plan_ad_group_service_pb2 as google_dot_ads_dot_googleads__v2_dot_proto_dot_services_dot_keyword__plan__ad__group__service__pb2


class KeywordPlanAdGroupServiceStub(object):
  """Proto file describing the keyword plan ad group service.

  Service to manage Keyword Plan ad groups.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetKeywordPlanAdGroup = channel.unary_unary(
        '/google.ads.googleads.v2.services.KeywordPlanAdGroupService/GetKeywordPlanAdGroup',
        request_serializer=google_dot_ads_dot_googleads__v2_dot_proto_dot_services_dot_keyword__plan__ad__group__service__pb2.GetKeywordPlanAdGroupRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v2_dot_proto_dot_resources_dot_keyword__plan__ad__group__pb2.KeywordPlanAdGroup.FromString,
        )
    self.MutateKeywordPlanAdGroups = channel.unary_unary(
        '/google.ads.googleads.v2.services.KeywordPlanAdGroupService/MutateKeywordPlanAdGroups',
        request_serializer=google_dot_ads_dot_googleads__v2_dot_proto_dot_services_dot_keyword__plan__ad__group__service__pb2.MutateKeywordPlanAdGroupsRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v2_dot_proto_dot_services_dot_keyword__plan__ad__group__service__pb2.MutateKeywordPlanAdGroupsResponse.FromString,
        )


class KeywordPlanAdGroupServiceServicer(object):
  """Proto file describing the keyword plan ad group service.

  Service to manage Keyword Plan ad groups.
  """

  def GetKeywordPlanAdGroup(self, request, context):
    """Returns the requested Keyword Plan ad group in full detail.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MutateKeywordPlanAdGroups(self, request, context):
    """Creates, updates, or removes Keyword Plan ad groups. Operation statuses are
    returned.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_KeywordPlanAdGroupServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetKeywordPlanAdGroup': grpc.unary_unary_rpc_method_handler(
          servicer.GetKeywordPlanAdGroup,
          request_deserializer=google_dot_ads_dot_googleads__v2_dot_proto_dot_services_dot_keyword__plan__ad__group__service__pb2.GetKeywordPlanAdGroupRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v2_dot_proto_dot_resources_dot_keyword__plan__ad__group__pb2.KeywordPlanAdGroup.SerializeToString,
      ),
      'MutateKeywordPlanAdGroups': grpc.unary_unary_rpc_method_handler(
          servicer.MutateKeywordPlanAdGroups,
          request_deserializer=google_dot_ads_dot_googleads__v2_dot_proto_dot_services_dot_keyword__plan__ad__group__service__pb2.MutateKeywordPlanAdGroupsRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v2_dot_proto_dot_services_dot_keyword__plan__ad__group__service__pb2.MutateKeywordPlanAdGroupsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.ads.googleads.v2.services.KeywordPlanAdGroupService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
