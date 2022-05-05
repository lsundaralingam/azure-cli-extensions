# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional, TYPE_CHECKING

from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

from ._configuration import DnsResolverManagementClientConfiguration
from .operations import DnsResolversOperations
from .operations import InboundEndpointsOperations
from .operations import OutboundEndpointsOperations
from .operations import DnsForwardingRulesetsOperations
from .operations import ForwardingRulesOperations
from .operations import VirtualNetworkLinksOperations
from .. import models


class DnsResolverManagementClient(object):
    """The DNS Resolver Management Client.

    :ivar dns_resolvers: DnsResolversOperations operations
    :vartype dns_resolvers: azure.mgmt.dnsresolver.aio.operations.DnsResolversOperations
    :ivar inbound_endpoints: InboundEndpointsOperations operations
    :vartype inbound_endpoints: azure.mgmt.dnsresolver.aio.operations.InboundEndpointsOperations
    :ivar outbound_endpoints: OutboundEndpointsOperations operations
    :vartype outbound_endpoints: azure.mgmt.dnsresolver.aio.operations.OutboundEndpointsOperations
    :ivar dns_forwarding_rulesets: DnsForwardingRulesetsOperations operations
    :vartype dns_forwarding_rulesets: azure.mgmt.dnsresolver.aio.operations.DnsForwardingRulesetsOperations
    :ivar forwarding_rules: ForwardingRulesOperations operations
    :vartype forwarding_rules: azure.mgmt.dnsresolver.aio.operations.ForwardingRulesOperations
    :ivar virtual_network_links: VirtualNetworkLinksOperations operations
    :vartype virtual_network_links: azure.mgmt.dnsresolver.aio.operations.VirtualNetworkLinksOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        subscription_id: str,
        base_url: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = DnsResolverManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.dns_resolvers = DnsResolversOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.inbound_endpoints = InboundEndpointsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.outbound_endpoints = OutboundEndpointsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.dns_forwarding_rulesets = DnsForwardingRulesetsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.forwarding_rules = ForwardingRulesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.virtual_network_links = VirtualNetworkLinksOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "DnsResolverManagementClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
