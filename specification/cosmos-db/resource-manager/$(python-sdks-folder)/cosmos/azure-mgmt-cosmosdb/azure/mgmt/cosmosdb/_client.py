# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, TYPE_CHECKING

from azure.core.rest import HttpRequest, HttpResponse
from azure.mgmt.core import ARMPipelineClient

from ._configuration import CosmosDBManagementClientConfiguration
from ._serialization import Deserializer, Serializer
from .operations import (
    CassandraClustersOperations,
    CassandraDataCentersOperations,
    CassandraResourcesOperations,
    CollectionOperations,
    CollectionPartitionOperations,
    CollectionPartitionRegionOperations,
    CollectionRegionOperations,
    DataTransferJobsOperations,
    DatabaseAccountRegionOperations,
    DatabaseAccountsOperations,
    DatabaseOperations,
    GraphResourcesOperations,
    GremlinResourcesOperations,
    LocationsOperations,
    MongoDBResourcesOperations,
    NotebookWorkspacesOperations,
    Operations,
    PartitionKeyRangeIdOperations,
    PartitionKeyRangeIdRegionOperations,
    PercentileOperations,
    PercentileSourceTargetOperations,
    PercentileTargetOperations,
    PrivateEndpointConnectionsOperations,
    PrivateLinkResourcesOperations,
    RestorableDatabaseAccountsOperations,
    RestorableGremlinDatabasesOperations,
    RestorableGremlinGraphsOperations,
    RestorableGremlinResourcesOperations,
    RestorableMongodbCollectionsOperations,
    RestorableMongodbDatabasesOperations,
    RestorableMongodbResourcesOperations,
    RestorableSqlContainersOperations,
    RestorableSqlDatabasesOperations,
    RestorableSqlResourcesOperations,
    RestorableTableResourcesOperations,
    RestorableTablesOperations,
    ServiceOperations,
    SqlResourcesOperations,
    TableResourcesOperations,
)

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials import TokenCredential


