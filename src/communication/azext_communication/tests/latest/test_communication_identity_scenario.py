# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from azure.cli.testsdk import ScenarioTest, ResourceGroupPreparer
from .utils import get_test_identity_id
import os
from .recording_processors import BodyReplacerProcessor, URIIdentityReplacer
from .preparers import CommunicationResourcePreparer


class CommunicationIdentityScenarios(ScenarioTest):

    def __init__(self, method_name):
        super().__init__(method_name, recording_processors=[
            URIIdentityReplacer(), 
            BodyReplacerProcessor(keys=["id", "token"])
        ])

    @ResourceGroupPreparer(name_prefix='clitestcommunication_MyResourceGroup'[:7], key='rg', parameter_name='rg')
    @CommunicationResourcePreparer(resource_group_parameter_name='rg')
    def test_issue_access_token(self, communication_resource_info):

        os.environ['AZURE_COMMUNICATION_CONNECTION_STRING'] = communication_resource_info[1]

        val = self.cmd(
            'az communication identity issue-access-token --scope chat').get_output_in_json()
        self.assertIsNotNone(val['token'])

    @ResourceGroupPreparer(name_prefix='clitestcommunication_MyResourceGroup'[:7], key='rg', parameter_name='rg')
    @CommunicationResourcePreparer(resource_group_parameter_name='rg')
    def test_issue_access_token_with_id(self, communication_resource_info):
        
        os.environ['AZURE_COMMUNICATION_CONNECTION_STRING'] = communication_resource_info[1]

        id = get_test_identity_id(self.is_live, self.in_recording, communication_resource_info[1])
        self.kwargs.update({'id': id})

        val = self.cmd(
            'az communication identity issue-access-token --scope chat --userid {id}').get_output_in_json()
        self.assertIsNotNone(val['token'])
    
    @ResourceGroupPreparer(name_prefix='clitestcommunication_MyResourceGroup'[:7], key='rg', parameter_name='rg')
    @CommunicationResourcePreparer(resource_group_parameter_name='rg')
    def test_issue_access_token_with_multiple_scopes(self, communication_resource_info):

        os.environ['AZURE_COMMUNICATION_CONNECTION_STRING'] = communication_resource_info[1]

        val = self.cmd(
            'az communication identity issue-access-token --scope voip chat').get_output_in_json()
        self.assertIsNotNone(val['token'])
        
    @ResourceGroupPreparer(name_prefix='clitestcommunication_MyResourceGroup'[:7], key='rg', parameter_name='rg')
    @CommunicationResourcePreparer(resource_group_parameter_name='rg')
    def test_revoke_access_tokens(self, communication_resource_info):
        os.environ['AZURE_COMMUNICATION_CONNECTION_STRING'] = communication_resource_info[1]

        id = get_test_identity_id(self.is_live, self.in_recording, communication_resource_info[1])
        self.kwargs.update({'id': id})

        val = self.cmd(
            'az communication identity issue-access-token --scope chat').get_output_in_json()
        self.assertIsNotNone(val['token'])

        self.cmd(
            'az communication identity revoke-access-tokens --userid {id}')
