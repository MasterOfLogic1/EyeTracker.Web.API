from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiParameter
from .models import Efis,Ecam,Pfd
from .serializers import EfisSerializer,EcamSerializer,PfdSerializer

@extend_schema(
    methods=["GET"],
    parameters=[
        OpenApiParameter(
            name="section_id",
            type=str,
            location=OpenApiParameter.QUERY,
            description="Optional query parameter to filter EFIS records by section_id."
        ),
        OpenApiParameter(
            name="recording_id",
            type=str,
            location=OpenApiParameter.QUERY,
            description="Optional query parameter to filter EFIS records by recording_id."
        ),
        OpenApiParameter(
            name="fixation_id",
            type=str,
            location=OpenApiParameter.QUERY,
            description="Optional query parameter to filter EFIS records by fixation_id."
        ),
    ],
    responses={200: EfisSerializer(many=True)},
    summary="Retrieve EFIS Data",
    description="Endpoint for retrieving EFIS records filtered by the 'Owner-Id' header and optionally by 'section_id'.",
    tags=["Efis"]
)
@extend_schema(
    methods=["POST"],
    request=EfisSerializer(many=True),  # Accepts a list of EFIS records
    responses={201: EfisSerializer(many=True)},
    summary="Create EFIS Data",
    description="Endpoint for creating EFIS records. Allows bulk creation. The user and owner_id are set internally.",
    tags=["Efis"]
)
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def data_efis(request):
    if request.method == 'GET':
        owner_id = request.user.user_id#request.headers.get('Owner-Id')
        #return Response({owner_id})
        if not owner_id:
            return Response({"error": "Owner-Id header is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Retrieve section_id from query parameters (if provided)
        section_id = request.query_params.get('section_id')
        # Retrieve recording_id from query parameters (if provided)
        recording_id = request.query_params.get('recording_id')
        # Retrieve fixation_id from query parameters (if provided)
        fixation_id = request.query_params.get('fixation_id')

        filters = {'owner_id': owner_id}
        if section_id:
            filters['section_id'] = section_id

        if recording_id:
            filters['recording_id'] = recording_id

        if fixation_id:
            fixation_id['fixation_id'] = fixation_id
        
        # Filter UserEfis records where the related user's primary key matches user_id.
        efis_records = Efis.objects.filter(**filters)
        if not efis_records.exists():
            return Response({"error": "No data found for this user"}, status=status.HTTP_404_NOT_FOUND)
        serializer = EfisSerializer(efis_records, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        user = request.user
        owner_id = user.user_id 

        if not isinstance(request.data, list):
            return Response({"error": "Payload must be a list of objects."}, status=status.HTTP_400_BAD_REQUEST)

        for item in request.data:
            item['user'] = user.id  # Set user field
            item['owner_id'] = owner_id  # Set owner_id field

        serializer = EfisSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Created successfully","data": serializer.data}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




#-----------------------------------------------------------------------------------------------------------------

@extend_schema(
    methods=["GET"],
    parameters=[
        OpenApiParameter(
            name="section_id",
            type=str,
            location=OpenApiParameter.QUERY,
            description="Optional query parameter to filter ECAM records by section_id."
        ),
        OpenApiParameter(
            name="recording_id",
            type=str,
            location=OpenApiParameter.QUERY,
            description="Optional query parameter to filter ECAM records by recording_id."
        ),
        OpenApiParameter(
            name="fixation_id",
            type=str,
            location=OpenApiParameter.QUERY,
            description="Optional query parameter to filter ECAM records by fixation_id."
        ),
    ],
    responses={200: EcamSerializer(many=True)},
    summary="Retrieve ECAM Data",
    description="Endpoint for retrieving ECAM records filtered by the 'Owner-Id' header and optionally by 'section_id'.",
    tags=["Ecam"]
)
@extend_schema(
    methods=["POST"],
    request=EcamSerializer(many=True),  # Accepts a list of ECAM records
    responses={201: EcamSerializer(many=True)},
    summary="Create ECAM Data",
    description="Endpoint for creating ECAM records. Allows bulk creation. The user and owner_id are set internally.",
    tags=["Ecam"]
)
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def data_ecam(request):
    if request.method == 'GET':
        owner_id = request.user.user_id#request.headers.get('Owner-Id')
        #return Response({owner_id})
        if not owner_id:
            return Response({"error": "Owner-Id header is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Retrieve section_id from query parameters (if provided)
        section_id = request.query_params.get('section_id')
        # Retrieve recording_id from query parameters (if provided)
        recording_id = request.query_params.get('recording_id')
        # Retrieve fixation_id from query parameters (if provided)
        fixation_id = request.query_params.get('fixation_id')

        filters = {'owner_id': owner_id}
        if section_id:
            filters['section_id'] = section_id

        if recording_id:
            filters['recording_id'] = recording_id

        if fixation_id:
            fixation_id['fixation_id'] = fixation_id
        
        # Filter UserEcam records where the related user's primary key matches user_id.
        Ecam_records = Ecam.objects.filter(**filters)
        if not Ecam_records.exists():
            return Response({"error": "No data found for this user"}, status=status.HTTP_404_NOT_FOUND)
        serializer = EcamSerializer(Ecam_records, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        user = request.user
        owner_id = user.user_id 

        if not isinstance(request.data, list):
            return Response({"error": "Payload must be a list of objects."}, status=status.HTTP_400_BAD_REQUEST)

        for item in request.data:
            item['user'] = user.id  # Set user field
            item['owner_id'] = owner_id  # Set owner_id field

        serializer = EcamSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Created successfully","data": serializer.data}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#------------------------------------------------------------------------------------------------------------------
@extend_schema(
    methods=["GET"],
    parameters=[
        OpenApiParameter(
            name="section_id",
            type=str,
            location=OpenApiParameter.QUERY,
            description="Optional query parameter to filter PFD records by section_id."
        ),
        OpenApiParameter(
            name="recording_id",
            type=str,
            location=OpenApiParameter.QUERY,
            description="Optional query parameter to filter PFD records by recording_id."
        ),
        OpenApiParameter(
            name="fixation_id",
            type=str,
            location=OpenApiParameter.QUERY,
            description="Optional query parameter to filter PFD records by fixation_id."
        ),
    ],
    responses={200: PfdSerializer(many=True)},
    summary="Retrieve PFD Data",
    description="Endpoint for retrieving PFD records filtered by the 'Owner-Id' header and optionally by 'section_id'.",
    tags=["Pfd"]
)
@extend_schema(
    methods=["POST"],
    request=PfdSerializer(many=True),  # Accepts a list of EFIS records
    responses={201: PfdSerializer(many=True)},
    summary="Create PFD Data",
    description="Endpoint for creating PFD records. Allows bulk creation. The user and owner_id are set internally.",
    tags=["Pfd"]
)
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def data_pfd(request):
    if request.method == 'GET':
        owner_id = request.user.user_id#request.headers.get('Owner-Id')
        #return Response({owner_id})
        if not owner_id:
            return Response({"error": "Owner-Id header is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Retrieve section_id from query parameters (if provided)
        section_id = request.query_params.get('section_id')
        # Retrieve recording_id from query parameters (if provided)
        recording_id = request.query_params.get('recording_id')
        # Retrieve fixation_id from query parameters (if provided)
        fixation_id = request.query_params.get('fixation_id')

        filters = {'owner_id': owner_id}
        if section_id:
            filters['section_id'] = section_id

        if recording_id:
            filters['recording_id'] = recording_id

        if fixation_id:
            fixation_id['fixation_id'] = fixation_id
        
        # Filter UserPfd records where the related user's primary key matches user_id.
        Pfd_records = Pfd.objects.filter(**filters)
        if not Pfd_records.exists():
            return Response({"error": "No data found for this user"}, status=status.HTTP_404_NOT_FOUND)
        serializer = PfdSerializer(Pfd_records, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        user = request.user
        owner_id = user.user_id 

        if not isinstance(request.data, list):
            return Response({"error": "Payload must be a list of objects."}, status=status.HTTP_400_BAD_REQUEST)

        for item in request.data:
            item['user'] = user.id  # Set user field
            item['owner_id'] = owner_id  # Set owner_id field

        serializer = PfdSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Created successfully","data": serializer.data}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)