class CosmosDBManagementClient:  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """Azure Cosmos DB Database Service Resource Provider REST API.

    :ivar database_accounts: DatabaseAccountsOperations operations
    :vartype database_accounts: azure.mgmt.cosmosdb.operations.DatabaseAccountsOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.cosmosdb.operations.Operations
    :ivar database: DatabaseOperations operations
    :vartype database: azure.mgmt.cosmosdb.operations.DatabaseOperations
    :ivar collection: CollectionOperations operations
    :vartype collection: azure.mgmt.cosmosdb.operations.CollectionOperations
    :ivar collection_region: CollectionRegionOperations operations
    :vartype collection_region: azure.mgmt.cosmosdb.operations.CollectionRegionOperations
    :ivar database_account_region: DatabaseAccountRegionOperations operations
    :vartype database_account_region:
     azure.mgmt.cosmosdb.operations.DatabaseAccountRegionOperations
    :ivar percentile_source_target: PercentileSourceTargetOperations operations
    :vartype percentile_source_target:
     azure.mgmt.cosmosdb.operations.PercentileSourceTargetOperations
    :ivar percentile_target: PercentileTargetOperations operations
    :vartype percentile_target: azure.mgmt.cosmosdb.operations.PercentileTargetOperations
    :ivar percentile: PercentileOperations operations
    :vartype percentile: azure.mgmt.cosmosdb.operations.PercentileOperations
    :ivar collection_partition_region: CollectionPartitionRegionOperations operations
    :vartype collection_partition_region:
     azure.mgmt.cosmosdb.operations.CollectionPartitionRegionOperations
    :ivar collection_partition: CollectionPartitionOperations operations
    :vartype collection_partition: azure.mgmt.cosmosdb.operations.CollectionPartitionOperations
    :ivar partition_key_range_id: PartitionKeyRangeIdOperations operations
    :vartype partition_key_range_id: azure.mgmt.cosmosdb.operations.PartitionKeyRangeIdOperations
    :ivar partition_key_range_id_region: PartitionKeyRangeIdRegionOperations operations
    :vartype partition_key_range_id_region:
     azure.mgmt.cosmosdb.operations.PartitionKeyRangeIdRegionOperations
    :ivar graph_resources: GraphResourcesOperations operations
    :vartype graph_resources: azure.mgmt.cosmosdb.operations.GraphResourcesOperations
    :ivar sql_resources: SqlResourcesOperations operations
    :vartype sql_resources: azure.mgmt.cosmosdb.operations.SqlResourcesOperations
    :ivar mongo_db_resources: MongoDBResourcesOperations operations
    :vartype mongo_db_resources: azure.mgmt.cosmosdb.operations.MongoDBResourcesOperations
    :ivar table_resources: TableResourcesOperations operations
    :vartype table_resources: azure.mgmt.cosmosdb.operations.TableResourcesOperations
    :ivar cassandra_resources: CassandraResourcesOperations operations
    :vartype cassandra_resources: azure.mgmt.cosmosdb.operations.CassandraResourcesOperations
    :ivar gremlin_resources: GremlinResourcesOperations operations
    :vartype gremlin_resources: azure.mgmt.cosmosdb.operations.GremlinResourcesOperations
    :ivar locations: LocationsOperations operations
    :vartype locations: azure.mgmt.cosmosdb.operations.LocationsOperations
    :ivar data_transfer_jobs: DataTransferJobsOperations operations
    :vartype data_transfer_jobs: azure.mgmt.cosmosdb.operations.DataTransferJobsOperations
    :ivar cassandra_clusters: CassandraClustersOperations operations
    :vartype cassandra_clusters: azure.mgmt.cosmosdb.operations.CassandraClustersOperations
    :ivar cassandra_data_centers: CassandraDataCentersOperations operations
    :vartype cassandra_data_centers: azure.mgmt.cosmosdb.operations.CassandraDataCentersOperations
    :ivar notebook_workspaces: NotebookWorkspacesOperations operations
    :vartype notebook_workspaces: azure.mgmt.cosmosdb.operations.NotebookWorkspacesOperations
    :ivar private_endpoint_connections: PrivateEndpointConnectionsOperations operations
    :vartype private_endpoint_connections:
     azure.mgmt.cosmosdb.operations.PrivateEndpointConnectionsOperations
    :ivar private_link_resources: PrivateLinkResourcesOperations operations
    :vartype private_link_resources: azure.mgmt.cosmosdb.operations.PrivateLinkResourcesOperations
    :ivar restorable_database_accounts: RestorableDatabaseAccountsOperations operations
    :vartype restorable_database_accounts:
     azure.mgmt.cosmosdb.operations.RestorableDatabaseAccountsOperations
    :ivar restorable_sql_databases: RestorableSqlDatabasesOperations operations
    :vartype restorable_sql_databases:
     azure.mgmt.cosmosdb.operations.RestorableSqlDatabasesOperations
    :ivar restorable_sql_containers: RestorableSqlContainersOperations operations
    :vartype restorable_sql_containers:
     azure.mgmt.cosmosdb.operations.RestorableSqlContainersOperations
    :ivar restorable_sql_resources: RestorableSqlResourcesOperations operations
    :vartype restorable_sql_resources:
     azure.mgmt.cosmosdb.operations.RestorableSqlResourcesOperations
    :ivar restorable_mongodb_databases: RestorableMongodbDatabasesOperations operations
    :vartype restorable_mongodb_databases:
     azure.mgmt.cosmosdb.operations.RestorableMongodbDatabasesOperations
    :ivar restorable_mongodb_collections: RestorableMongodbCollectionsOperations operations
    :vartype restorable_mongodb_collections:
     azure.mgmt.cosmosdb.operations.RestorableMongodbCollectionsOperations
    :ivar restorable_mongodb_resources: RestorableMongodbResourcesOperations operations
    :vartype restorable_mongodb_resources:
     azure.mgmt.cosmosdb.operations.RestorableMongodbResourcesOperations
    :ivar restorable_gremlin_databases: RestorableGremlinDatabasesOperations operations
    :vartype restorable_gremlin_databases:
     azure.mgmt.cosmosdb.operations.RestorableGremlinDatabasesOperations
    :ivar restorable_gremlin_graphs: RestorableGremlinGraphsOperations operations
    :vartype restorable_gremlin_graphs:
     azure.mgmt.cosmosdb.operations.RestorableGremlinGraphsOperations
    :ivar restorable_gremlin_resources: RestorableGremlinResourcesOperations operations
    :vartype restorable_gremlin_resources:
     azure.mgmt.cosmosdb.operations.RestorableGremlinResourcesOperations
    :ivar restorable_tables: RestorableTablesOperations operations
    :vartype restorable_tables: azure.mgmt.cosmosdb.operations.RestorableTablesOperations
    :ivar restorable_table_resources: RestorableTableResourcesOperations operations
    :vartype restorable_table_resources:
     azure.mgmt.cosmosdb.operations.RestorableTableResourcesOperations
    :ivar service: ServiceOperations operations
    :vartype service: azure.mgmt.cosmosdb.operations.ServiceOperations
    :param subscription_id: The ID of the target subscription. Required.
    :type subscription_id: str
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials.TokenCredential
    :keyword endpoint: Service URL. Default value is "https://management.azure.com".
    :paramtype endpoint: str
    :keyword api_version: Api Version. Default value is "2022-08-15-preview". Note that overriding
     this default value may result in unsupported behavior.
    :paramtype api_version: str
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
     Retry-After header is present.
    """

    def __init__(
        self,
        subscription_id: str,
        credential: "TokenCredential",
        *,
        endpoint: str = "https://management.azure.com",
        **kwargs: Any
    ) -> None:
        self._config = CosmosDBManagementClientConfiguration(
            subscription_id=subscription_id, credential=credential, **kwargs
        )
        self._client = ARMPipelineClient(base_url=endpoint, config=self._config, **kwargs)

        self._serialize = Serializer()
        self._deserialize = Deserializer()
        self._serialize.client_side_validation = False
        self.database_accounts = DatabaseAccountsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.operations = Operations(self._client, self._config, self._serialize, self._deserialize)
        self.database = DatabaseOperations(self._client, self._config, self._serialize, self._deserialize)
        self.collection = CollectionOperations(self._client, self._config, self._serialize, self._deserialize)
        self.collection_region = CollectionRegionOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.database_account_region = DatabaseAccountRegionOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.percentile_source_target = PercentileSourceTargetOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.percentile_target = PercentileTargetOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.percentile = PercentileOperations(self._client, self._config, self._serialize, self._deserialize)
        self.collection_partition_region = CollectionPartitionRegionOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.collection_partition = CollectionPartitionOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.partition_key_range_id = PartitionKeyRangeIdOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.partition_key_range_id_region = PartitionKeyRangeIdRegionOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.graph_resources = GraphResourcesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.sql_resources = SqlResourcesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.mongo_db_resources = MongoDBResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.table_resources = TableResourcesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.cassandra_resources = CassandraResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.gremlin_resources = GremlinResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.locations = LocationsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.data_transfer_jobs = DataTransferJobsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.cassandra_clusters = CassandraClustersOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.cassandra_data_centers = CassandraDataCentersOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.notebook_workspaces = NotebookWorkspacesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.private_endpoint_connections = PrivateEndpointConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.private_link_resources = PrivateLinkResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.restorable_database_accounts = RestorableDatabaseAccountsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.restorable_sql_databases = RestorableSqlDatabasesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.restorable_sql_containers = RestorableSqlContainersOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.restorable_sql_resources = RestorableSqlResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.restorable_mongodb_databases = RestorableMongodbDatabasesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.restorable_mongodb_collections = RestorableMongodbCollectionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.restorable_mongodb_resources = RestorableMongodbResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.restorable_gremlin_databases = RestorableGremlinDatabasesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.restorable_gremlin_graphs = RestorableGremlinGraphsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.restorable_gremlin_resources = RestorableGremlinResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.restorable_tables = RestorableTablesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.restorable_table_resources = RestorableTableResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.service = ServiceOperations(self._client, self._config, self._serialize, self._deserialize)

    def send_request(self, request: HttpRequest, **kwargs: Any) -> HttpResponse:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = client.send_request(request)
        <HttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.HttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, **kwargs)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> CosmosDBManagementClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)