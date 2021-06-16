# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


# EXAMPLE: /Controller/put/Create controller
def step_controller_create(test, rg, rg_2, checks=None):
    if checks is None:
        checks = []
    test.cmd('az dnc controller create '
             '--location "eastus2euap" '
             '--resource-group "{rg}" '
             '--resource-name "{myController}"',
             checks=checks)
             

# EXAMPLE: /Controller/get/Get details of a controller
def step_controller_show(test, rg, rg_2, checks=None):
    if checks is None:
        checks = []
    test.cmd('az dnc controller show '
             '--resource-group "{rg}" '
             '--resource-name "{myController}"',
             checks=checks)


# EXAMPLE: /DelegatedSubnetService/put/put delegated subnet
def step_delegated_subnet_service_create(test, rg, rg_2, checks=None):
    if checks is None:
        checks = []
    test.cmd('az dnc delegated-subnet-service create '
             '--location "eastus2euap" '
             '--id "/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.DelegatedNetwork/controlle'
             'r/{myController}" '
             '--subnet-details-id "/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.Network/vir'
             'tualNetworks/{vn}/subnets/default" '
             '--resource-group "{rg}" '
             '--resource-name "delegated1"',
             checks=checks)


# EXAMPLE: /DelegatedSubnetService/get/Get details of a delegated subnet
def step_delegated_subnet_service_show(test, rg, rg_2, checks=None):
    if checks is None:
        checks = []
    test.cmd('az dnc delegated-subnet-service show '
             '--resource-group "{rg}" '
             '--resource-name "delegated1"',
             checks=checks)


# EXAMPLE: /DelegatedSubnetService/patch/patch delegated subnet
def step_delegated_subnet_service_patch_detail(test, rg, rg_2, checks=None):
    if checks is None:
        checks = []
    test.cmd('az dnc delegated-subnet-service patch-detail '
             '--tags key="value" '
             '--resource-group "{rg}" '
             '--resource-name "delegated1"',
             checks=checks)


# EXAMPLE: /OrchestratorInstanceService/put/Create orchestrator instance
def step_orchestrator_instance_service_create(test, rg, rg_2, checks=None):
    if checks is None:
        checks = []
    test.cmd('az dnc orchestrator-instance-service create '
             '--type "SystemAssigned" '
             '--location "eastus2euap" '
             '--api-server-endpoint "https://testk8s.cloudapp.net" '
             '--cluster-root-ca "ddsadsad344mfdsfdl" '
             '--id "/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.DelegatedNetwork/controlle'
             'r/{myController}" '
             '--orchestrator-app-id "546192d7-503f-477a-9cfe-4efc3ee2b6e1" '
             '--orchestrator-tenant-id "da6192d7-503f-477a-9cfe-4efc3ee2b6c3" '
             '--priv-link-resource-id "/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.Network'
             '/privateLinkServices/plresource1" '
             '--resource-group "{rg}" '
             '--resource-name "testk8s1"',
             checks=checks)

# EXAMPLE: /OrchestratorInstanceService/get/Get details of a orchestratorInstance
def step_orchestrator_instance_service_show(test, rg, rg_2, checks=None):
    if checks is None:
        checks = []
    test.cmd('az dnc orchestrator-instance-service show '
             '--resource-group "{rg}" '
             '--resource-name "testk8s1"',
             checks=checks)


# EXAMPLE: /OrchestratorInstanceService/get/Get OrchestratorInstance resources by resource group
def step_orchestrator_instance_service_list(test, rg, rg_2, checks=None):
    if checks is None:
        checks = []
    test.cmd('az dnc orchestrator-instance-service list '
             '--resource-group "{rg_2}"',
             checks=checks)


# EXAMPLE: /OrchestratorInstanceService/get/Get orchestratorInstance resources by subscription
def step_orchestrator_instance_service_list2(test, rg, rg_2, checks=None):
    if checks is None:
        checks = []
    test.cmd('az dnc orchestrator-instance-service list '
             '-g ""',
             checks=checks)


# EXAMPLE: /OrchestratorInstanceService/delete/Delete Orchestrator Instance
def step_orchestrator_instance_service_delete(test, rg, rg_2, checks=None):
    if checks is None:
        checks = []
    test.cmd('az dnc orchestrator-instance-service delete -y '
             '--resource-group "{rg}" '
             '--resource-name "k8stest1"',
             checks=checks)


# EXAMPLE: /Controller/delete/Delete controller
def step_controller_delete(test, rg, rg_2, checks=None):
    if checks is None:
        checks = []
    test.cmd('az dnc controller delete -y '
             '--resource-group "{rg}" '
             '--resource-name "{myController}"',
             checks=checks)


# EXAMPLE: /DelegatedNetwork/get/Get DelegatedController resources by subscription
def step_delegated_network_list(test, rg, rg_2, checks=None):
    if checks is None:
        checks = []
    test.cmd('az dnc delegated-network list '
             '-g ""',
             checks=checks)


# EXAMPLE: /DelegatedNetwork/get/Get DelegatedNetwork resources by resource group
def step_delegated_network_list2(test, rg, rg_2, checks=None):
    if checks is None:
        checks = []
    test.cmd('az dnc delegated-network list '
             '--resource-group "{rg_2}"',
             checks=checks)


# EXAMPLE: /DelegatedSubnetService/get/Get DelegatedSubnets resources by resource group
def step_delegated_subnet_service_list(test, rg, rg_2, checks=None):
    if checks is None:
        checks = []
    test.cmd('az dnc delegated-subnet-service list '
             '--resource-group "{rg_2}"',
             checks=checks)


# EXAMPLE: /DelegatedSubnetService/get/Get DelegatedSubnets resources by subscription
def step_delegated_subnet_service_list2(test, rg, rg_2, checks=None):
    if checks is None:
        checks = []
    test.cmd('az dnc delegated-subnet-service list '
             '-g ""',
             checks=checks)


# EXAMPLE: /DelegatedSubnetService/delete/delete delegated subnet
def step_delegated_subnet_service_delete(test, rg, rg_2, checks=None):
    if checks is None:
        checks = []
    test.cmd('az dnc delegated-subnet-service delete -y '
             '--resource-group "{rg}" '
             '--resource-name "delegated1"',
             checks=checks)