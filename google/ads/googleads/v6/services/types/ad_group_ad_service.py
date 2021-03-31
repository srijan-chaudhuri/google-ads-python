# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import proto  # type: ignore


from google.ads.googleads.v6.common.types import policy
from google.ads.googleads.v6.enums.types import (
    response_content_type as gage_response_content_type,
)
from google.ads.googleads.v6.resources.types import (
    ad_group_ad as gagr_ad_group_ad,
)
from google.protobuf import field_mask_pb2 as field_mask  # type: ignore
from google.rpc import status_pb2 as status  # type: ignore


__protobuf__ = proto.module(
    package="google.ads.googleads.v6.services",
    marshal="google.ads.googleads.v6",
    manifest={
        "GetAdGroupAdRequest",
        "MutateAdGroupAdsRequest",
        "AdGroupAdOperation",
        "MutateAdGroupAdsResponse",
        "MutateAdGroupAdResult",
    },
)


class GetAdGroupAdRequest(proto.Message):
    r"""Request message for
    [AdGroupAdService.GetAdGroupAd][google.ads.googleads.v6.services.AdGroupAdService.GetAdGroupAd].

    Attributes:
        resource_name (str):
            Required. The resource name of the ad to
            fetch.
    """

    resource_name = proto.Field(proto.STRING, number=1)


class MutateAdGroupAdsRequest(proto.Message):
    r"""Request message for
    [AdGroupAdService.MutateAdGroupAds][google.ads.googleads.v6.services.AdGroupAdService.MutateAdGroupAds].

    Attributes:
        customer_id (str):
            Required. The ID of the customer whose ads
            are being modified.
        operations (Sequence[google.ads.googleads.v6.services.types.AdGroupAdOperation]):
            Required. The list of operations to perform
            on individual ads.
        partial_failure (bool):
            If true, successful operations will be
            carried out and invalid operations will return
            errors. If false, all operations will be carried
            out in one transaction if and only if they are
            all valid. Default is false.
        validate_only (bool):
            If true, the request is validated but not
            executed. Only errors are returned, not results.
        response_content_type (google.ads.googleads.v6.enums.types.ResponseContentTypeEnum.ResponseContentType):
            The response content type setting. Determines
            whether the mutable resource or just the
            resource name should be returned post mutation.
    """

    customer_id = proto.Field(proto.STRING, number=1)
    operations = proto.RepeatedField(
        proto.MESSAGE, number=2, message="AdGroupAdOperation",
    )
    partial_failure = proto.Field(proto.BOOL, number=3)
    validate_only = proto.Field(proto.BOOL, number=4)
    response_content_type = proto.Field(
        proto.ENUM,
        number=5,
        enum=gage_response_content_type.ResponseContentTypeEnum.ResponseContentType,
    )


class AdGroupAdOperation(proto.Message):
    r"""A single operation (create, update, remove) on an ad group
    ad.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            FieldMask that determines which resource
            fields are modified in an update.
        policy_validation_parameter (google.ads.googleads.v6.common.types.PolicyValidationParameter):
            Configuration for how policies are validated.
        create (google.ads.googleads.v6.resources.types.AdGroupAd):
            Create operation: No resource name is
            expected for the new ad.
        update (google.ads.googleads.v6.resources.types.AdGroupAd):
            Update operation: The ad is expected to have
            a valid resource name.
        remove (str):
            Remove operation: A resource name for the removed ad is
            expected, in this format:

            ``customers/{customer_id}/adGroupAds/{ad_group_id}~{ad_id}``
    """

    update_mask = proto.Field(
        proto.MESSAGE, number=4, message=field_mask.FieldMask,
    )
    policy_validation_parameter = proto.Field(
        proto.MESSAGE, number=5, message=policy.PolicyValidationParameter,
    )
    create = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="operation",
        message=gagr_ad_group_ad.AdGroupAd,
    )
    update = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="operation",
        message=gagr_ad_group_ad.AdGroupAd,
    )
    remove = proto.Field(proto.STRING, number=3, oneof="operation")


class MutateAdGroupAdsResponse(proto.Message):
    r"""Response message for an ad group ad mutate.

    Attributes:
        partial_failure_error (google.rpc.status_pb2.Status):
            Errors that pertain to operation failures in the partial
            failure mode. Returned only when partial_failure = true and
            all errors occur inside the operations. If any errors occur
            outside the operations (e.g. auth errors), we return an RPC
            level error.
        results (Sequence[google.ads.googleads.v6.services.types.MutateAdGroupAdResult]):
            All results for the mutate.
    """

    partial_failure_error = proto.Field(
        proto.MESSAGE, number=3, message=status.Status,
    )
    results = proto.RepeatedField(
        proto.MESSAGE, number=2, message="MutateAdGroupAdResult",
    )


class MutateAdGroupAdResult(proto.Message):
    r"""The result for the ad mutate.

    Attributes:
        resource_name (str):
            The resource name returned for successful
            operations.
        ad_group_ad (google.ads.googleads.v6.resources.types.AdGroupAd):
            The mutated ad group ad with only mutable fields after
            mutate. The field will only be returned when
            response_content_type is set to "MUTABLE_RESOURCE".
    """

    resource_name = proto.Field(proto.STRING, number=1)
    ad_group_ad = proto.Field(
        proto.MESSAGE, number=2, message=gagr_ad_group_ad.AdGroupAd,
    )


__all__ = tuple(sorted(__protobuf__.manifest))