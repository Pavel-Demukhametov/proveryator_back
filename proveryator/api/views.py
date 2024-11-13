# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status

class LectureUploadAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)  # Для обработки файлов

    def post(self, request):
        method = request.data.get('method')
        url = request.data.get('url')
        file = request.FILES.get('file')
        materials = request.data.get('materials')
        print(url)
        print(materials)
        print(file)
        if not materials:
            return Response(
                {"error": "Материалы лекции обязательны."},
                status=status.HTTP_400_BAD_REQUEST
            )

        if method == 'YandexDisk' and not url:
            return Response(
                {"error": "Для метода YandexDisk требуется ссылка."},
                status=status.HTTP_400_BAD_REQUEST
            )

        if method == 'Device' and not file:
            return Response(
                {"error": "Для метода Device требуется файл."},
                status=status.HTTP_400_BAD_REQUEST
            )


        response_data = {
            "message": "Лекция успешно обработана!",
            "method": method,
            "url": url if method == 'YandexDisk' else None,
            "file_name": file.name if file else None,
            "materials": materials,
        }
        return Response(response_data, status=status.HTTP_200_OK)