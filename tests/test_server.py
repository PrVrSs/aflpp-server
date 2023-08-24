import grpc
import grpc_testing
from grpc_health.v1 import health, health_pb2


def test_health_check():
    test_server = grpc_testing.server_from_dictionary(
        descriptors_to_servicers={
            health_pb2.DESCRIPTOR.services_by_name['Health']: health.HealthServicer(),
        },
        time=grpc_testing.strict_real_time()
    )

    request = health_pb2.HealthCheckRequest(service='')

    health_check = test_server.invoke_unary_unary(
        method_descriptor=health_pb2.DESCRIPTOR.services_by_name['Health'].methods_by_name['Check'],
        invocation_metadata={},
        request=request,
        timeout=1,
    )

    response, metadata, code, details = health_check.termination()

    assert response.status == 1
    assert code == grpc.StatusCode.OK
