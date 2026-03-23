import grpc
import course_service_pb2_grpc
import course_service_pb2


def get_course(course_id: str):
    channel = grpc.insecure_channel('localhost:50051')
    stub = course_service_pb2_grpc.CourseServiceStub(channel)
    request = course_service_pb2.GetCourseRequest(course_id=course_id)
    response = stub.GetCourse(request)
    return response


if __name__ == '__main__':
    response = get_course('api-course')
    print(response)